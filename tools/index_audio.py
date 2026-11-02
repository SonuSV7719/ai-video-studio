import os
import sys
import csv
import json
import shutil
import subprocess
import re
from pathlib import Path

# Paths relative to project root (video-studio)
STUDIO_DIR = Path(__file__).resolve().parent.parent
INBOX_DIR = STUDIO_DIR / "assets" / "audio-inbox"
LICENSES_CSV = STUDIO_DIR / "assets" / "AUDIO_LICENSES.csv"
INDEX_JSON = STUDIO_DIR / "assets" / "audio-index.json"
MUSIC_DIR = STUDIO_DIR / "assets" / "music"
SFX_DIR = STUDIO_DIR / "assets" / "sfx"

MOOD_KEYWORDS = {
    "tech": ["tech", "digital", "future", "cyber", "ai", "synth", "electric", "data", "robotic"],
    "upbeat": ["upbeat", "energy", "happy", "fun", "dance", "pop", "bright", "groove", "joy"],
    "cinematic": ["cinematic", "epic", "dramatic", "trailer", "orchestral", "strings", "heroic"],
    "lofi": ["lofi", "chill", "relax", "soft", "jazz", "cozy", "study", "ambient", "calm"],
    "tense": ["tense", "dark", "suspense", "mystery", "horror", "drone", "eerie", "danger"],
}

SFX_KEYWORDS = {
    "whoosh": ["whoosh", "swoosh", "transition", "swipe", "air", "whip"],
    "hit": ["hit", "impact", "boom", "thud", "slam", "punch", "strike"],
    "ui": ["click", "pop", "tap", "button", "mouse", "keyboard", "beep"],
    "riser": ["riser", "sweep", "build", "tension", "climax"],
    "glitch": ["glitch", "static", "distort", "error", "noise"],
    "notification": ["notification", "chime", "bell", "ding", "alert", "ping"],
    "ambience": ["ambience", "room", "hum", "space", "wind", "background"],
}

def load_licenses():
    """Load valid licenses from CSV."""
    if not LICENSES_CSV.exists():
        print(f"Error: {LICENSES_CSV} not found.")
        return {}

    licenses = {}
    with open(LICENSES_CSV, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            filename = row.get("file", "").strip()
            if filename:
                licenses[filename.lower()] = row
    return licenses

def get_audio_duration(file_path):
    """Retrieve audio duration in seconds using ffprobe."""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(file_path)
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return float(res.stdout.strip())
    except Exception as e:
        print(f"Warning: Could not measure duration with ffprobe: {e}")
        return 0.0

def measure_lufs(file_path):
    """Measure integrated loudness in LUFS using FFmpeg ebur128 filter."""
    cmd = [
        "ffmpeg", "-y", "-i", str(file_path),
        "-af", "ebur128=framelog=verbose",
        "-f", "null", "-"
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        # Search for: Integrated loudness: \n I: -14.2 LUFS
        match = re.search(r"I:\s*(-?\d+(?:\.\d+)?)\s*LUFS", res.stderr)
        if match:
            return float(match.group(1))
    except Exception as e:
        print(f"Warning: Could not measure LUFS: {e}")
    return -14.0

def measure_bpm(file_path, duration):
    """Estimate BPM using librosa if duration allows, otherwise return 0."""
    if duration < 3.0:
        return 0.0
    try:
        import librosa
        y, sr = librosa.load(str(file_path), sr=22050, duration=min(duration, 30.0))
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        if hasattr(tempo, "__len__"):
            return round(float(tempo[0]), 1)
        return round(float(tempo), 1)
    except Exception:
        # Fallback default estimate if librosa not available or audio too short
        return 120.0

def classify_mood_and_type(filename, duration):
    """Determine if audio is SFX or Music and suggest mood/category."""
    name_lower = filename.lower()
    
    if duration < 4.0:
        audio_type = "sfx"
        # Match SFX subfolder
        for cat, kws in SFX_KEYWORDS.items():
            if any(k in name_lower for k in kws):
                return audio_type, cat
        return audio_type, "ui" # default sfx
    else:
        audio_type = "music"
        for mood, kws in MOOD_KEYWORDS.items():
            if any(k in name_lower for k in kws):
                return audio_type, mood
        return audio_type, "tech" # default music

def run_index():
    print(f"=== Audio Indexer Scanning {INBOX_DIR} ===")
    licenses = load_licenses()
    
    existing_index = []
    if INDEX_JSON.exists():
        try:
            with open(INDEX_JSON, "r", encoding="utf-8") as f:
                existing_index = json.load(f)
        except Exception:
            existing_index = []

    indexed_files = {item["file"]: item for item in existing_index}
    
    inbox_files = [f for f in INBOX_DIR.iterdir() if f.is_file() and not f.name.startswith(".")]
    if not inbox_files:
        print("assets/audio-inbox is empty. No files to process.")
        return

    processed = 0
    rejected = 0

    for file_path in inbox_files:
        fname = file_path.name
        lic_row = licenses.get(fname.lower())
        
        # Check license presence
        if not lic_row:
            print(f"[REJECTED / UNVERIFIED] '{fname}' has NO entry in AUDIO_LICENSES.csv. Skipping.")
            rejected += 1
            continue
            
        comm_ok = lic_row.get("commercial_ok", "").strip().lower()
        lic_name = lic_row.get("license", "").strip().lower()
        
        # Check commercial and NC/ND restrictions
        if comm_ok != "y" or "nc" in lic_name or "nd" in lic_name or "noncommercial" in lic_name:
            print(f"[REJECTED / RESTRICTED] '{fname}' is non-commercial or has ND restrictions. Skipping.")
            rejected += 1
            continue

        print(f"[ACCEPTED] Processing '{fname}' (License: {lic_row.get('license')})...")
        
        duration = round(get_audio_duration(file_path), 2)
        lufs = measure_lufs(file_path)
        bpm = measure_bpm(file_path, duration)
        audio_type, mood_cat = classify_mood_and_type(fname, duration)
        
        # Determine target folder
        if audio_type == "sfx":
            target_folder = SFX_DIR / mood_cat
        else:
            target_folder = MUSIC_DIR / mood_cat
            
        target_folder.mkdir(parents=True, exist_ok=True)
        target_path = target_folder / fname
        
        shutil.move(str(file_path), str(target_path))
        print(f"  → Moved to {target_path.relative_to(STUDIO_DIR)}")
        
        item_entry = {
            "file": fname,
            "type": audio_type,
            "category": mood_cat,
            "rel_path": str(target_path.relative_to(STUDIO_DIR)).replace("\\", "/"),
            "duration": duration,
            "bpm": bpm,
            "LUFS": lufs,
            "mood": mood_cat,
            "license": lic_row.get("license", ""),
            "attribution_required": lic_row.get("attribution_required", "n").lower() == "y",
            "credit_text": lic_row.get("credit_text", "None"),
        }
        
        indexed_files[fname] = item_entry
        processed += 1

    # Save updated audio-index.json
    with open(INDEX_JSON, "w", encoding="utf-8") as f:
        json.dump(list(indexed_files.values()), f, indent=2)

    print(f"\nIndexing Complete: {processed} accepted & cataloged, {rejected} rejected.")
    print(f"Audio Index written to: {INDEX_JSON}")

if __name__ == "__main__":
    run_index()
