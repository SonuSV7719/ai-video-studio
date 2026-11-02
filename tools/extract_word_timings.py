import json
import os

files = [
    ("take1_hook", "IMG_0050.json", 0.10),
    ("take2_announcement", "IMG_0054.json", 0.50),
    ("take3_realtime", "IMG_0058.json", 0.35),
    ("take4_audio", "IMG_0059.json", 1.45),
    ("take5_continuous", "IMG_0061.json", 2.00),
    ("take6_specs", "IMG_0063.json", 14.05),
    ("take7_cta", "IMG_0064.json", 0.35),
]

transcripts_dir = r"C:\Users\sonup\.gemini\antigravity\scratch\video-studio\tools\transcripts"

for take_id, json_file, offset in files:
    path = os.path.join(transcripts_dir, json_file)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\n--- {take_id} (offset -{offset:.2f}s) ---")
    for seg in data.get("transcription", []):
        t_from = seg["offsets"]["from"] / 1000.0 - offset
        t_to = seg["offsets"]["to"] / 1000.0 - offset
        if t_to > 0:
            print(f"[{max(0, t_from):.2f}s -> {t_to:.2f}s]: {seg['text'].strip()}")
