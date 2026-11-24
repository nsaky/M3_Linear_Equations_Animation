"""
Master Render & Assembly Pipeline for Version 2 (v2)
Renders all 6 scenes in 1080p 30fps, synchronizes with beat-calibrated audio,
and exports output/final_video_v2.mp4 without touching v1.
"""
import os
import sys
import glob
import subprocess

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCENES_V2_DIR = os.path.join(PROJECT_DIR, "scenes_v2")
AUDIO_V2_DIR = os.path.join(PROJECT_DIR, "assets", "audio_v2")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "output")
INTERMEDIATE_DIR = os.path.join(OUTPUT_DIR, "intermediate_scenes_v2")
MEDIA_DIR = os.path.join(OUTPUT_DIR, "manim_media_v2")

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
    (1, "scene_01_intro_v2.py", "Scene01IntroV2"),
    (2, "scene_02_concept_v2.py", "Scene02ConceptV2"),
    (3, "scene_03_matrix_construction_v2.py", "Scene03MatrixConstructionV2"),
    (4, "scene_04_worked_example_v2.py", "Scene04WorkedExampleV2"),
    (5, "scene_05_solution_sets_v2.py", "Scene05SolutionSetsV2"),
    (6, "scene_06_summary_v2.py", "Scene06SummaryV2"),
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
    synced_output = os.path.join(INTERMEDIATE_DIR, f"scene_{num:02d}_synced_v2.mp4")
    if os.path.exists(synced_output) and os.path.getsize(synced_output) > 1000 and "--force" not in sys.argv:
        print(f"\n==========================================")
        print(f"Skipping v2 Scene {num}: {class_name} (already rendered & synced)")
        print(f"  ✓ {synced_output} ({get_duration(synced_output):.2f}s)")
        print(f"==========================================")
        return synced_output

    script_path = os.path.join(SCENES_V2_DIR, script_file)
    print(f"\n==========================================")
    print(f"Rendering v2 Scene {num}: {class_name} (1080p 30fps)...")
    print(f"==========================================")
    
    cmd = [
        sys.executable, "-m", "manim",
        "-qh", "--fps", "30", "-r", "1920,1080",
        "--media_dir", MEDIA_DIR,
        script_path, class_name
    ]
    subprocess.run(cmd, check=True)
    
    # Locate output file
    pattern = os.path.join(MEDIA_DIR, "videos", "**", f"{class_name}.mp4")
    matches = glob.glob(pattern, recursive=True)
    if not matches:
        raise FileNotFoundError(f"Could not locate rendered MP4 for {class_name}")
    
    raw_video = max(matches, key=os.path.getmtime)
    raw_dur = get_duration(raw_video)
    print(f"  ✓ Rendered raw video: {raw_video} ({raw_dur:.2f}s)")
    
    # Mux with narration audio
    audio_file = os.path.join(AUDIO_V2_DIR, f"scene_{num:02d}_v2.mp3")
    synced_output = os.path.join(INTERMEDIATE_DIR, f"scene_{num:02d}_synced_v2.mp4")
    
    if os.path.exists(audio_file):
        audio_dur = get_duration(audio_file)
        print(f"  Muxing with audio: {audio_file} ({audio_dur:.2f}s)")
        
        # If audio is slightly longer, pad video's last frame; if video is slightly longer, cut with -shortest
        if audio_dur > raw_dur:
            pad_dur = audio_dur - raw_dur + 0.1
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
        print(f"  ! Audio missing for Scene {num}, copying video stream")
        subprocess.run([FFMPEG, "-y", "-i", raw_video, "-c", "copy", synced_output], check=True)
        
    final_dur = get_duration(synced_output)
    print(f"  ✓ Synchronized Scene {num}: {synced_output} ({final_dur:.2f}s)")
    return synced_output

def concatenate_scenes(scene_files):
    print(f"\n==========================================")
    print(f"Concatenating all {len(scene_files)} scenes into final_video_v2.mp4...")
    print(f"==========================================")
    
    concat_list = os.path.join(INTERMEDIATE_DIR, "concat_list_v2.txt")
    with open(concat_list, "w") as f:
        for p in scene_files:
            f.write(f"file '{os.path.abspath(p)}'\n")
            
    final_mp4 = os.path.join(OUTPUT_DIR, "final_video_v2.mp4")
    
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
    print(f"\n🎉 FINAL V2 VIDEO EXPORTED: {final_mp4}")
    print(f"   Total Duration: {total_dur:.2f} seconds ({total_dur/60:.2f} minutes)")
    return final_mp4

def main():
    synced_scenes = []
    for num, script, cls in SCENE_SPECS:
        out_mp4 = render_scene(num, script, cls)
        synced_scenes.append(out_mp4)
        
    final_video = concatenate_scenes(synced_scenes)
    
    val_script = os.path.join(PROJECT_DIR, "scripts", "validate_video_v2.py")
    if os.path.exists(val_script):
        subprocess.run([sys.executable, val_script], check=True)

if __name__ == "__main__":
    main()
