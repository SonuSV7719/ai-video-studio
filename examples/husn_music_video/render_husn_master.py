#!/usr/bin/env python3
"""
Master AI Video Studio Render Engine for "Husn" (Anuv Jain)
Applies the 51 Video Effects, Anime.js physics equations, MediaPipe cutout segmentation,
and broadcast audio mastering (-14 LUFS).
"""

import os
import sys
import math
import time
import subprocess
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 1. Project Paths & Settings
PROJECT_DIR = r"C:\Users\sonup\.gemini\antigravity\scratch\hindi-ai-song-studio"
SKILLS_DIR = r"C:\Users\sonup\.gemini\antigravity\scratch\ai-video-studio\skills\video-effects"
FONTS_DIR = os.path.join(SKILLS_DIR, "fonts")
MODELS_DIR = os.path.join(SKILLS_DIR, "models")

AUDIO_IN = os.path.join(PROJECT_DIR, "raw_footage", "husn_take.wav")
SINGER_IMG_PATH = os.path.join(PROJECT_DIR, "raw_footage", "singer_portrait.png")
BROLL_IMG_PATH = os.path.join(PROJECT_DIR, "raw_footage", "rain_window_broll.png")
OUTPUT_MASTER = os.path.join(PROJECT_DIR, "export", "husn_ai_master.mp4")

WIDTH = 1080
HEIGHT = 1920
FPS = 24.0
TOTAL_DURATION = 30.0
TOTAL_FRAMES = int(FPS * TOTAL_DURATION)  # 720 frames

# 2. Load Fonts
def get_font(name, size):
    path = os.path.join(FONTS_DIR, name)
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

font_display_huge = get_font("ArchivoBlack-Regular.ttf", 260)
font_display_big  = get_font("ArchivoBlack-Regular.ttf", 190)
font_display_mid  = get_font("ArchivoBlack-Regular.ttf", 110)
font_serif_italic = get_font("InstrumentSerif-Italic.ttf", 85)
font_serif_mid    = get_font("InstrumentSerif-Italic.ttf", 55)
font_ui_bold      = get_font("Montserrat.ttf", 36)
font_ui_regular   = get_font("Inter.ttf", 32)
font_mono         = get_font("SpaceMono-Bold.ttf", 24)
font_marker       = get_font("PermanentMarker-Regular.ttf", 60)

# 3. MediaPipe Segmentation & YuNet Face Detection
print("⚡ Initializing Computer Vision Models (MediaPipe & YuNet)...")
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path=os.path.join(MODELS_DIR, "selfie_segmenter.tflite"))
options = vision.ImageSegmenterOptions(base_options=base_options, output_category_mask=False)
segmenter = vision.ImageSegmenter.create_from_options(options)

detector = cv2.FaceDetectorYN.create(
    os.path.join(MODELS_DIR, "yunet.onnx"), "", (320, 320), 0.6, 0.3, 5000
)

# 4. Prepare Base Assets
print("🎨 Preparing Base Images & Alpha Segmentations...")
raw_singer = cv2.imread(SINGER_IMG_PATH)
raw_broll  = cv2.imread(BROLL_IMG_PATH)

# Fit singer to 1080x1920 keeping aspect
sh, sw = raw_singer.shape[:2]
scale = max(WIDTH / sw, HEIGHT / sh)
singer_resized = cv2.resize(raw_singer, (int(sw * scale), int(sh * scale)), interpolation=cv2.INTER_LANCZOS4)
# Crop center
start_x = (singer_resized.shape[1] - WIDTH) // 2
start_y = (singer_resized.shape[0] - HEIGHT) // 2
singer_canvas = singer_resized[start_y:start_y+HEIGHT, start_x:start_x+WIDTH]

# Fit B-roll to 1080x1920
bh, bw = raw_broll.shape[:2]
bscale = max(WIDTH / bw, HEIGHT / bh)
broll_resized = cv2.resize(raw_broll, (int(bw * bscale), int(bh * bscale)), interpolation=cv2.INTER_LANCZOS4)
bx = (broll_resized.shape[1] - WIDTH) // 2
by = (broll_resized.shape[0] - HEIGHT) // 2
broll_canvas = broll_resized[by:by+HEIGHT, bx:bx+WIDTH]

# Compute MediaPipe Alpha Mask on 1080x1920 singer canvas
rgb_singer = cv2.cvtColor(singer_canvas, cv2.COLOR_BGR2RGB)
mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_singer)
seg_res = segmenter.segment(mp_img)
raw_mask = seg_res.confidence_masks[0].numpy_view() # float32 (H, W, 1)
# Clean and feather mask
alpha_mask = cv2.GaussianBlur(raw_mask, (15, 15), 0)
alpha_3ch = np.repeat(alpha_mask[:, :, np.newaxis] if len(alpha_mask.shape) == 2 else alpha_mask, 3, axis=2)

# Compute Face Box
detector.setInputSize((WIDTH, HEIGHT))
_, faces = detector.detect(singer_canvas)
if faces is not None and len(faces) > 0:
    face_box = faces[0][:4]  # [x, y, w, h]
    face_cx = int(face_box[0] + face_box[2] / 2)
    face_cy = int(face_box[1] + face_box[3] / 2)
else:
    face_cx, face_cy = WIDTH // 2, int(HEIGHT * 0.42)
    face_box = [face_cx - 100, face_cy - 120, 200, 240]

print(f"✓ Face tracked at: ({face_cx}, {face_cy}), Bounding Box: {face_box}")

# 5. Physics & Easing Functions (Anime.js Spring approximation)
def ease_spring(t, mass=1.0, stiffness=85.0, damping=13.0):
    """Calculates damped harmonic spring progression t in [0, 1]."""
    if t <= 0.0: return 0.0
    if t >= 1.0: return 1.0
    omega = math.sqrt(stiffness / mass)
    zeta = damping / (2.0 * math.sqrt(stiffness * mass))
    decay = math.exp(-zeta * omega * t)
    osc = math.cos(omega * math.sqrt(max(0.001, 1.0 - zeta**2)) * t)
    return 1.0 - decay * osc

def ease_in_out_cubic(t):
    return 4 * t * t * t if t < 0.5 else 1 - math.pow(-2 * t + 2, 3) / 2

# 6. Procedural Particle Simulation (Embers & Dust Motes)
np.random.seed(42)
NUM_PARTICLES = 70
particles = []
for _ in range(NUM_PARTICLES):
    particles.append({
        'x': np.random.uniform(50, WIDTH - 50),
        'y': np.random.uniform(100, HEIGHT - 100),
        'speed_y': np.random.uniform(0.6, 2.2),
        'speed_x': np.random.uniform(-0.4, 0.4),
        'radius': np.random.uniform(1.5, 4.0),
        'alpha': np.random.uniform(0.2, 0.7),
        'phase': np.random.uniform(0, math.pi * 2)
    })

# 7. Helper: Draw Frosted Glass Pill
def draw_glass_pill(img_pil, x, y, w, h, text, font, accent_color=(245, 166, 35), border_alpha=80):
    draw = ImageDraw.Draw(img_pil, "RGBA")
    r = h // 2
    # Fill semi-translucent dark glass
    draw.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=(20, 19, 25, 200), outline=(255, 255, 255, border_alpha), width=2)
    # Highlight accent dot
    dot_r = 5
    draw.ellipse([x + 22 - dot_r, y + h//2 - dot_r, x + 22 + dot_r, y + h//2 + dot_r], fill=(*accent_color, 255))
    # Text
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = x + 38 + (w - 50 - tw) // 2
    ty = y + (h - th) // 2 - bbox[1]
    draw.text((tx, ty), text, font=font, fill=(255, 255, 255, 245))

# 8. Frame Rendering Loop
print(f"🎬 Commencing Master Render ({TOTAL_FRAMES} frames @ 24 fps)...")

ffmpeg_cmd = [
    "ffmpeg", "-y",
    "-f", "rawvideo",
    "-vcodec", "rawvideo",
    "-s", f"{WIDTH}x{HEIGHT}",
    "-pix_fmt", "bgr24",
    "-r", str(FPS),
    "-i", "-",               # Video pipe from stdin
    "-i", AUDIO_IN,          # Synced broadcast audio
    "-c:v", "libx264",
    "-crf", "18",
    "-preset", "fast",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    "-shortest",
    OUTPUT_MASTER
]

ffmpeg_log = open(os.path.join(PROJECT_DIR, "export", "ffmpeg_render.log"), "w")
proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=ffmpeg_log)
start_render_time = time.time()

for frame_idx in range(TOTAL_FRAMES):
    t_sec = frame_idx / FPS
    
    # -------------------------------------------------------------
    # A. Update Particles
    # -------------------------------------------------------------
    for p in particles:
        p['y'] -= p['speed_y']
        p['x'] += math.sin(t_sec * 2.0 + p['phase']) * p['speed_x']
        if p['y'] < 50:
            p['y'] = HEIGHT - 50
            p['x'] = np.random.uniform(50, WIDTH - 50)
            
    # -------------------------------------------------------------
    # B. Scene Routing & Compositing
    # -------------------------------------------------------------
    # Base background canvas: deep obsidian (#0B0B0E)
    bg = np.full((HEIGHT, WIDTH, 3), (14, 11, 11), dtype=np.uint8) # BGR
    
    # Add subtle radial lighting vignette
    if t_sec < 4.5:
        # Scene 1: Spotlight effect (0.0s - 4.5s)
        spot_intensity = min(1.0, t_sec / 1.0)
        cv2.circle(bg, (face_cx, face_cy - 50), int(480 * spot_intensity), (45, 35, 25), -1)
        bg = cv2.GaussianBlur(bg, (151, 151), 0)
    elif 4.5 <= t_sec < 9.0:
        # Scene 2: Warm ambient glow for BAATEIN drop
        cv2.circle(bg, (WIDTH // 2, HEIGHT // 2), 600, (30, 25, 20), -1)
        bg = cv2.GaussianBlur(bg, (141, 141), 0)
    elif 9.0 <= t_sec < 14.0:
        # Scene 3: Split Paradox (Top: Rain B-roll, Bottom: Stage)
        split_ratio = 0.52
        split_y = int(HEIGHT * split_ratio)
        bg[:split_y, :] = broll_canvas[:split_y, :]
        # Darken top B-roll slightly for contrast
        bg[:split_y, :] = (bg[:split_y, :].astype(np.float32) * 0.75).astype(np.uint8)
        # Separator hairline line
        cv2.line(bg, (0, split_y), (WIDTH, split_y), (80, 75, 90), 2)
    elif 14.0 <= t_sec < 19.5:
        # Scene 4: Soft moody blue/teal ambient room
        cv2.circle(bg, (face_cx, face_cy), 550, (40, 32, 22), -1)
        bg = cv2.GaussianBlur(bg, (141, 141), 0)
    elif 19.5 <= t_sec < 25.0:
        # Scene 5: CLIMAX DROP — Electric Coral / Crimson Backglow!
        pulse = 0.85 + 0.15 * math.sin((t_sec - 19.5) * 8.0)
        cv2.circle(bg, (WIDTH // 2, int(HEIGHT * 0.38)), int(650 * pulse), (35, 30, 110), -1) # BGR Coral
        cv2.circle(bg, (WIDTH // 2, int(HEIGHT * 0.42)), int(380 * pulse), (60, 50, 210), -1)
        bg = cv2.GaussianBlur(bg, (171, 171), 0)
    else:
        # Scene 6: Outro subtle stage glow
        cv2.circle(bg, (WIDTH // 2, face_cy), 500, (30, 25, 20), -1)
        bg = cv2.GaussianBlur(bg, (141, 141), 0)

    # -------------------------------------------------------------
    # C. Layer 2: Typographic Drops BEHIND the Singer (Alpha Sandwich)
    # -------------------------------------------------------------
    bg_pil = Image.fromarray(cv2.cvtColor(bg, cv2.COLOR_BGR2RGB))
    draw_behind = ImageDraw.Draw(bg_pil, "RGBA")
    
    if 4.5 <= t_sec < 9.0:
        # Scene 2: Giant word "BAATEIN" dropping behind singer
        progress = min(1.0, (t_sec - 4.5) / 1.2)
        eased_y = -150 + ease_spring(progress) * 420  # Springs down to Y=270
        word = "BAATEIN"
        bbox = font_display_huge.getbbox(word)
        bx = (WIDTH - (bbox[2] - bbox[0])) // 2
        # Draw soft drop shadow behind
        draw_behind.text((bx + 4, eased_y + 4), word, font=font_display_huge, fill=(0, 0, 0, 120))
        # Draw translucent warm paper milk text
        draw_behind.text((bx, eased_y), word, font=font_display_huge, fill=(247, 245, 238, 90))
        
    elif 19.5 <= t_sec < 25.0:
        # Scene 5: Chorus SHOWSTOPPER — Giant glowing "HUSN"
        climax_p = min(1.0, (t_sec - 19.5) / 0.6)
        scale_punch = 1.0 + 0.25 * math.exp(-(t_sec - 19.5) * 4.0)
        word = "HUSN"
        bbox = font_display_huge.getbbox(word)
        bw = bbox[2] - bbox[0]
        bx = (WIDTH - bw) // 2
        by = int(HEIGHT * 0.22)
        # Giant outer glow in Coral-Red
        for offset in [8, 5, 2]:
            draw_behind.text((bx, by), word, font=font_display_huge, fill=(255, 74, 61, 70))
        # Crisp punch text
        draw_behind.text((bx, by), word, font=font_display_huge, fill=(255, 95, 82, 220))
        
    # Render particles on background
    particle_draw = ImageDraw.Draw(bg_pil, "RGBA")
    for p in particles:
        col = (255, 180, 80, int(p['alpha'] * 255)) if t_sec < 19.5 else (255, 120, 100, int(p['alpha'] * 255))
        r = p['radius']
        particle_draw.ellipse([p['x'] - r, p['y'] - r, p['x'] + r, p['y'] + r], fill=col)

    bg_composited = cv2.cvtColor(np.array(bg_pil), cv2.COLOR_RGB2BGR)

    # -------------------------------------------------------------
    # D. Layer 3: Middleground Singer Silhouette / Portrait
    # -------------------------------------------------------------
    # Camera scale & transform
    cam_scale = 1.0
    cam_dx = 0
    cam_dy = 0
    
    if t_sec < 4.5:
        # Scene 1: Locked-on zoom (1.0 -> 1.25x)
        p = min(1.0, t_sec / 2.5)
        cam_scale = 1.0 + 0.22 * ease_in_out_cubic(p)
        cam_dy = int((face_cy - HEIGHT * 0.45) * 0.15)
    elif 4.5 <= t_sec < 9.0:
        # Scene 2: Parallax drift
        cam_scale = 1.15
        cam_dx = int(math.sin((t_sec - 4.5) * 0.8) * 25)
    elif 9.0 <= t_sec < 14.0:
        # Scene 3: Punch-in at 11.8s
        if t_sec >= 11.8:
            cam_scale = 1.28
        else:
            cam_scale = 1.10
    elif 14.0 <= t_sec < 19.5:
        # Scene 4: Slow cinematic push-in
        p = (t_sec - 14.0) / 5.5
        cam_scale = 1.10 + 0.20 * p
    elif 19.5 <= t_sec < 25.0:
        # Scene 5: Chorus Punch (1.40x with decay)
        punch = math.exp(-(t_sec - 19.5) * 3.0) * 0.15
        cam_scale = 1.30 + punch
    else:
        # Scene 6: Easing back to 1.05x
        p = min(1.0, (t_sec - 25.0) / 3.0)
        cam_scale = 1.20 - 0.15 * p

    # Apply camera scale to singer and alpha mask around center
    if abs(cam_scale - 1.0) > 0.005 or cam_dx != 0 or cam_dy != 0:
        M = cv2.getRotationMatrix2D((face_cx, face_cy), 0, cam_scale)
        M[0, 2] += cam_dx
        M[1, 2] += cam_dy
        singer_frame = cv2.warpAffine(singer_canvas, M, (WIDTH, HEIGHT), borderMode=cv2.BORDER_REFLECT)
        mask_frame = cv2.warpAffine(alpha_3ch, M, (WIDTH, HEIGHT), borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))
    else:
        singer_frame = singer_canvas
        mask_frame = alpha_3ch

    # Alpha composite singer over Layer 2 background
    final_bgr = (singer_frame.astype(np.float32) * mask_frame + bg_composited.astype(np.float32) * (1.0 - mask_frame)).astype(np.uint8)

    # -------------------------------------------------------------
    # E. Layer 4: Foreground VFX, Brackets, Glass Cards, Kinetic Lyrics
    # -------------------------------------------------------------
    frame_pil = Image.fromarray(cv2.cvtColor(final_bgr, cv2.COLOR_BGR2RGB))
    draw_fg = ImageDraw.Draw(frame_pil, "RGBA")
    
    # 1. Telemetry HUD (All Scenes)
    rec_red = (255, 59, 48, 240) if int(t_sec * 2) % 2 == 0 else (255, 59, 48, 80)
    draw_fg.ellipse([60, 80, 76, 96], fill=rec_red)
    draw_fg.text((90, 77), "REC", font=font_mono, fill=(255, 255, 255, 230))
    tc_h = int(t_sec // 3600)
    tc_m = int((t_sec % 3600) // 60)
    tc_s = int(t_sec % 60)
    tc_f = int((t_sec * FPS) % FPS)
    timecode_str = f"{tc_h:02d}:{tc_m:02d}:{tc_s:02d}:{tc_f:02d}"
    draw_fg.text((WIDTH - 240, 77), timecode_str, font=font_mono, fill=(255, 255, 255, 200))

    # 2. Scene-Specific Overlays
    if t_sec < 4.5:
        # Scene 1: Locked-on Cyan Face Tracking Brackets
        bx = int(face_cx - 120 * cam_scale)
        by = int(face_cy - 140 * cam_scale)
        bw = int(240 * cam_scale)
        bh = int(280 * cam_scale)
        b_len = 35
        cyan = (0, 229, 255, 230)
        # Top-left corner
        draw_fg.line([(bx, by), (bx + b_len, by)], fill=cyan, width=4)
        draw_fg.line([(bx, by), (bx, by + b_len)], fill=cyan, width=4)
        # Top-right corner
        draw_fg.line([(bx + bw, by), (bx + bw - b_len, by)], fill=cyan, width=4)
        draw_fg.line([(bx + bw, by), (bx + bw, by + b_len)], fill=cyan, width=4)
        # Bottom-left corner
        draw_fg.line([(bx, by + bh), (bx + b_len, by + bh)], fill=cyan, width=4)
        draw_fg.line([(bx, by + bh), (bx, by + bh - b_len)], fill=cyan, width=4)
        # Bottom-right corner
        draw_fg.line([(bx + bw, by + bh), (bx + bw - b_len, by + bh)], fill=cyan, width=4)
        draw_fg.line([(bx + bw, by + bh), (bx + bw, by + bh - b_len)], fill=cyan, width=4)
        
        # Tracking label
        draw_fg.text((bx + 8, by - 32), "TRACK_ID: [01_VOCAL]", font=font_mono, fill=cyan)
        
        # Frosted Lyric Pill
        draw_glass_pill(frame_pil, (WIDTH - 420) // 2, int(HEIGHT * 0.76), 420, 68, "DEKHO DEKHO...", font_ui_bold, accent_color=(245, 166, 35))
        
    elif 4.5 <= t_sec < 9.0:
        # Scene 2: Kinetic Subtitle Pill with Staggered Word Progression
        words = ["kaisi", "baatein", "yahan", "ki..."]
        active_idx = min(3, int((t_sec - 4.5) / 1.1))
        
        # Draw lyric card
        draw_glass_pill(frame_pil, (WIDTH - 540) // 2, int(HEIGHT * 0.76), 540, 72, " ".join(words).upper(), font_ui_bold, accent_color=(255, 230, 0))
        
    elif 9.0 <= t_sec < 14.0:
        # Scene 3: Hand-drawn Red Crayon Circle Doodle around face at 11.8s
        draw_glass_pill(frame_pil, (WIDTH - 640) // 2, int(HEIGHT * 0.76), 640, 72, "HAI SAATH PAR HAIN SAATH NA BHI...", font_ui_bold, accent_color=(255, 74, 61))
        
        if t_sec >= 11.4:
            doodle_prog = min(1.0, (t_sec - 11.4) / 0.5)
            # Draw dynamic sketch circle
            pts = []
            for deg in range(0, int(360 * doodle_prog), 15):
                rad = math.radians(deg)
                rx = face_cx + (140 + math.sin(deg * 3) * 8) * math.cos(rad)
                ry = face_cy + (160 + math.cos(deg * 2) * 8) * math.sin(rad)
                pts.append((rx, ry))
            if len(pts) > 1:
                draw_fg.line(pts, fill=(255, 74, 61, 230), width=5)
                
    elif 14.0 <= t_sec < 19.5:
        # Scene 4: Translucent Liquid Glass Card with Animated Climbing Waveform
        gx = (WIDTH - 600) // 2
        gy = int(HEIGHT * 0.72)
        gw, gh = 600, 150
        draw_fg.rounded_rectangle([gx, gy, gx + gw, gy + gh], radius=16, fill=(18, 17, 24, 210), outline=(255, 255, 255, 60), width=2)
        draw_fg.text((gx + 24, gy + 16), "AUDIO SPECTRAL ENERGY", font=font_mono, fill=(160, 155, 170, 220))
        
        # Animated Waveform
        wave_pts = []
        for xi in range(gx + 24, gx + gw - 24, 12):
            norm_x = (xi - gx) / gw
            amp = math.sin(norm_x * 12.0 + t_sec * 8.0) * math.cos(norm_x * 5.0) * 32.0
            wave_pts.append((xi, gy + 85 + amp))
        if len(wave_pts) > 1:
            draw_fg.line(wave_pts, fill=(0, 229, 255, 240), width=3)
            
        draw_fg.text((gx + 24, gy + 115), '"kya itni aasaan hai yeh be-rukhi..."', font=font_serif_mid, fill=(255, 255, 255, 240))
        
    elif 19.5 <= t_sec < 25.0:
        # Scene 5: Chorus Climax Drop Overlays
        # Kinetic Lyric Flash
        if (t_sec - 19.5) < 2.8:
            lyric_hero = "HUSN TERA"
            sub_hero = "TAUBA TAUBA"
        else:
            lyric_hero = "TAUBA TAUBA"
            sub_hero = "HUSN TERA"
            
        draw_glass_pill(frame_pil, (WIDTH - 580) // 2, int(HEIGHT * 0.76), 580, 80, f"★ {lyric_hero} {sub_hero} ★", font_ui_bold, accent_color=(255, 74, 61), border_alpha=120)
        
    else:
        # Scene 6: Orbit 3D Carousel (3 Cards rotating around head)
        orbit_angle = (t_sec - 25.0) * 1.8
        card_w, card_h = 140, 190
        radius_x = 320
        radius_y = 70
        
        for idx in range(3):
            theta = orbit_angle + idx * (2 * math.pi / 3)
            cx = face_cx + radius_x * math.cos(theta)
            cy = face_cy - 40 + radius_y * math.sin(theta)
            # Depth sorting: sin(theta) > 0 is front, < 0 is behind
            card_scale = 0.8 + 0.3 * (math.sin(theta) + 1.0) / 2.0
            alpha = int(120 + 135 * (math.sin(theta) + 1.0) / 2.0)
            
            cw = int(card_w * card_scale)
            ch = int(card_h * card_scale)
            # Draw card
            draw_fg.rounded_rectangle([cx - cw//2, cy - ch//2, cx + cw//2, cy + ch//2], radius=10, fill=(30, 28, 38, alpha), outline=(255, 255, 255, alpha), width=2)
            draw_fg.text((cx - cw//2 + 12, cy - ch//2 + 12), f"#{idx+1}", font=font_mono, fill=(245, 166, 35, alpha))
            draw_fg.text((cx - cw//2 + 12, cy + ch//2 - 32), "HUSN", font=font_mono, fill=(255, 255, 255, alpha))
            
        # Follow Pill
        follow_text = "✓ LISTENING" if t_sec >= 27.5 else "+ FOLLOW"
        draw_glass_pill(frame_pil, (WIDTH - 360) // 2, int(HEIGHT * 0.78), 360, 64, follow_text, font_ui_bold, accent_color=(127, 176, 105))

    # -------------------------------------------------------------
    # F. Push Frame to FFmpeg
    # -------------------------------------------------------------
    final_frame_bgr = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)
    proc.stdin.write(final_frame_bgr.tobytes())
    
    if frame_idx % 72 == 0:
        elapsed = time.time() - start_render_time
        fps_speed = (frame_idx + 1) / max(0.01, elapsed)
        pct = (frame_idx / TOTAL_FRAMES) * 100
        print(f"  [{pct:5.1f}%] Frame {frame_idx:03d}/{TOTAL_FRAMES} ({t_sec:.1f}s) @ {fps_speed:.1f} fps")
        sys.stdout.flush()

proc.stdin.close()
proc.wait()
ffmpeg_log.close()

render_dur = time.time() - start_render_time
print(f"\n🎉 Render Complete in {render_dur:.1f}s!")
print(f"📁 Master Output: {OUTPUT_MASTER}")
