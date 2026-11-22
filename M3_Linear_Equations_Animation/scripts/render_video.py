"""
Master Render & Assembly Pipeline
Renders all 6 scenes in 1080p 30fps, synchronizes with narration, and exports output/final_video.mp4.
"""
import os
import sys
import glob
import subprocess

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCENES_DIR = os.path.join(PROJECT_DIR, "scenes")
AUDIO_DIR = os.path.join(PROJECT_DIR, "assets", "audio")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "output")
INTERMEDIATE_DIR = os.path.join(OUTPUT_DIR, "intermediate_scenes")
MEDIA_DIR = os.path.join(OUTPUT_DIR, "manim_media")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(INTERMEDIATE_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)

# Add Homebrew & TinyTeX to PATH
TINYTEX_BIN = "/Users/yasireqbal/Library/TinyTeX/bin/universal-darwin"
HOMEBREW_BIN = "/opt/homebrew/bin"
os.environ["PATH"] = f"{TINYTEX_BIN}:{HOMEBREW_BIN}:{os.environ.get('PATH', '')}"

FFMPEG = "/opt/homebrew/bin/ffmpeg"
FFPROBE = "/opt/homebrew/bin/ffprobe"

SCENE_SPECS = [
    (1, "scene_01_intro.py", "Scene01Intro"),
    (2, "scene_02_concept.py", "Scene02Concept"),
    (3, "scene_03_matrix_construction.py", "Scene03MatrixConstruction"),
    (4, "scene_04_worked_example.py", "Scene04WorkedExample"),
    (5, "scene_05_solution_sets.py", "Scene05SolutionSets"),
    (6, "scene_06_summary.py", "Scene06Summary"),
]

def get_duration(media_path):
    cmd = [
        FFPROBE, "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", media_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return float(res.stdout.strip())

def render_scene(num, script_file, class_name):
    script_path = os.path.join(SCENES_DIR, script_file)
    print(f"\n==========================================")
    print(f"Rendering Scene {num}: {class_name} (1080p 30fps)...")
    print(f"==========================================")
    
    cmd = [
        sys.executable, "-m", "manim",
        "-qh", "--fps", "30", "-r", "1920,1080",
        "--media_dir", MEDIA_DIR,
        script_path, class_name
    ]
    subprocess.run(cmd, check=True)
    
    # Locate output file inside MEDIA_DIR
    pattern = os.path.join(MEDIA_DIR, "videos", "**", f"{class_name}.mp4")
    matches = glob.glob(pattern, recursive=True)
    if not matches:
        # Also check root media dir if any
        matches = glob.glob(os.path.join(PROJECT_DIR, "**", f"{class_name}.mp4"), recursive=True)
    if not matches:
        raise FileNotFoundError(f"Could not locate rendered MP4 for {class_name}")
    
    # Pick the largest or newest file
    raw_video = max(matches, key=os.path.getmtime)
    raw_dur = get_duration(raw_video)
    print(f"  ✓ Rendered raw video: {raw_video} ({raw_dur:.2f}s)")
    
    # Mux with narration audio
    audio_file = os.path.join(AUDIO_DIR, f"scene_{num:02d}.mp3")
    synced_output = os.path.join(INTERMEDIATE_DIR, f"scene_{num:02d}_synced.mp4")
    
    if os.path.exists(audio_file):
        audio_dur = get_duration(audio_file)
        print(f"  Muxing with audio: {audio_file} ({audio_dur:.2f}s)")
        # Hold last video frame if audio is longer, else truncate
        if audio_dur > raw_dur:
            pad_dur = audio_dur - raw_dur + 0.3
            filter_str = f"[0:v]tpad=stop_mode=clone:stop_duration={pad_dur:.2f}[v]"
            mux_cmd = [
                FFMPEG, "-y",
                "-i", raw_video,
                "-i", audio_file,
                "-filter_complex", filter_str,
                "-map", "[v]", "-map", "1:a",
                "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k",
                "-shortest",
                synced_output
            ]
        else:
            mux_cmd = [
                FFMPEG, "-y",
                "-i", raw_video,
                "-i", audio_file,
                "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k",
                "-shortest",
                synced_output
            ]
        subprocess.run(mux_cmd, check=True)
    else:
        print(f"  ! Audio file missing for scene {num}, copying video without audio")
        subprocess.run([FFMPEG, "-y", "-i", raw_video, "-c", "copy", synced_output], check=True)
        
    final_dur = get_duration(synced_output)
    print(f"  ✓ Final synchronized Scene {num}: {synced_output} ({final_dur:.2f}s)")
    return synced_output

def concatenate_scenes(scene_files):
    print(f"\n==========================================")
    print(f"Concatenating all {len(scene_files)} scenes into final_video.mp4...")
    print(f"==========================================")
    
    concat_list = os.path.join(INTERMEDIATE_DIR, "concat_list.txt")
    with open(concat_list, "w") as f:
        for p in scene_files:
            f.write(f"file '{os.path.abspath(p)}'\n")
            
    final_mp4 = os.path.join(OUTPUT_DIR, "final_video.mp4")
    
    cmd = [
        FFMPEG, "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list,
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        final_mp4
    ]
    subprocess.run(cmd, check=True)
    
    total_dur = get_duration(final_mp4)
    print(f"\n🎉 FINAL VIDEO EXPORTED: {final_mp4}")
    print(f"   Total Duration: {total_dur:.2f} seconds ({total_dur/60:.2f} minutes)")
    return final_mp4

def main():
    synced_scenes = []
    for num, script, cls in SCENE_SPECS:
        out_mp4 = render_scene(num, script, cls)
        synced_scenes.append(out_mp4)
        
    final_video = concatenate_scenes(synced_scenes)
    
    # Run validation
    val_script = os.path.join(PROJECT_DIR, "scripts", "validate_video.py")
    if os.path.exists(val_script):
        subprocess.run([sys.executable, val_script], check=True)

if __name__ == "__main__":
    main()
