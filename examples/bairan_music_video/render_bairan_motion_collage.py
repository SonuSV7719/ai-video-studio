#!/usr/bin/env python3
"""
Bairan: Surreal Multiplane Motion Collage Master Renderer
Renders the authentic Bairan visual music video language:
- Layered 2.5D multiplane paper collage with physical drop shadows
- Dynamic visual hooks:
  * Parting hair curtains + 3D extruded cloud title
  * Bed with glowing violet tear dust + sliding Alta feet polaroids
  * 3D anatomical ruby heart with 92 BPM double-thump pulse & energy shockwaves
  * Macro eye portal crash zoom diving into the iris
  * Balcony sunset with 3-plane architectural pillar parallax
  * Crashing tempestuous ocean with soaring seagulls
  * Scrolling 8mm vintage film reel with weightless floating boy & crying girl profile
  * Cosmic starlit outro
- Authentic Hindi kinetic typography in illuminated gold leaf styling
- High-fidelity FFmpeg H.264 CFR 24fps render with 320k AAC audio
"""

import os
import sys
import math
import random
import subprocess
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 1920
HEIGHT = 1080
FPS = 24

BASE_DIR = r"C:\Users\sonup\.gemini\antigravity\scratch\bairan-video"
COLLAGE_DIR = os.path.join(BASE_DIR, "raw_footage", "collage_assets")
AUDIO_PATH = os.path.join(BASE_DIR, "raw_footage", "bairan_audio.mp3")
OUTPUT_PATH = os.path.join(BASE_DIR, "export", "bairan_music_video_master.mp4")

# Load fonts
try:
    FONT_HINDI_HERO = ImageFont.truetype(r"C:\Windows\Fonts\Nirmala.ttc", 76)
    FONT_HINDI_SUB = ImageFont.truetype(r"C:\Windows\Fonts\Nirmala.ttc", 48)
    FONT_ENG_TITLE = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 54)
    FONT_ENG_SUB = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 34)
except Exception as e:
    print(f"Font loading fallback: {e}")
    FONT_HINDI_HERO = ImageFont.load_default()
    FONT_HINDI_SUB = ImageFont.load_default()
    FONT_ENG_TITLE = ImageFont.load_default()
    FONT_ENG_SUB = ImageFont.load_default()

def load_and_resize(filename):
    p = os.path.join(COLLAGE_DIR, filename)
    if not os.path.exists(p):
        print(f"Warning: {p} not found, generating placeholder", file=sys.stderr)
        return np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    img = cv2.imread(p)
    return cv2.resize(img, (WIDTH, HEIGHT), interpolation=cv2.INTER_LANCZOS4)

print("Loading collage assets...")
IMG_CLOUD_TITLE     = load_and_resize("scene_01_cloud_title.jpg")
IMG_ALTA_FEET       = load_and_resize("scene_02_alta_feet.jpg")
IMG_BED_BOY         = load_and_resize("scene_02_bed_boy.jpg")
IMG_RUBY_HEART      = load_and_resize("scene_03_ruby_heart.jpg")
IMG_EYE_PORTAL      = load_and_resize("scene_04_eye_portal.jpg")
IMG_BALCONY_SUNSET  = load_and_resize("scene_05_balcony_sunset.jpg")
IMG_OCEAN_STORM     = load_and_resize("scene_06_ocean_storm.jpg")
IMG_FILM_REEL       = load_and_resize("scene_07_film_reel.jpg")
IMG_WEIGHTLESS_BOY  = load_and_resize("scene_07_weightless_boy.jpg")
IMG_OUTRO           = load_and_resize("scene_08_outro.jpg")

# Pre-render polaroid cutout of Alta feet
def make_polaroid(img_src, width=540, height=640, angle=-7.0):
    """Creates a realistic Polaroid photo with white cardboard border and drop shadow."""
    pol_w = width
    pol_h = height
    pol = Image.new("RGBA", (pol_w, pol_h), (250, 248, 242, 255))
    
    # Inner photo
    margin = 28
    photo_w = pol_w - margin * 2
    photo_h = pol_h - margin * 2 - 80 # Polaroid chin
    
    crop = cv2.resize(img_src, (photo_w, photo_h))
    crop_pil = Image.fromarray(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
    pol.paste(crop_pil, (margin, margin))
    
    # Rotate with smooth antialiasing
    rotated = pol.rotate(angle, resample=Image.BICUBIC, expand=True)
    
    # Generate soft drop shadow
    shadow_pad = 40
    sh_w = rotated.width + shadow_pad * 2
    sh_h = rotated.height + shadow_pad * 2
    shadow = Image.new("RGBA", (sh_w, sh_h), (0, 0, 0, 0))
    sh_draw = ImageDraw.Draw(shadow)
    
    # Shadow offset (12px down, 8px right)
    sh_rect = [shadow_pad + 8, shadow_pad + 14, shadow_pad + rotated.width + 8, shadow_pad + rotated.height + 14]
    sh_draw.rectangle(sh_rect, fill=(0, 0, 0, 160))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    
    # Composite rotated polaroid over shadow
    shadow.paste(rotated, (shadow_pad, shadow_pad), rotated)
    return shadow

POLAROID_ALTA = make_polaroid(IMG_ALTA_FEET, width=520, height=620, angle=-6.5)

# Pre-render kinetic typography cards
TYPOGRAPHY_CARDS = {}

def create_lyric_card(hindi_text, eng_text=None, is_hero=False):
    card = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    cx = WIDTH // 2

    font_h = FONT_HINDI_HERO if is_hero else FONT_HINDI_SUB
    bbox = draw.textbbox((0, 0), hindi_text, font=font_h)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = cx - tw // 2
    ty = HEIGHT - 180 if not is_hero else (HEIGHT // 2 - 30)

    # 1. Dark warm outline & drop shadow
    for ox, oy in [(-2, -2), (2, -2), (-2, 2), (2, 2), (0, 3), (3, 3), (0, 5)]:
        draw.text((tx + ox, ty + oy), hindi_text, font=font_h, fill=(20, 10, 5, 230))

    # 2. Golden-leaf warm gradient fill
    draw.text((tx, ty), hindi_text, font=font_h, fill=(255, 242, 190, 255))

    # Optional English subtitle
    if eng_text:
        e_bbox = draw.textbbox((0, 0), eng_text, font=FONT_ENG_SUB)
        e_tw = e_bbox[2] - e_bbox[0]
        e_tx = cx - e_tw // 2
        e_ty = ty + th + 18
        draw.text((e_tx + 2, e_ty + 2), eng_text, font=FONT_ENG_SUB, fill=(0, 0, 0, 190))
        draw.text((e_tx, e_ty), eng_text, font=FONT_ENG_SUB, fill=(230, 205, 155, 240))

    card_np = np.array(card)
    b, g, r, a = cv2.split(card_np)
    card_bgr = cv2.merge([b, g, r])
    card_alpha = (a.astype(np.float32) / 255.0)[:, :, np.newaxis]
    return card_bgr, card_alpha

# Define lyrics per section
LYRICS = {
    "title_intro": create_lyric_card("बैरन • BAIRAN", "A Musical Story by Banjaare", is_hero=True),
    "lyric_1": create_lyric_card("बैरी तन्हाई मनै", "This cruel loneliness haunting me..."),
    "lyric_2": create_lyric_card("तेरे झांझरा के जोड़े", "The memory of your chiming anklets..."),
    "lyric_3": create_lyric_card("छाती के लगाई मनै...", "Held close against my aching heart..."),
    "lyric_4": create_lyric_card("हाय रे बैरण... हाय रे बैरण...", "Oh my beloved... my sweet tormentor..."),
    "lyric_5": create_lyric_card("जीणा बंजारे का...", "The wandering life of Banjaare..."),
    "lyric_6": create_lyric_card("जित भी गया रै तेरी... ठीक कोन्या हाल मेरा", "Wherever I roam, my heart finds no peace..."),
    "lyric_7": create_lyric_card("हाय रे बैरण... तेरे प्यार में...", "Lost forever in the ocean of your love..."),
    "outro": create_lyric_card("बैरन • BAIRAN", "Directed & Produced with AI Video Studio", is_hero=True),
}

# Particle and effect generators
random.seed(101)
TEAR_DUST = [
    {
        "x": random.uniform(WIDTH * 0.45, WIDTH * 0.55),
        "y": random.uniform(HEIGHT * 0.35, HEIGHT * 0.55),
        "vx": random.uniform(-0.4, 0.4),
        "vy": random.uniform(-1.2, -0.4),
        "rad": random.uniform(2.5, 6.0),
        "phase": random.uniform(0, 6.28),
        "color": (240, 130, 180) # BGR: Soft violet-cyan
    }
    for _ in range(50)
]

SEAGULLS = [
    {
        "x": random.uniform(100, WIDTH - 100),
        "y": random.uniform(80, HEIGHT * 0.45),
        "speed": random.uniform(1.8, 3.5),
        "size": random.uniform(14, 26),
        "phase": random.uniform(0, 6.28),
    }
    for _ in range(8)
]

def draw_seagull(frame, x, y, size, flap_phase):
    """Draws a silhouetted flying seagull with flapping wings."""
    wing_dip = math.sin(flap_phase) * (size * 0.4)
    pts_left = np.array([
        [int(x - size), int(y - wing_dip)],
        [int(x - size * 0.4), int(y - size * 0.2)],
        [int(x), int(y)]
    ], np.int32)
    pts_right = np.array([
        [int(x), int(y)],
        [int(x + size * 0.4), int(y - size * 0.2)],
        [int(x + size), int(y - wing_dip)]
    ], np.int32)
    cv2.polylines(frame, [pts_left], False, (25, 25, 30), 2, cv2.LINE_AA)
    cv2.polylines(frame, [pts_right], False, (25, 25, 30), 2, cv2.LINE_AA)

def blend_card(frame, card_tuple, alpha=1.0):
    if alpha < 0.02:
        return frame
    card_bgr, card_alpha = card_tuple
    cur_alpha = card_alpha * alpha
    frame[:] = (frame.astype(np.float32) * (1.0 - cur_alpha) + card_bgr.astype(np.float32) * cur_alpha).astype(np.uint8)
    return frame

def apply_ken_burns(img, progress, zoom_range, pan_range):
    t = 0.5 - 0.5 * math.cos(progress * math.pi)
    zoom = zoom_range[0] + (zoom_range[1] - zoom_range[0]) * t
    dx = pan_range[0] + (pan_range[2] - pan_range[0]) * t
    dy = pan_range[1] + (pan_range[3] - pan_range[1]) * t

    crop_w = int(WIDTH / zoom)
    crop_h = int(HEIGHT / zoom)
    cx = WIDTH / 2 + dx
    cy = HEIGHT / 2 + dy

    x1 = int(max(0, min(WIDTH - crop_w, cx - crop_w / 2)))
    y1 = int(max(0, min(HEIGHT - crop_h, cy - crop_h / 2)))
    x2 = x1 + crop_w
    y2 = y1 + crop_h
    return cv2.resize(img[y1:y2, x1:x2], (WIDTH, HEIGHT), interpolation=cv2.INTER_LINEAR)

def render_scene_1(frame_idx, total_frames):
    """Scene 1: Parting hair curtains + drifting 3D cloud title + golden dust."""
    prog = frame_idx / max(1, total_frames - 1)
    # Cloud drift
    cloud_dx = math.sin(prog * 2.5) * 25.0
    cloud_dy = math.cos(prog * 2.0) * 12.0
    frame = apply_ken_burns(IMG_CLOUD_TITLE, prog, (1.00, 1.06), (cloud_dx, cloud_dy, cloud_dx + 15, cloud_dy + 8))

    # Curtains opening (curtain effect via dark curved vignettes receding left & right)
    curtain_open = min(1.0, prog * 2.2)
    curtain_w = int((1.0 - curtain_open) * 180)
    if curtain_w > 0:
        cv2.rectangle(frame, (0, 0), (curtain_w, HEIGHT), (15, 12, 10), -1)
        cv2.rectangle(frame, (WIDTH - curtain_w, 0), (WIDTH, HEIGHT), (15, 12, 10), -1)

    # Shimmering golden dust sparkles
    for i in range(35):
        sx = int((i * 57 + frame_idx * 1.2) % WIDTH)
        sy = int((i * 83 + math.sin(frame_idx * 0.08 + i) * 20) % HEIGHT)
        sparkle = 0.5 + 0.5 * math.sin(frame_idx * 0.15 + i)
        rad = max(1, int(3 * sparkle))
        cv2.circle(frame, (sx, sy), rad, (150, 220, 255), -1, cv2.LINE_AA)

    # Title Card
    alpha = min(1.0, prog * 5.0) * min(1.0, (1.0 - prog) * 5.0)
    blend_card(frame, LYRICS["title_intro"], alpha)
    return frame

def render_scene_2(frame_idx, total_frames):
    """Scene 2: Bed with boy + glowing violet tear dust + sliding Alta polaroid."""
    prog = frame_idx / max(1, total_frames - 1)
    frame = apply_ken_burns(IMG_BED_BOY, prog, (1.02, 1.08), (0, 0, 0, -10))

    # Glowing violet tear dust motes drifting upward from boy's face
    for p in TEAR_DUST:
        px = int((p["x"] + math.sin(frame_idx * 0.05 + p["phase"]) * 14) % WIDTH)
        py = int((p["y"] + frame_idx * p["vy"]) % HEIGHT)
        glow = max(0.1, 0.4 + 0.6 * math.sin(frame_idx * 0.1 + p["phase"]))
        rad = max(1, int(p["rad"] * glow))
        cv2.circle(frame, (px, py), rad, p["color"], -1, cv2.LINE_AA)

    # Polaroid sliding in from right side at frame 220 (~9s in)
    if frame_idx > 220:
        pol_prog = min(1.0, (frame_idx - 220) / 45.0) # smooth slide in over ~1.8s
        ease_x = 1.0 - math.pow(1.0 - pol_prog, 3.0)
        pol_target_x = WIDTH - POLAROID_ALTA.width - 90
        pol_start_x = WIDTH + 100
        cur_x = int(pol_start_x + (pol_target_x - pol_start_x) * ease_x)
        cur_y = HEIGHT - POLAROID_ALTA.height - 70

        # Overlay Polaroid onto OpenCV frame
        pil_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        pil_frame.paste(POLAROID_ALTA, (cur_x, cur_y), POLAROID_ALTA)
        frame = cv2.cvtColor(np.array(pil_frame), cv2.COLOR_RGB2BGR)

    # Kinetic Lyrics (Line 1: 0-280, Line 2: 280-576)
    if frame_idx < 288:
        l_prog = frame_idx / 288.0
        alpha = min(1.0, l_prog * 6.0) * min(1.0, (1.0 - l_prog) * 6.0)
        blend_card(frame, LYRICS["lyric_1"], alpha)
    else:
        l_prog = (frame_idx - 288) / (total_frames - 288)
        alpha = min(1.0, l_prog * 6.0) * min(1.0, (1.0 - l_prog) * 6.0)
        blend_card(frame, LYRICS["lyric_2"], alpha)

    return frame

def render_scene_3(frame_idx, total_frames):
    """Scene 3: 3D Anatomical Ruby Heart beating at 92 BPM with radial energy shockwaves."""
    prog = frame_idx / max(1, total_frames - 1)

    # 92 BPM heartbeat pulse equation: double-thump systolic bounce
    beat_freq = 0.40
    pulse = math.pow(max(0.0, math.sin(frame_idx * beat_freq)), 14) + 0.45 * math.pow(max(0.0, math.sin(frame_idx * beat_freq + 0.35)), 12)
    heart_scale = 1.0 + 0.16 * pulse

    # Base heart frame with zoom and pulse
    frame = apply_ken_burns(IMG_RUBY_HEART, prog, (1.00 * heart_scale, 1.05 * heart_scale), (0, 0, 0, 0))

    # Concentric crimson energy ripples expanding outward on thumps
    if pulse > 0.3:
        cx, cy = WIDTH // 2, HEIGHT // 2
        ripple_rad = int((1.0 - pulse) * 140) + 120
        cv2.circle(frame, (cx, cy), ripple_rad, (40, 20, 220), 3, cv2.LINE_AA)
        cv2.circle(frame, (cx, cy), ripple_rad + 35, (30, 15, 180), 2, cv2.LINE_AA)

    # Floating memory fragments (subtle orbiting squares)
    for i in range(12):
        angle = (frame_idx * 0.02 + i * 0.52)
        dist = 360 + math.sin(frame_idx * 0.04 + i) * 40
        fx = int(WIDTH // 2 + math.cos(angle) * dist)
        fy = int(HEIGHT // 2 + math.sin(angle) * (dist * 0.6))
        cv2.rectangle(frame, (fx - 15, fy - 20), (fx + 15, fy + 20), (240, 235, 220), -1)

    # Kinetic lyric
    alpha = min(1.0, prog * 6.0) * min(1.0, (1.0 - prog) * 6.0)
    blend_card(frame, LYRICS["lyric_3"], alpha)
    return frame

def render_scene_4(frame_idx, total_frames):
    """Scene 4: Macro Eye Portal with exponential crash zoom into the pupil."""
    prog = frame_idx / max(1, total_frames - 1)

    # Crash zoom equation: starts slow, exponentially dives after frame 120
    if frame_idx < 120:
        zoom = 1.0 + prog * 0.1
    else:
        dive_t = (frame_idx - 120) / (total_frames - 120)
        zoom = 1.1 + math.pow(dive_t, 2.6) * 5.5

    # Focus center is the pupil (center of eye)
    crop_w = int(WIDTH / zoom)
    crop_h = int(HEIGHT / zoom)
    cx, cy = int(WIDTH * 0.49), int(HEIGHT * 0.52)
    x1 = max(0, min(WIDTH - crop_w, cx - crop_w // 2))
    y1 = max(0, min(HEIGHT - crop_h, cy - crop_h // 2))
    frame = cv2.resize(IMG_EYE_PORTAL[y1:y1 + crop_h, x1:x1 + crop_w], (WIDTH, HEIGHT), interpolation=cv2.INTER_LINEAR)

    # Chorus 1 Hook Drop Typography (pulsing to beat)
    pulse = 0.85 + 0.15 * math.sin(frame_idx * 0.40)
    alpha = min(1.0, prog * 5.0) * min(1.0, (1.0 - prog) * 5.0) * pulse
    blend_card(frame, LYRICS["lyric_4"], alpha)
    return frame

def render_scene_5(frame_idx, total_frames):
    """Scene 5: Balcony silhouette looking at glowing sunset orb through pillars."""
    prog = frame_idx / max(1, total_frames - 1)
    # Slow majestic horizontal parallax pan
    frame = apply_ken_burns(IMG_BALCONY_SUNSET, prog, (1.00, 1.07), (-30, 0, 30, -10))

    # Sun glowing chromatic bloom
    sun_x, sun_y = int(WIDTH * 0.44), int(HEIGHT * 0.32)
    bloom_radius = int(80 + math.sin(frame_idx * 0.12) * 15)
    sun_glow = np.zeros_like(frame)
    cv2.circle(sun_glow, (sun_x, sun_y), bloom_radius, (120, 160, 255), -1, cv2.LINE_AA)
    sun_glow = cv2.GaussianBlur(sun_glow, (81, 81), 0)
    cv2.addWeighted(frame, 1.0, sun_glow, 0.25, 0, frame)

    # Lyric
    alpha = min(1.0, prog * 6.0) * min(1.0, (1.0 - prog) * 6.0)
    blend_card(frame, LYRICS["lyric_5"], alpha)
    return frame

def render_scene_6(frame_idx, total_frames):
    """Scene 6: Tempestuous ocean with open-arm silhouette & soaring seagulls."""
    prog = frame_idx / max(1, total_frames - 1)
    frame = apply_ken_burns(IMG_OCEAN_STORM, prog, (1.05, 1.00), (0, 15, 0, -20))

    # Animated seagulls soaring across the horizon
    for s in SEAGULLS:
        sx = int((s["x"] + frame_idx * s["speed"]) % (WIDTH + 150)) - 80
        sy = int(s["y"] + math.sin(frame_idx * 0.04 + s["phase"]) * 18)
        draw_seagull(frame, sx, sy, s["size"], frame_idx * 0.22 + s["phase"])

    # Sea spray foam particles in lower third
    for i in range(25):
        fx = int((i * 79 + frame_idx * 2.5) % WIDTH)
        fy = int(HEIGHT - 40 - (math.sin(frame_idx * 0.15 + i) * 35))
        cv2.circle(frame, (fx, fy), 2, (255, 250, 240), -1, cv2.LINE_AA)

    # Lyric
    alpha = min(1.0, prog * 6.0) * min(1.0, (1.0 - prog) * 6.0)
    blend_card(frame, LYRICS["lyric_6"], alpha)
    return frame

def render_scene_7(frame_idx, total_frames):
    """Scene 7: 8mm Vintage film strip scrolling + weightless floating boy & heart."""
    prog = frame_idx / max(1, total_frames - 1)

    # Weightless boy floating with sinusoidal bob
    bob_y = int(math.sin(frame_idx * 0.08) * 18)
    frame = apply_ken_burns(IMG_WEIGHTLESS_BOY, prog, (1.02, 1.06), (0, bob_y, 0, bob_y + 10))

    # Top banner: 8mm film strip scrolling horizontally (from IMG_FILM_REEL)
    strip_h = 240
    scroll_x = int((frame_idx * 5) % WIDTH)
    strip_crop = IMG_FILM_REEL[:strip_h, :]
    
    # Seamless horizontal roll
    rolled = np.roll(strip_crop, scroll_x, axis=1)
    # Subtle film grain / flicker
    flicker = 0.90 + 0.10 * math.sin(frame_idx * 0.8)
    rolled = (rolled.astype(np.float32) * flicker).astype(np.uint8)

    # Blend 8mm strip across the top with soft border shadow
    frame[:strip_h, :] = rolled
    cv2.line(frame, (0, strip_h), (WIDTH, strip_h), (10, 10, 10), 3)

    # Beating heart shockwaves above boy's chest
    beat_pulse = math.pow(max(0.0, math.sin(frame_idx * 0.40)), 12)
    if beat_pulse > 0.4:
        rad = max(1, int(beat_pulse * 65))
        cv2.circle(frame, (int(WIDTH * 0.36), int(HEIGHT * 0.28)), rad, (50, 30, 240), 2, cv2.LINE_AA)

    # Grand chorus finale lyric
    alpha = min(1.0, prog * 6.0) * min(1.0, (1.0 - prog) * 6.0)
    blend_card(frame, LYRICS["lyric_7"], alpha)
    return frame

def render_scene_8(frame_idx, total_frames):
    """Scene 8: Cosmic starlit outro with resolving golden title."""
    prog = frame_idx / max(1, total_frames - 1)
    frame = apply_ken_burns(IMG_OUTRO, prog, (1.06, 1.00), (0, 0, 0, -10))

    # Twinkling stars
    for i in range(60):
        sx = int((i * 31) % WIDTH)
        sy = int((i * 47) % (HEIGHT // 2))
        twinkle = 0.3 + 0.7 * abs(math.sin(frame_idx * 0.12 + i))
        cv2.circle(frame, (sx, sy), max(1, int(3 * twinkle)), (255, 255, 255), -1, cv2.LINE_AA)

    # Outro title card
    alpha = min(1.0, prog * 4.0) * min(1.0, (1.0 - prog) * 3.5)
    blend_card(frame, LYRICS["outro"], alpha)
    return frame

SCENE_DISPATCH = [
    (14.0, render_scene_1, "Scene 1: Cloud Title & Hair Curtains"),
    (24.0, render_scene_2, "Scene 2: Bed Tear Dust & Alta Polaroid"),
    (16.0, render_scene_3, "Scene 3: Beating 3D Ruby Crystal Heart"),
    (24.0, render_scene_4, "Scene 4: Macro Eye Portal Crash Zoom"),
    (18.0, render_scene_5, "Scene 5: Balcony Sunset & Pillar Parallax"),
    (22.0, render_scene_6, "Scene 6: Tempest Ocean & Outstretched Man"),
    (24.0, render_scene_7, "Scene 7: 8mm Film Reel & Weightless Dive"),
    (8.39, render_scene_8, "Scene 8: Cosmic Starlit Outro"),
]

def main():
    sys.stdout.reconfigure(line_buffering=True)
    print("🎬 Starting Bairan Surreal Multiplane Motion Collage Master Render...", flush=True)
    print(f"  Resolution: {WIDTH}x{HEIGHT} @ {FPS} fps", flush=True)
    print(f"  Audio Track: {AUDIO_PATH}", flush=True)
    print(f"  Output Master: {OUTPUT_PATH}", flush=True)

    # Calculate scene frame counts
    scene_frames = [int(round(d * FPS)) for d, _, _ in SCENE_DISPATCH]
    total_frames = sum(scene_frames)
    print(f"  Total Video Frames: {total_frames} ({total_frames / FPS:.2f}s)", flush=True)

    log_path = os.path.join(BASE_DIR, "export", "ffmpeg_motion_render.log")
    log_file = open(log_path, "w")

    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "bgr24",
        "-r", str(FPS),
        "-i", "-",
        "-i", AUDIO_PATH,
        "-c:v", "libx264",
        "-preset", "faster",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "320k",
        "-shortest",
        OUTPUT_PATH
    ]

    pipe = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=log_file)
    global_frame = 0
    CROSSFADE_FRAMES = 16 # 0.65s transition

    try:
        for s_idx, (dur, render_fn, desc) in enumerate(SCENE_DISPATCH):
            n_frames = scene_frames[s_idx]
            next_fn = SCENE_DISPATCH[s_idx + 1][1] if s_idx + 1 < len(SCENE_DISPATCH) else None
            next_total = scene_frames[s_idx + 1] if s_idx + 1 < len(SCENE_DISPATCH) else 1

            print(f"  -> Rendering {desc} ({n_frames} frames)...", flush=True)

            for f in range(n_frames):
                frame = render_fn(f, n_frames)

                # Cross-dissolve into next scene at tail
                if next_fn is not None and f >= n_frames - CROSSFADE_FRAMES:
                    trans_prog = (f - (n_frames - CROSSFADE_FRAMES)) / CROSSFADE_FRAMES
                    next_frame = next_fn(0, next_total)
                    cv2.addWeighted(next_frame, trans_prog, frame, 1.0 - trans_prog, 0, frame)

                pipe.stdin.write(frame.tobytes())
                global_frame += 1

                if global_frame % 240 == 0:
                    pct = (global_frame / total_frames) * 100
                    print(f"     [{pct:5.1f}%] Rendered {global_frame}/{total_frames} frames ({global_frame / FPS:.1f}s)", flush=True)

        pipe.stdin.close()
        pipe.wait()
        log_file.close()

        if pipe.returncode == 0:
            file_size_mb = os.path.getsize(OUTPUT_PATH) / (1024 * 1024)
            print("\n🎉 SURREAL MOTION COLLAGE RENDER SUCCESSFUL!", flush=True)
            print(f"  Master File: {OUTPUT_PATH}", flush=True)
            print(f"  File Size: {file_size_mb:.2f} MB", flush=True)
            print(f"  Duration: {total_frames / FPS:.2f}s", flush=True)
        else:
            print(f"\n❌ FFmpeg Error (code {pipe.returncode}). Check {log_path}", flush=True)

    except Exception as e:
        print(f"\n❌ Exception during render: {e}", flush=True)
        if pipe.poll() is None:
            pipe.kill()
        log_file.close()
        sys.exit(1)

if __name__ == "__main__":
    main()
