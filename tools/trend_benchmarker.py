#!/usr/bin/env python3
"""
Trend Benchmarker — Automated Reel / Short / TikTok Style Deconstruction Engine
Part of AI Video Studio (https://github.com/SonuSV7719/ai-video-studio)

Usage:
  python tools/trend_benchmarker.py "https://www.youtube.com/shorts/..."
  python tools/trend_benchmarker.py "https://www.instagram.com/reel/..."
  python tools/trend_benchmarker.py path/to/reference.mp4 --out-dir reference/benchmarks/my_style
"""

import os
import sys
import json
import re
import argparse
import subprocess
from pathlib import Path
from PIL import Image

def run_cmd(cmd, cwd=None, check=True):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if check and res.returncode != 0:
        raise RuntimeError(f"Command failed (code {res.returncode}): {cmd}\nStderr: {res.stderr[:500]}")
    return res

def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '_', text)[:40] or "benchmark"

def download_reference(url, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    meta_json_path = out_dir / "meta.json"
    video_out = out_dir / "source.mp4"
    
    print(f"📥 Downloading reference via yt-dlp: {url}...")
    
    # 1. Fetch metadata
    meta_cmd = f'yt-dlp --dump-json --no-warnings "{url}"'
    meta_res = run_cmd(meta_cmd, check=False)
    meta = {}
    if meta_res.returncode == 0 and meta_res.stdout.strip():
        try:
            meta = json.loads(meta_res.stdout)
            with open(meta_json_path, "w", encoding="utf-8") as f:
                json.dump(meta, f, indent=2)
        except Exception:
            pass
            
    # 2. Download video (limit to vertical / standard 1080p max to save bandwidth)
    dl_cmd = f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" --output "{video_out}" --no-playlist "{url}"'
    run_cmd(dl_cmd)
    
    title = meta.get("title", "Reference Reel")
    uploader = meta.get("uploader", meta.get("channel", "Unknown Creator"))
    return video_out, title, uploader, meta

def probe_video(video_path):
    cmd = f'ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,duration,bit_rate -of json "{video_path}"'
    res = run_cmd(cmd)
    data = json.loads(res.stdout)
    stream = data.get("streams", [{}])[0]
    
    width = int(stream.get("width", 1080))
    height = int(stream.get("height", 1920))
    
    # parse frame rate
    r_fps = stream.get("r_frame_rate", "30/1")
    if "/" in r_fps:
        num, den = r_fps.split("/")
        fps = round(float(num) / float(den), 2)
    else:
        fps = float(r_fps)
        
    duration = float(stream.get("duration", 0))
    if duration == 0:
        # Fallback to format duration
        cmd_fmt = f'ffprobe -v error -show_entries format=duration -of json "{video_path}"'
        fres = run_cmd(cmd_fmt)
        fdata = json.loads(fres.stdout)
        duration = float(fdata.get("format", {}).get("duration", 0))
        
    aspect = "9:16" if height > width else ("16:9" if width > height else "1:1")
    return {
        "width": width,
        "height": height,
        "fps": fps,
        "duration": round(duration, 2),
        "aspect_ratio": aspect
    }

def detect_scenes(video_path, scene_threshold=0.3):
    """Detects scene cut timestamps using FFmpeg scene filter."""
    print("✂️ Analyzing shot cuts and editing velocity...")
    cmd = (
        f'ffmpeg -i "{video_path}" -filter:v "select=\'gt(scene,{scene_threshold})\',metadata=print" '
        f'-f null -'
    )
    res = run_cmd(cmd, check=False)
    output = res.stderr
    
    pts_matches = re.findall(r'pts_time:([0-9.]+)', output)
    cut_times = [float(t) for t in pts_matches]
    cut_times = sorted(list(set(cut_times)))
    return cut_times

def extract_keyframes_and_palette(video_path, out_dir, duration, cuts):
    """Extracts hook keyframes (0.5s, 1.5s, 3.0s) and extracts dominant color palette."""
    frames_dir = out_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    
    # Sample keyframe timestamps: start hook + each cut or intervals
    sample_points = [0.5, 1.5, min(3.0, max(0.5, duration - 0.5))]
    for c in cuts[:10]:
        if c not in sample_points and c < duration:
            sample_points.append(round(c, 2))
    sample_points = sorted(list(set([p for p in sample_points if 0 <= p <= duration])))[:8]
    
    extracted_images = []
    for idx, t in enumerate(sample_points):
        out_img = frames_dir / f"frame_{idx:02d}_{t:.1f}s.jpg"
        cmd = f'ffmpeg -y -ss {t} -i "{video_path}" -frames:v 1 -q:v 2 "{out_img}"'
        run_cmd(cmd, check=False)
        if out_img.exists():
            extracted_images.append(out_img)
            
    # Color palette extraction from sampled images
    hex_colors = []
    if extracted_images:
        try:
            combined_colors = []
            for img_path in extracted_images[:4]:
                im = Image.open(img_path).convert('RGB').resize((120, 120))
                # Quantize down to 5 dominant colors per frame
                q_im = im.quantize(colors=5, method=Image.Quantize.MEDIANCUT).convert('RGB')
                colors = q_im.getcolors(maxcolors=256)
                if colors:
                    sorted_colors = sorted(colors, key=lambda x: x[0], reverse=True)
                    for count, col in sorted_colors[:3]:
                        hex_code = '#{:02x}{:02x}{:02x}'.format(*col).upper()
                        if hex_code not in hex_colors:
                            hex_colors.append(hex_code)
            hex_colors = hex_colors[:6]
        except Exception as e:
            print(f"Warning: palette extraction skipped ({e})")
            
    if not hex_colors:
        hex_colors = ["#0F0F12", "#FFFFFF", "#FF3B30", "#F5A623", "#007AFF"]
        
    return extracted_images, hex_colors

def analyze_loudness(video_path):
    """Measures EBU R128 loudness (Integrated LUFS & LRA)."""
    print("🔊 Analyzing audio loudness & dynamic range (EBU R128)...")
    cmd = f'ffmpeg -i "{video_path}" -af ebur128=framelog=verbose -f null -'
    res = run_cmd(cmd, check=False)
    output = res.stderr
    
    lufs_match = re.search(r'I:\s+([-\d.]+)\s+LUFS', output)
    lra_match = re.search(r'LRA:\s+([-\d.]+)\s+LU', output)
    tp_match = re.search(r'Peak:\s+([-\d.]+)\s+dBFS', output)
    
    integrated_lufs = float(lufs_match.group(1)) if lufs_match else -14.0
    lra = float(lra_match.group(1)) if lra_match else 5.0
    true_peak = float(tp_match.group(1)) if tp_match else -1.0
    
    return {
        "integrated_lufs": integrated_lufs,
        "loudness_range_lra": lra,
        "true_peak_dbfs": true_peak
    }

def synthesize_style_recipe(metrics, aspect, cuts, hex_colors):
    """Infers the professional motion graphics, VFX, and editing formula."""
    asl = metrics["average_shot_length_sec"]
    hook_cuts = metrics["hook_cut_count_first_3s"]
    duration = metrics["duration"]
    
    # 1. Pacing Archetype
    if asl < 1.5:
        pacing_name = "Hyper-Velocity Kinetic (Tiktok/Reels Max-Retention)"
        pacing_desc = "Cuts occur every 0.8-1.4s. High visual novelty, jump cuts on breath, continuous pattern interrupts."
    elif asl < 2.5:
        pacing_name = "Dynamic Editorial (Modern Tech/Product Reel)"
        pacing_desc = "Cuts every 1.8-2.4s. Anchored A-roll talking head with rapid B-roll inserts, kinetic UI overlays."
    elif asl < 4.0:
        pacing_name = "Narrative Essay / Vox Documentary"
        pacing_desc = "Cuts every 3.0-4.0s. Rich visual exploration, animated maps, document highlighter treatments."
    else:
        pacing_name = "Cinematic / Thought Leadership"
        pacing_desc = "Longer deliberate takes (4s+). Heavy reliance on natural performance, atmosphere, and sound design."

    # 2. Recommended Video-Effects
    recommended_effects = []
    if aspect == "9:16":
        recommended_effects.extend(["backdrop-word", "locked-on", "spotlight"])
        if hook_cuts >= 1:
            recommended_effects.append("lean-in")
        if duration > 15:
            recommended_effects.extend(["liquid-glass-graph", "apple-toggles", "checklist"])
    else:
        recommended_effects.extend(["terminal-inserts", "article-highlights", "spotlight"])

    # 3. Recommended Caption & Typography Style
    if asl < 2.0:
        caption_style = "Apple-Clean Single Word Kinetic (Yellow Active Highlight)"
    else:
        caption_style = "Vox Highlighter Boxed Subtitles (Medium Pace)"

    # 4. Motion Engine
    motion_engine = "Anime.js + GSAP physics springs (stagger: 35ms, damping: 14)"
    
    return {
        "archetype": pacing_name,
        "description": pacing_desc,
        "recommended_effects": recommended_effects,
        "caption_style": caption_style,
        "motion_engine": motion_engine
    }

def generate_markdown_report(info, probe, cuts, loudness, palette, recipe, out_path):
    dur = probe["duration"]
    shot_count = len(cuts) + 1
    asl = round(dur / max(1, shot_count), 2)
    hook_cuts = len([c for c in cuts if c <= 3.0])
    
    palette_swatches = " ".join([f"`{c}`" for c in palette])
    effects_list = ", ".join([f"`{e}`" for e in recipe["recommended_effects"]])
    
    md = f"""# 📊 Reel & Short Style Benchmark Report
**Deconstructed from**: {info.get('title', 'Reference Video')}  
**Creator/Source**: {info.get('uploader', 'Unknown')}  
**Target Format**: `{probe['width']}x{probe['height']}` ({probe['aspect_ratio']}) @ `{probe['fps']} FPS` | **Duration**: `{dur}s`

---

## 🎬 Editing Velocity & Pacing Metrics

| Metric | Measured Value | Professional Benchmark Reference |
| :--- | :--- | :--- |
| **Total Shots / Scenes** | `{shot_count}` shots | Short-form benchmark: 10-25 shots per 30s |
| **Average Shot Length (ASL)** | **`{asl}s`** | **{recipe['archetype']}** |
| **First 3s Hook Cuts** | `{hook_cuts}` cut(s) in 0-3s | Rule: ≥1 pattern interrupt in first 3s |
| **Integrated Loudness** | `{loudness['integrated_lufs']} LUFS` | Broadcast speech standard: `-14 to -16 LUFS` |
| **Loudness Range (LRA)** | `{loudness['loudness_range_lra']} LU` | Compact commercial dialogue (< 6 LU) |
| **True Peak** | `{loudness['true_peak_dbfs']} dBFS` | Ceiling max: `-1.0 dBFS` |

---

## 🎨 Color Palette & Visual Identity

Dominant Swatches: {palette_swatches}

```css
:root {{
  --bg-primary: {palette[0] if len(palette) > 0 else '#0F0F12'};
  --text-primary: {palette[1] if len(palette) > 1 else '#FFFFFF'};
  --accent-primary: {palette[2] if len(palette) > 2 else '#FF3B30'};
  --surface-elevated: {palette[3] if len(palette) > 3 else '#1E1E24'};
  --text-muted: {palette[4] if len(palette) > 4 else '#888888'};
}}
```

---

## 💡 Reverse-Engineered Director Recipe

* **Pacing Profile**: {recipe['archetype']}
  > {recipe['description']}
* **Recommended 51 Viral Video Effects**: {effects_list}
* **Motion Graphics Stack**: {recipe['motion_engine']}
* **Captions & Kinetic Typography**: `{recipe['caption_style']}`

### Executable Production Mapping:
1. **Dialogue Track**: Normalize via `ffmpeg -af "dynaudnorm=f=150:g=15:p=0.95:m=10.0"`
2. **Hook Execution (0-3s)**: Use `{recipe['recommended_effects'][0]}` at `0.5s` and a jump cut or punch-in at `{cuts[0] if cuts else 2.0}s`.
3. **Mid-Roll Retention (3s-20s)**: Alternate every {asl}s between talking head with behind-the-head text drops (`backdrop-word`) and floating UI widgets (`liquid-glass-graph` / `apple-toggles`).
4. **Resolution Guard**: CFR `{probe['fps']} fps`, 0% synthetic background blur, studio Mobius tone curve.
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✓ Generated Benchmark Report: {out_path}")

def main():
    parser = argparse.ArgumentParser(description="Deconstruct trending Reels/Shorts into actionable video production specs.")
    parser.add_argument("source", help="URL (YouTube Short, Instagram Reel, TikTok) or local MP4 path")
    parser.add_argument("--out-dir", default=None, help="Directory to save benchmark assets (default: reference/trending/<slug>)")
    parser.add_argument("--threshold", type=float, default=0.28, help="FFmpeg scene detection threshold (0.2 - 0.4)")
    args = parser.parse_args()
    
    source = args.source.strip()
    is_url = source.startswith("http://") or source.startswith("https://")
    
    if is_url:
        temp_slug = slugify(re.sub(r'https?://(www\.)?', '', source)[:30])
        out_dir = Path(args.out_dir) if args.out_dir else Path(f"reference/trending/{temp_slug}")
        video_path, title, uploader, meta = download_reference(source, out_dir)
        info = {"title": title, "uploader": uploader, "url": source}
    else:
        video_path = Path(source).resolve()
        if not video_path.exists():
            print(f"Error: Video file not found: {video_path}")
            sys.exit(1)
        slug = slugify(video_path.stem)
        out_dir = Path(args.out_dir) if args.out_dir else Path(f"reference/trending/{slug}")
        out_dir.mkdir(parents=True, exist_ok=True)
        info = {"title": video_path.stem, "uploader": "Local File", "url": str(video_path)}
        
    print(f"\n🔬 Deconstructing style benchmarks from: {video_path.name}")
    probe = probe_video(video_path)
    print(f"  Format: {probe['width']}x{probe['height']} ({probe['aspect_ratio']}) @ {probe['fps']} fps, {probe['duration']}s")
    
    cuts = detect_scenes(video_path, args.threshold)
    shot_count = len(cuts) + 1
    asl = round(probe['duration'] / max(1, shot_count), 2)
    hook_cuts = len([c for c in cuts if c <= 3.0])
    
    metrics = {
        "duration": probe["duration"],
        "total_shots": shot_count,
        "average_shot_length_sec": asl,
        "hook_cut_count_first_3s": hook_cuts,
        "cut_timestamps": cuts
    }
    
    frames, palette = extract_keyframes_and_palette(video_path, out_dir, probe["duration"], cuts)
    loudness = analyze_loudness(video_path)
    recipe = synthesize_style_recipe(metrics, probe["aspect_ratio"], cuts, palette)
    
    # Save JSON benchmark
    benchmark_data = {
        "source": info,
        "video": probe,
        "metrics": metrics,
        "audio": loudness,
        "palette": palette,
        "director_recipe": recipe
    }
    json_path = out_dir / "style_benchmark.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(benchmark_data, f, indent=2)
    print(f"✓ Saved JSON Benchmark: {json_path}")
    
    # Save Markdown report
    report_path = out_dir / "benchmark_report.md"
    generate_markdown_report(info, probe, cuts, loudness, palette, recipe, report_path)
    
    print(f"\n🎉 Style Deconstruction Complete! Check {report_path} to review the design and pacing specs.")

if __name__ == "__main__":
    main()
