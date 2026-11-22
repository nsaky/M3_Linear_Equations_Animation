"""
Audio compilation and mixing utility.
Combines scene voiceovers into a single full-length narration track.
"""
import os
import sys
import subprocess

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_DIR = os.path.join(PROJECT_DIR, "assets", "audio")
FFMPEG = "/opt/homebrew/bin/ffmpeg"

def combine():
    inputs = []
    filter_parts = []
    n_files = 6
    
    for i in range(1, n_files + 1):
        p = os.path.join(AUDIO_DIR, f"scene_{i:02d}.mp3")
        if not os.path.exists(p):
            print(f"Error: missing audio file {p}")
            return False
        inputs.extend(["-i", p])
        filter_parts.append(f"[{i-1}:a]")
        
    filter_complex = "".join(filter_parts) + f"concat=n={n_files}:v=0:a=1[outa]"
    out_file = os.path.join(AUDIO_DIR, "full_narration.mp3")
    
    cmd = [
        FFMPEG, "-y"
    ] + inputs + [
        "-filter_complex", filter_complex,
        "-map", "[outa]",
        "-c:a", "libmp3lame", "-qscale:a", "2",
        out_file
    ]
    subprocess.run(cmd, check=True)
    print(f"✓ Combined narration track: {out_file}")
    return out_file

if __name__ == "__main__":
    combine()
