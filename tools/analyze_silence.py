import wave
import numpy as np
import os

def analyze_audio(filename, start_s, end_s):
    path = os.path.join(r"C:\Users\sonup\.gemini\antigravity\scratch\video-studio\tools\transcripts", filename)
    with wave.open(path, 'rb') as wf:
        sr = wf.getframerate()
        n_frames = wf.getnframes()
        data = wf.readframes(n_frames)
        samples = np.frombuffer(data, dtype=np.int16)
        duration = len(samples) / sr
        
        # Calculate RMS energy in 50ms windows
        window_size = int(sr * 0.05)
        n_windows = len(samples) // window_size
        energies = []
        for i in range(n_windows):
            chunk = samples[i*window_size : (i+1)*window_size]
            rms = np.sqrt(np.mean(chunk.astype(np.float64)**2))
            t = (i * window_size) / sr
            energies.append((t, rms))
            
        print(f"=== {filename} (Total duration: {duration:.2f}s) ===")
        # Find when voice actually starts (threshold ~ 500)
        voice_start = 0.0
        for t, e in energies:
            if t >= start_s and e > 800:
                voice_start = t
                break
                
        # Find voice end
        voice_end = duration
        for t, e in reversed(energies):
            if t <= end_s and e > 800:
                voice_end = t + 0.1
                break
                
        print(f"Suggested clean trim: {max(0, voice_start - 0.15):.2f}s to {min(duration, voice_end + 0.25):.2f}s")

analyze_audio("IMG_0054.wav", 0.0, 10.0)
analyze_audio("IMG_0055.wav", 0.0, 9.0)
analyze_audio("IMG_0058.wav", 0.0, 6.0)
analyze_audio("IMG_0059.wav", 0.0, 8.5)
analyze_audio("IMG_0061.wav", 1.5, 7.5)
analyze_audio("IMG_0063.wav", 14.0, 23.0)
analyze_audio("IMG_0064.wav", 0.0, 5.5)
