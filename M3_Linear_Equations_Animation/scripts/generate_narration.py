"""
Calibrated Narration Generation for exact 4m 30s target (270s total, strictly < 300s).
"""
import os
import sys
import asyncio
import subprocess

AUDIO_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

VOICE_PRIMARY = "en-IN-PrabhatNeural"

NARRATION_SCRIPTS = {
    1: {
        "title": "Hook & Context",
        "target_duration": 25.0,
        "rate": "+5%",
        "text": (
            "Imagine two equations with two unknowns: 2x plus y equals 5, and x minus y equals 1. "
            "How do we represent both together in a single expression? "
            "Linear algebra gives us matrix notation. "
            "In this video, we'll see how a system becomes A x equals b, and what its solutions actually mean."
        )
    },
    2: {
        "title": "Concept Introduction",
        "target_duration": 35.0,
        "rate": "+6%",
        "text": (
            "A system of linear equations contains multiple conditions that hold true simultaneously. "
            "Here, x and y are the unknown variables. "
            "The numbers multiplying them are coefficients: 2, 1, 1, and negative 1. "
            "The numbers on the right are constants: 5 and 1. "
            "Matrix notation unifies this into A x equals b. "
            "A stores coefficients, x stores unknowns, and b stores constants. "
            "For m equations and n unknowns, their dimensions fit as m by n, n by 1, and m by 1."
        )
    },
    3: {
        "title": "Visual Intuition & Matrix Construction",
        "target_duration": 55.0,
        "rate": "+6%",
        "text": (
            "Let's build the matrix equation from our example. "
            "In equation one, the coefficients of x and y are 2 and 1. These form the first row of matrix A. "
            "In equation two, the coefficients are 1 and negative 1. These form the second row. "
            "Together, they form our 2 by 2 coefficient matrix A. "
            "Next, we collect the unknowns into vector x, and the constants into vector b. "
            "When we multiply A by x, the first row recreates our first equation: 2x plus y equals 5. "
            "The second row recreates our second equation: x minus y equals 1. "
            "So A x equals b is simply both equations expressed together in compact matrix form."
        )
    },
    4: {
        "title": "Worked Example & Verification",
        "target_duration": 100.0,
        "rate": "+6%",
        "text": (
            "Now let's solve the system algebraically. "
            "We have equation one: 2x plus y equals 5, and equation two: x minus y equals 1. "
            "Adding both equations eliminates y, because positive y and negative y cancel out. "
            "This gives 3x equals 6. Dividing by 3, we find x equals 2. "
            "Substituting x equals 2 into the second equation gives 2 minus y equals 1, so y equals 1. "
            "Our unique algebraic solution is the column vector 2, 1. "
            "Now, let's verify by substitution into our matrix equation A x. "
            "We multiply the coefficient matrix by our solution vector 2, 1. "
            "For row one: 2 times 2 plus 1 times 1 gives 4 plus 1, which equals 5. "
            "For row two: 1 times 2 minus 1 times 1 gives 2 minus 1, which equals 1. "
            "This produces the vector 5, 1, exactly matching vector b. "
            "A x equals b is satisfied, proving our solution is correct."
        )
    },
    5: {
        "title": "Geometric Interpretation & Solution Sets",
        "target_duration": 30.0,
        "rate": "+6%",
        "text": (
            "Geometrically, each linear equation represents a straight line. "
            "Solving the system means finding where the two lines meet. "
            "Rearranging gives y equals 5 minus 2x, and y equals x minus 1. "
            "They intersect at the single point (2, 1), directly matching our matrix solution vector. "
            "More generally, two lines can intersect once for a unique solution, remain parallel for no solution, "
            "or coincide completely for infinitely many solutions."
        )
    },
    6: {
        "title": "Summary & Credits",
        "target_duration": 25.0,
        "rate": "+5%",
        "text": (
            "To summarize, a system of linear equations is compactly represented as A x equals b. "
            "Matrix A stores the coefficients, vector x contains the unknowns, and vector b holds the constants. "
            "This assessment was presented by Yasir Eqbal, Student ID: E25B070671, for M3 Linear Algebra and Calculus. "
            "Thank you for watching."
        )
    }
}

async def generate_scene_audio(scene_num, info):
    output_path = os.path.join(AUDIO_DIR, f"scene_{scene_num:02d}.mp3")
    text = info["text"]
    rate = info.get("rate", "+5%")
    print(f"Generating calibrated audio for Scene {scene_num}: {info['title']} (rate {rate})...")
    
    try:
        import edge_tts
        communicate = edge_tts.Communicate(text, VOICE_PRIMARY, rate=rate)
        await communicate.save(output_path)
        return output_path
    except Exception as e:
        print(f"  Fallback for Scene {scene_num}: {e}")
        aiff_path = os.path.join(AUDIO_DIR, f"scene_{scene_num:02d}.aiff")
        subprocess.run(["say", "-v", "Rishi", "-r", "175", text, "-o", aiff_path], check=True)
        subprocess.run(["/opt/homebrew/bin/ffmpeg", "-y", "-i", aiff_path, "-codec:a", "libmp3lame", "-qscale:a", "2", output_path], check=True)
        if os.path.exists(aiff_path):
            os.remove(aiff_path)
        return output_path

async def main():
    for scene_num, info in sorted(NARRATION_SCRIPTS.items()):
        await generate_scene_audio(scene_num, info)
        
    print("\nCalibrated audio durations:")
    total = 0.0
    for scene_num in sorted(NARRATION_SCRIPTS.keys()):
        p = os.path.join(AUDIO_DIR, f"scene_{scene_num:02d}.mp3")
        res = subprocess.run([
            "/opt/homebrew/bin/ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", p
        ], capture_output=True, text=True)
        dur = float(res.stdout.strip())
        total += dur
        print(f"  Scene {scene_num:02d}: {dur:.2f}s (Target: {NARRATION_SCRIPTS[scene_num]['target_duration']:.1f}s)")
    print(f"\nTOTAL AUDIO DURATION: {total:.2f}s ({total/60:.2f} minutes) - Target 270s, Max 300s.")

if __name__ == "__main__":
    asyncio.run(main())
