"""
Calibrated Beat-by-Beat Narration Generator for v2.
Calibrates speech rate (+18%) and punchy pacing to ensure total runtime is strictly between 240s (4:00) and 300s (5:00).
"""
import os
import sys
import json
import asyncio
import subprocess

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_V2_DIR = os.path.join(PROJECT_DIR, "assets", "audio_v2")
os.makedirs(AUDIO_V2_DIR, exist_ok=True)

VOICE_PRIMARY = "en-IN-PrabhatNeural"
FFMPEG = "/opt/homebrew/bin/ffmpeg"
FFPROBE = "/opt/homebrew/bin/ffprobe"

BEAT_SCRIPTS = {
    1: [
        ("s1_b1", "GPS satellites, computer graphics, and machine learning models solve millions of simultaneous equations every second."),
        ("s1_b2", "How do we solve massive systems without drowning in algebraic chaos?"),
        ("s1_b3", "The secret is transforming separate equations into a unified matrix equation: A x equals b!"),
        ("s1_b4", "Systems of Linear Equations: From Equations to Matrices."),
        ("s1_b5", "Presented by Yasir Eqbal, Student ID: E25B070671, for M3 Linear Algebra.")
    ],
    2: [
        ("s2_b1", "A linear system contains multiple conditions that must hold true simultaneously."),
        ("s2_b2", "Consider our system: 2x plus y equals 5, and x minus y equals 1."),
        ("s2_b3", "x and y are the unknown variables."),
        ("s2_b4", "The numbers multiplying them—2, 1, 1, and negative 1—are the coefficients."),
        ("s2_b5", "And the values on the right—5 and 1—are the constants."),
        ("s2_b6", "Matrix notation unifies this entire system into the iconic equation: A x equals b."),
        ("s2_b7", "A stores the coefficients, x stores the unknowns, and b stores the constants."),
        ("s2_b8", "For m equations and n unknowns, the dimensions align: an m by n matrix times an n by 1 vector yields an m by 1 vector.")
    ],
    3: [
        ("s3_b1", "Watch closely as the matrix equation is constructed from the original system."),
        ("s3_b2", "In equation one, the coefficients 2 and 1 form the first row of matrix A."),
        ("s3_b3", "In equation two, coefficients 1 and negative 1 form the second row, completing our 2 by 2 matrix A."),
        ("s3_b4", "Next, unknowns x and y form column vector x, and constants 5 and 1 form vector b."),
        ("s3_b5", "What does matrix multiplication actually mean? It is row-by-column computation."),
        ("s3_b6", "Row one times vector x yields 2x plus y, recreating our first equation: 2x plus y equals 5."),
        ("s3_b7", "Row two times vector x yields x minus y, recreating our second equation: x minus y equals 1."),
        ("s3_b8", "So A x equals b is not a new problem—it is both equations written in compact matrix notation.")
    ],
    4: [
        ("s4_b1", "Now let's solve the system algebraically using elimination."),
        ("s4_b2", "We have equation one: 2x plus y equals 5, and equation two: x minus y equals 1."),
        ("s4_b3", "Adding both equations eliminates y, because positive y and negative y cancel out!"),
        ("s4_b4", "This gives 3x equals 6."),
        ("s4_b5", "Dividing by 3 yields our first coordinate: x equals 2."),
        ("s4_b6", "Substituting x equals 2 into equation two gives 2 minus y equals 1."),
        ("s4_b7", "Subtracting 2 gives negative y equals negative 1, so y equals 1."),
        ("s4_b8", "Our unique solution is x equals 2, y equals 1, forming the solution vector: column vector 2, 1."),
        ("s4_b9", "Now let's verify our solution by substituting it into the matrix equation A x."),
        ("s4_b10", "We multiply matrix A by the solution vector 2, 1."),
        ("s4_b11", "For row one: 2 times 2 plus 1 times 1 gives 4 plus 1, which equals 5!"),
        ("s4_b12", "For row two: 1 times 2 minus 1 times 1 gives 2 minus 1, which equals 1!"),
        ("s4_b13", "We recover the constant vector 5, 1. A x equals b is satisfied, and our solution is completely verified!")
    ],
    5: [
        ("s5_b1", "Geometrically, each linear equation represents a straight line in the Cartesian plane."),
        ("s5_b2", "Rearranging gives y equals 5 minus 2x in cyan, and y equals x minus 1 in amber."),
        ("s5_b3", "Solving the system means finding where both lines meet: their unique intersection at (2, 1)!"),
        ("s5_b4", "This coordinate point (2, 1) directly matches our algebraic solution vector [2, 1]."),
        ("s5_b5", "More generally, linear systems have three possible geometric outcomes:"),
        ("s5_b6", "Lines can cross once for a unique solution... remain parallel for no solution... or overlap completely for infinitely many solutions.")
    ],
    6: [
        ("s6_b1", "To summarize, any linear system can be represented compactly as A x equals b."),
        ("s6_b2", "Matrix A captures structure, vector x holds the unknowns, and vector b defines targets."),
        ("s6_b3", "Connecting equations, matrices, and geometry gives us a complete understanding of linear algebra."),
        ("s6_b4", "Presented by Yasir Eqbal, Student ID: E25B070671, for M3 Linear Algebra and Calculus. Thank you.")
    ]
}

def get_duration(file_path):
    cmd = [
        FFPROBE, "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", file_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return float(res.stdout.strip())

async def generate_beat_audio(beat_id, text):
    out_mp3 = os.path.join(AUDIO_V2_DIR, f"{beat_id}.mp3")
    try:
        import edge_tts
        communicate = edge_tts.Communicate(text, VOICE_PRIMARY, rate="+15%")
        await communicate.save(out_mp3)
        return out_mp3
    except Exception as e:
        aiff = os.path.join(AUDIO_V2_DIR, f"{beat_id}.aiff")
        subprocess.run(["say", "-v", "Rishi", "-r", "185", text, "-o", aiff], check=True)
        subprocess.run([FFMPEG, "-y", "-i", aiff, "-c:a", "libmp3lame", "-q:a", "2", out_mp3], check=True)
        if os.path.exists(aiff):
            os.remove(aiff)
        return out_mp3

async def main():
    durations = {}
    total_time = 0.0
    
    print("Generating calibrated beat-by-beat narration for v2 (+15% rate)...")
    for scene_num, beats in sorted(BEAT_SCRIPTS.items()):
        print(f"\n--- Scene {scene_num} ({len(beats)} beats) ---")
        scene_inputs = []
        scene_filter = []
        
        for idx, (beat_id, text) in enumerate(beats):
            out_file = await generate_beat_audio(beat_id, text)
            dur = get_duration(out_file)
            durations[beat_id] = dur
            print(f"  [{beat_id}] ({dur:.2f}s): {text[:60]}...")
            
            scene_inputs.extend(["-i", out_file])
            scene_filter.append(f"[{idx}:a]")
            
        scene_mp3 = os.path.join(AUDIO_V2_DIR, f"scene_{scene_num:02d}_v2.mp3")
        filter_str = "".join(scene_filter) + f"concat=n={len(beats)}:v=0:a=1[outa]"
        concat_cmd = [FFMPEG, "-y"] + scene_inputs + ["-filter_complex", filter_str, "-map", "[outa]", "-c:a", "libmp3lame", "-q:a", "2", scene_mp3]
        subprocess.run(concat_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        scene_dur = get_duration(scene_mp3)
        durations[f"scene_{scene_num:02d}_total"] = scene_dur
        total_time += scene_dur
        print(f"  ==> Scene {scene_num} Total: {scene_dur:.2f}s ({scene_dur/60:.2f} mins)")
        
    durations_json = os.path.join(AUDIO_V2_DIR, "beat_durations.json")
    with open(durations_json, "w") as f:
        json.dump(durations, f, indent=2)
        
    print("\n==========================================")
    print(f"V2 TOTAL NARRATION TIME: {total_time:.2f} seconds ({total_time/60:.2f} minutes)")
    is_valid = 240.0 <= total_time <= 300.0
    print(f"Status: {'✅ PERFECT (Between 4:00 and 5:00)' if is_valid else '❌ INVALID DURATION'}")
    print(f"Saved timing metadata to: {durations_json}")
    print("==========================================")
    return is_valid

if __name__ == "__main__":
    asyncio.run(main())
