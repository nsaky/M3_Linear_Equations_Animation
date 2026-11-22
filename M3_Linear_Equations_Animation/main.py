"""
Master Entry Point for M3 Linear Equations Animation Project
Executes end-to-end production: Narration -> Storyboard PDF -> Video Rendering -> Validation.
"""
import os
import sys
import subprocess

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(PROJECT_DIR, "scripts")
DOCS_DIR = os.path.join(PROJECT_DIR, "documentation")

# Set up PATH for TinyTeX & Homebrew
TINYTEX_BIN = "/Users/yasireqbal/Library/TinyTeX/bin/universal-darwin"
HOMEBREW_BIN = "/opt/homebrew/bin"
os.environ["PATH"] = f"{TINYTEX_BIN}:{HOMEBREW_BIN}:{os.environ.get('PATH', '')}"

def main():
    print("=" * 60)
    print(" M3 LINEAR ALGEBRA & CALCULUS: ANIMATION VIDEO PIPELINE")
    print(" Systems of Linear Equations: From Equations to Matrices (Ax = b)")
    print(" Student: YASIR EQBAL | Student ID: E25B070671")
    print("=" * 60)
    
    # Step 1: Generate Narration
    print("\n[STEP 1/4] Generating Voiceover Narration Audio...")
    subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, "generate_narration.py")], check=True)
    subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, "combine_audio.py")], check=True)
    
    # Step 2: Generate Storyboard PDF
    print("\n[STEP 2/4] Generating Storyboard PDF Document...")
    subprocess.run([sys.executable, os.path.join(DOCS_DIR, "generate_storyboard_pdf.py")], check=True)
    
    # Step 3: Render and Assemble Final Video
    print("\n[STEP 3/4] Rendering 6 Manim Scenes (1080p 30fps) and Assembling MP4...")
    subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, "render_video.py")], check=True)
    
    # Step 4: Quality Assurance and Validation
    print("\n[STEP 4/4] Validating Video Specifications & Extracting Snapshots...")
    subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, "validate_video.py")], check=True)
    
    print("\n" + "=" * 60)
    print("🎉 FULL PRODUCTION PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
