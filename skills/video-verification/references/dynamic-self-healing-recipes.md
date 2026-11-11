# Dynamic Self-Healing Recipes (On-Demand Code Generation)

When a defect is detected during the self-verification loop, generate the appropriate tailored fix code on the fly without using hardcoded, static templates.

---

## 1. Remedying Audio Loudness & True Peak Without Video Re-Render

If the video stream is perfect but audio is slightly clipping (e.g. `True Peak > -0.5 dBFS`) or too quiet:

```python
import subprocess

def fix_audio_stream(input_mp4, output_mp4, target_lufs=-14.0, true_peak=-1.0):
    """Lossless video copy while applying dynamic leveling and peak limiting to audio."""
    cmd = (
        f'ffmpeg -y -i "{input_mp4}" -c:v copy '
        f'-af "dynaudnorm=f=150:g=15:p=0.95:m=10.0,alimiter=limit={true_peak}dB:level=false" '
        f'-c:a aac -b:a 192k "{output_mp4}"'
    )
    subprocess.run(cmd, shell=True, check=True)
    print(f"✓ Remediated audio track to {target_lufs} LUFS ceiling {true_peak} dBFS without re-rendering video.")
```

---

## 2. Remedying MediaPipe Mask Fringe / Edge Halo Bleed

If typography behind the head bleeds slightly onto hair or shoulders due to tight segmentation:

```python
import cv2
import numpy as np

def refine_cutout_mask(raw_mask, expand_pixels=8, blur_kernel=15):
    """Dilates and feathers the segmentation mask to create a seamless natural edge."""
    # 1. Threshold confidence
    binary = (raw_mask > 0.45).astype(np.uint8)
    
    # 2. Dilate slightly to cover flyaway hair edges
    if expand_pixels > 0:
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (expand_pixels, expand_pixels))
        binary = cv2.dilate(binary, kernel, iterations=1)
        
    # 3. Feather edges with Gaussian blur for zero-halo optical blending
    feathered = cv2.GaussianBlur(binary.astype(np.float32), (blur_kernel, blur_kernel), 0)
    return feathered
```

---

## 3. Remedying Safe Margin Collisions

If an extracted frame reveals that a subtitle pill or widget is positioned at `Y = 1650px` (inside the bottom danger zone for Instagram/Shorts):

```python
# Calculate safe Y offset dynamically
def compute_safe_y(card_height, canvas_height, margin_bottom=370):
    max_safe_y = canvas_height - margin_bottom - card_height
    return max_safe_y

# In render code: replace Y coordinate with computed safe Y
safe_y = compute_safe_y(card_h, 1920, margin_bottom=380)
```

---

## 4. Remedying Remotion Sequence Double-Offset Freezing

If a frame diff check reveals that the last 15 frames of a video clip are completely identical:
- **Root Cause**: An `<OffthreadVideo startFrom={T} />` was nested inside `<Sequence from={T}>`, causing double-offset seeking.
- **Fix Code**: Edit the Remotion TSX component to remove `startFrom={T}` on child video elements inside sequences.
