import subprocess
import os

source_dir = r"C:\My_Project\Iphone\Video"
output_dir = r"C:\Users\sonup\.gemini\antigravity\scratch\video-studio\reel-studio\public\aroll"
os.makedirs(output_dir, exist_ok=True)

takes = [
    {
        "id": "take1_hook",
        "file": "IMG_0050.MOV",
        "start": 0.10,
        "end": 3.40,
    },
    {
        "id": "take2_announcement",
        "file": "IMG_0054.MOV",
        "start": 0.50,
        "end": 9.60,
    },
    {
        "id": "take3_realtime",
        "file": "IMG_0058.MOV",
        "start": 0.35,
        "end": 5.50,
    },
    {
        "id": "take4_audio",
        "file": "IMG_0059.MOV",
        "start": 1.45,
        "end": 8.15,
    },
    {
        "id": "take5_continuous",
        "file": "IMG_0061.MOV",
        "start": 2.00,
        "end": 7.05,
    },
    {
        "id": "take6_specs",
        "file": "IMG_0063.MOV",
        "start": 14.05,
        "end": 22.35,
    },
    {
        "id": "take7_cta",
        "file": "IMG_0064.MOV",
        "start": 0.35,
        "end": 4.85,
    },
]

vf_filter = (
    "zscale=tin=arib-std-b67:pin=bt2020:t=linear:npl=1000:p=bt709,"
    "tonemap=tonemap=mobius:param=0.3,"
    "zscale=t=bt709:m=bt709:r=tv,"
    "format=yuv420p"
)

for t in takes:
    in_video = os.path.join(source_dir, t["file"])
    out_video = os.path.join(output_dir, f"{t['id']}.mp4")
    dur = t["end"] - t["start"]
    
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(t["start"]),
        "-t", str(dur),
        "-i", in_video,
        "-vf", vf_filter,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-r", "24",
        "-fps_mode", "cfr",
        "-g", "24",
        "-tune", "fastdecode",
        "-crf", "18",
        "-an",
        out_video
    ]
    print(f"Encoding {t['id']}.mp4 (pure camera, NO BLUR)...")
    subprocess.run(cmd, check=True)
    print(f"Done {t['id']}.mp4")

print("All pure A-roll takes successfully encoded with 0% blur!")
