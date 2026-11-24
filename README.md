# M3 Mathematics Animation Video Project
## Systems of Linear Equations: From Equations to Matrices (Understanding $Ax = b$)

[![Course](https://img.shields.io/badge/Course-M3%20Linear%20Algebra%20%26%20Calculus-0B1220?style=for-the-badge)](https://github.com/nsaky/M3_Linear_Equations_Animation)
[![Topic](https://img.shields.io/badge/Topic-Systems%20of%20Linear%20Equations-39C6E6?style=for-the-badge)](https://github.com/nsaky/M3_Linear_Equations_Animation)
[![Engine](https://img.shields.io/badge/Rendered%20with-Manim%20Community%20v0.22-FFBF69?style=for-the-badge)](https://www.manim.community/)
[![Resolution](https://img.shields.io/badge/Resolution-1080p%20%7C%2030%20FPS-55D6A5?style=for-the-badge)](https://github.com/nsaky/M3_Linear_Equations_Animation)
[![Duration](https://img.shields.io/badge/Duration-4m%2040s%20(280.15s)-39C6E6?style=for-the-badge)](https://github.com/nsaky/M3_Linear_Equations_Animation)

**Student Name:** YASIR EQBAL  
**Student ID:** E25B070671  
**Assessment:** Internal Assessment — Educational Mathematics Animation Video  
**Official Guiding Question:** *"How can a system be written as Ax = b? Connect equations, coefficient matrices, and solution sets."*  
**Final Rendered Video:** [`output/final_video_m3_animation.mp4`](output/final_video_m3_animation.mp4)

---

## 📌 Project Overview
This project is an end-to-end, professionally directed educational mathematics animation designed for undergraduate engineering students taking Linear Algebra and Calculus (M3). Built using **Python and Manim Community Edition**, it explains:
1. **The Hook & Computational Context:** Why systems of equations matter—from satellite orbital navigation to machine learning optimization and 3D graphics rendering.
2. **Algebraic Anatomy:** Deconstructing equations into coefficients, variables, and constants.
3. **Matrix Vector Formulation ($Ax = b$):** Converting systems into matrix notation and establishing dimension compatibility ($m \times n$, $n \times 1$, $m \times 1$).
4. **Equivalence via Matrix Multiplication:** Proving that row-by-column multiplication reproduces the original simultaneous equations.
5. **Step-by-Step Algebraic Solution:** Solving $2x + y = 5$ and $x - y = 1$ via elimination and substitution to find $\mathbf{x} = [2, 1]^T$.
6. **Rigorous Matrix Verification:** Directly substituting the solution vector back into $Ax = b$ to verify $A\mathbf{x} = \mathbf{b}$.
7. **Geometric Interpretation & Solution Sets:** Plotting both lines on the Cartesian plane, spotlighting the intersection point $(2, 1)$, and classifying the three fundamental geometric realities: **Unique Solution** (intersecting lines), **No Solution** (parallel lines), and **Infinitely Many Solutions** (coincident lines).

---

## 🎨 Visual Identity & Color Palette
- **Canvas Background:** Deep Midnight Navy (`#0B1220`) & Dark Indigo (`#111C2E`)
- **Primary Typography:** Off-White (`#F4F6FA`) with LaTeX Math rendering
- **Matrix A & Coefficients:** Electric Cyan (`#39C6E6`)
- **Vector x & Unknown Variables:** Radiant Amber (`#FFBF69`)
- **Vector b & Constants:** Soft Green (`#55D6A5`)
- **Intersection Point / Solution:** Bright Neon Emerald (`#00FFA3` / `#22C55E`)
- **Supporting Badges & Grids:** Slate Muted Grey (`#A6B2C2`)

---

## 📁 Repository Structure
```
M3_Linear_Equations_Animation/
├── README.md                           # Project documentation & execution guide
├── requirements.txt                     # Python dependencies
├── main.py                              # One-click master production entry point
├── config.py                            # Shared styling, color constants, and helpers
├── scenes_v2/                           # High-engagement, beat-synchronized Manim scenes
│   ├── v2_utils.py                      # Millisecond-accurate audio sync engine
│   ├── scene_01_intro_v2.py             # Scene 1: High-Energy Hook & Computing Context
│   ├── scene_02_concept_v2.py           # Scene 2: Components & General Form (Ax = b)
│   ├── scene_03_matrix_construction_v2.py # Scene 3: Coefficient Extraction & Multiplication
│   ├── scene_04_worked_example_v2.py    # Scene 4: Elimination, Substitution & Verification
│   ├── scene_05_solution_sets_v2.py     # Scene 5: Cartesian Plane & 3 Solution Realities
│   └── scene_06_summary_v2.py           # Scene 6: Mathematical Synthesis & Academic Credits
├── assets/
│   ├── audio_v2/                        # 44 discrete vocal beats & scene audio tracks
│   │   ├── beat_durations.json          # Millisecond calibration database
│   │   ├── s1_b1.mp3 ... s6_b4.mp3      # Granular audio beats
│   │   └── scene_01_v2.mp3 ...          # Scene audio mixes
│   ├── music/                           # Ambient background audio
│   └── fonts/                           # Project typography
├── scripts/
│   ├── generate_narration_v2.py         # Voiceover generation with Edge-TTS
│   ├── render_video_v2.py               # 1080p30 render, audio mux, and concatenation pipeline
│   └── validate_video_v2.py             # Technical QA suite & snapshot extractor
├── output/
│   └── final_video_m3_animation.mp4     # Master 1080p 30fps finalized MP4 video (280.15s)
└── documentation/
    ├── storyboard.md                    # Six-scene comprehensive storyboard
    ├── storyboard.pdf                   # Formatted submission storyboard PDF
    ├── narration_script.md              # Complete timestamped voiceover script
    ├── mathematical_verification.md     # Step-by-step mathematical proofs
    ├── v2_production_notes.md           # Technical specifications & v2 production log
    └── snapshots_v2/                    # 1080p inspection frame captures
```

---

## 🚀 Installation & Execution

### 1. Prerequisites
Ensure you have Python 3.10+, FFmpeg, and LaTeX (TinyTeX / MacTeX) installed:
```bash
# macOS via Homebrew
brew install ffmpeg pango cairo pkg-config
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Production Pipeline
To render all scenes in 1080p, synchronize audio, assemble the master video, and run validation:
```bash
python3 main.py
```

### 4. Render an Individual Scene
```bash
# Example: Render Scene 3 in 1080p 30fps
python3 -m manim -qh --fps 30 -r 1920,1080 scenes_v2/scene_03_matrix_construction_v2.py Scene03MatrixConstructionV2
```

---

## 📊 Technical Specifications of Master Video
- **File Name:** `output/final_video_m3_animation.mp4`
- **Total Duration:** 280.15 seconds (4 minutes 40.15 seconds) — **Strictly between 4m and 5m**
- **Resolution:** $1920 \times 1080$ (1080p Full HD)
- **Aspect Ratio:** 16:9 Landscape
- **Frame Rate:** 30.00 FPS
- **Video Codec:** H.264 (`libx264`, High Profile, CRF 18, `yuv420p`)
- **Audio Codec:** AAC (Stereo, 192 kbps, 24 kHz)
- **File Size:** ~10.60 MB

---

## 📑 Academic Disclosures & References
- **Student Name:** YASIR EQBAL
- **Student ID:** E25B070671
- **Course:** M3 — Linear Algebra and Calculus
- **AI Tool Disclosure:** AI tools utilized for script refinement, code structuring, visual layout design, and neural voiceover synthesis under internal assessment guidelines.
- **Mathematical References:** Standard Undergraduate Linear Algebra (Strang, Lay, Anton & Rorres).
