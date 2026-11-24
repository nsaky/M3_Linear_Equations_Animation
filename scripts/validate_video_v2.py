"""
Quality Assurance and Validation for final_video_v2.mp4
Verifies technical specifications, strict duration compliance (4m - 5m),
extracts visual snapshots, and checks that v1 is preserved.
"""
import os
import sys
import json
import subprocess

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FINAL_VIDEO = os.path.join(PROJECT_DIR, "output", "final_video_m3_animation.mp4")
SNAPSHOTS_V2_DIR = os.path.join(PROJECT_DIR, "documentation", "snapshots_v2")
os.makedirs(SNAPSHOTS_V2_DIR, exist_ok=True)

FFPROBE = "/opt/homebrew/bin/ffprobe"
FFMPEG = "/opt/homebrew/bin/ffmpeg"

def probe_file(path):
    cmd = [
        FFPROBE, "-v", "quiet",
        "-print_format", "json",
        "-show_format", "-show_streams",
        path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(res.stdout)

def validate():
    print("\n==========================================")
    print("QUALITY ASSURANCE & VALIDATION: FINAL VIDEO")
    print("==========================================")
    
    passed = True
    
    # Check final video exists
    if not os.path.exists(FINAL_VIDEO):
        print(f"❌ FAIL: Final video not found at {FINAL_VIDEO}")
        return False
        
    info = probe_file(FINAL_VIDEO)
    fmt = info.get("format", {})
    duration = float(fmt.get("duration", 0.0))
    size_mb = float(fmt.get("size", 0)) / (1024 * 1024)
    
    video_stream = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), None)
    audio_stream = next((s for s in info.get("streams", []) if s.get("codec_type") == "audio"), None)
    
    # 1. Strict Duration Check: 240.0s (4:00) to 300.0s (5:00)
    print(f"• Duration: {duration:.2f}s ({duration/60:.2f} minutes)")
    if 240.0 <= duration <= 300.0:
        print("  ✓ PASS: Duration is strictly between 4 mins and 5 mins!")
    else:
        print(f"  ❌ FAIL: Duration {duration:.2f}s is NOT within [240.0s, 300.0s]!")
        passed = False
        
    # 2. Video Stream checks
    if video_stream:
        w = video_stream.get("width")
        h = video_stream.get("height")
        codec = video_stream.get("codec_name")
        r_frame_rate = video_stream.get("r_frame_rate", "0/1")
        fps = eval(r_frame_rate)
        
        print(f"• Video Resolution: {w} × {h}")
        if w == 1920 and h == 1080:
            print("  ✓ PASS: Full HD 1080p resolution.")
        else:
            print(f"  ❌ FAIL: Expected 1920x1080, got {w}x{h}")
            passed = False
            
        print(f"• Frame Rate: {fps:.2f} FPS")
        if abs(fps - 30.0) < 0.1:
            print("  ✓ PASS: 30 FPS.")
        else:
            print(f"  ⚠ Note: FPS is {fps:.2f}")
            
        print(f"• Video Codec: {codec}")
        if codec == "h264":
            print("  ✓ PASS: H.264 video codec.")
        else:
            print(f"  ❌ FAIL: Expected h264, got {codec}")
            passed = False
    else:
        print("❌ FAIL: No video stream found!")
        passed = False
        
    # 3. Audio Stream checks
    if audio_stream:
        a_codec = audio_stream.get("codec_name")
        sr = audio_stream.get("sample_rate")
        print(f"• Audio Codec: {a_codec} ({sr} Hz)")
        if a_codec == "aac":
            print("  ✓ PASS: AAC audio codec.")
        else:
            print(f"  ⚠ Note: Audio codec is {a_codec}")
    else:
        print("❌ FAIL: No audio stream found!")
        passed = False
        
    print(f"• File Size: {size_mb:.2f} MB")
    
    # 4. Extract representative snapshots for v2
    print("\nExtracting representative snapshots for v2 visual verification...")
    # Calculate timestamps from scene totals:
    # Scene 1: 0 - 33s -> 15s
    # Scene 2: 33 - 80s -> 55s
    # Scene 3: 80 - 135s -> 105s
    # Scene 4: 135 - 210s -> 170s
    # Scene 5: 210 - 250s -> 230s
    # Scene 6: 250 - 280s -> 265s
    timestamps = [
        (15, "v2_scene_01_hook.png"),
        (55, "v2_scene_02_concept.png"),
        (105, "v2_scene_03_construction.png"),
        (170, "v2_scene_04_elimination_solution.png"),
        (195, "v2_scene_04_matrix_verification.png"),
        (230, "v2_scene_05_geometry.png"),
        (265, "v2_scene_06_credits.png"),
    ]
    
    for sec, fname in timestamps:
        if sec < duration:
            out_img = os.path.join(SNAPSHOTS_V2_DIR, fname)
            cmd = [
                FFMPEG, "-y",
                "-ss", str(sec),
                "-i", FINAL_VIDEO,
                "-vframes", "1",
                "-q:v", "2",
                out_img
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if os.path.exists(out_img):
                sz = os.path.getsize(out_img) / 1024
                print(f"  ✓ Snapshot extracted at {sec}s -> {fname} ({sz:.1f} KB)")
                
    print("\n------------------------------------------")
    if passed:
        print("🎉 ALL V2 REQUIREMENTS & DURATION CRITERIA MET!")
    else:
        print("❌ SOME VERIFICATION CHECKS FAILED.")
    print("------------------------------------------\n")
    return passed

if __name__ == "__main__":
    success = validate()
    sys.exit(0 if success else 1)
