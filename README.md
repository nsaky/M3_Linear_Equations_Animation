# M3 Mathematics Animation Video Project
## Systems of Linear Equations: From Equations to Matrices (Understanding $Ax = b$)

[![Course](https://img.shields.io/badge/Course-M3%20Linear%20Algebra%20%26%20Calculus-0B1220?style=for-the-badge)](https://github.com)
[![Topic](https://img.shields.io/badge/Topic-Systems%20of%20Linear%20Equations-39C6E6?style=for-the-badge)](https://github.com)
[![Engine](https://img.shields.io/badge/Rendered%20with-Manim%20Community%20v0.22-FFBF69?style=for-the-badge)](https://www.manim.community/)
[![Resolution](https://img.shields.io/badge/Resolution-1080p%20%7C%2030%20FPS-55D6A5?style=for-the-badge)](https://github.com)

**Student Name:** YASIR EQBAL  
**Student ID:** E25B070671  
**Assessment:** Internal Assessment — Educational Mathematics Animation Video  
**Guiding Question:** *"How can a system be written as Ax = b? Connect equations, coefficient matrices, and solution sets."*

---

## 📌 Project Overview
This project is an end-to-end, professionally directed educational mathematics animation designed for undergraduate students taking Linear Algebra and Calculus (M3). Built using **Python and Manim Community Edition**, it explains:
1. What a system of simultaneous linear equations represents.
2. How to extract coefficients, variables, and constants into the matrix form $Ax = b$.
3. How matrix multiplication reproduces the original equations.
4. Step-by-step algebraic solution via elimination and substitution.
5. Rigorous verification by matrix substitution ($Ax^* = b$).
6. Geometric interpretation of the solution as the intersection of lines in $\mathbb{R}^2$.
7. The three fundamental solution-set outcomes: **Unique Solution**, **No Solution**, and **Infinitely Many Solutions**.

---

## 🎨 Visual Identity & Color Palette
- **Canvas Background:** Deep Midnight Navy (`#0B1220`) & Dark Indigo (`#111C2E`)
- **Primary Typography:** Off-White (`#F4F6FA`) with LaTeX Math rendering
- **Matrix A & Coefficients:** Electric Cyan (`#39C6E6`)
- **Vector x & Unknown Variables:** Radiant Amber (`#FFBF69`)
- **Vector b & Constants:** Soft Green (`#55D6A5`)
- **Intersection Point / Solution:** Bright Emerald (`#22C55E`)
- **Supporting Badges & Grids:** Slate Muted Grey (`#A6B2C2`)

---

## 📁 Repository Structure
```
M3_Linear_Equations_Animation/
├── README.md                           # Project documentation & execution guide
├── requirements.txt                     # Python dependencies
├── main.py                              # One-click master production entry point
├── config.py                            # Shared styling, color constants, and helpers
├── scenes/                              # Independent modular Manim scene scripts
│   ├── scene_01_intro.py                # Scene 1: Hook & Context
│   ├── scene_02_concept.py              # Scene 2: Concept Introduction (Ax = b)
│   ├── scene_03_matrix_construction.py  # Scene 3: Visual Extraction & Multiplication
│   ├── scene_04_worked_example.py       # Scene 4: Elimination & Matrix Verification
│   ├── scene_05_solution_sets.py        # Scene 5: Cartesian Plane & 3 Solution Cases
│   └── scene_06_summary.py              # Scene 6: Synthesis & Academic Credits
├── assets/
│   ├── audio/                           # Synthesized scene voiceovers & full track
│   ├── music/                           # Optional ambient background audio
│   └── fonts/                           # Project typography
├── scripts/
│   ├── generate_narration.py            # Calibrated voiceover generator
│   ├── combine_audio.py                 # Multi-track narration compiler
│   ├── render_video.py                  # High-definition video render & mux pipeline
│   └── validate_video.py                # Technical QA & frame snapshot extraction
├── output/
│   └── final_video.mp4                  # Full 1080p 30fps finalized MP4 video
└── documentation/
    ├── storyboard.md                    # Detailed six-scene storyboard
    ├── storyboard.pdf                   # Formatted submission PDF
    ├── narration_script.md              # Complete timestamped voiceover script
    ├── mathematical_verification.md     # Mathematical proof and verification
    ├── production_notes.md              # Technical specifications & design notes
    └── snapshots/                       # High-resolution video frame captures
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

### 3. Run the Full Production Pipeline
To generate voiceover, render all scenes in 1080p, assemble the video, and run validation:
```bash
python3 main.py
```

### 4. Render an Individual Scene
```bash
# Example: Render Scene 3 in 1080p 30fps
python3 -m manim -qh --fps 30 -r 1920,1080 scenes/scene_03_matrix_construction.py Scene03MatrixConstruction
```

---

## 📊 Technical Specifications of Exported Video
- **File Location:** `output/final_video.mp4`
- **Resolution:** $1920 \times 1080$ (1080p Full HD)
- **Aspect Ratio:** 16:9 Landscape
- **Frame Rate:** 30.00 FPS
- **Target Duration:** 270 seconds (4m 30s)
- **Max Duration Limit:** Strictly $< 300$ seconds (5m 00s)
- **Video Codec:** H.264 (libx264, High Profile, CRF 18)
- **Audio Codec:** AAC (192 kbps, 44.1 kHz, Stereo)

---

## 📑 Academic Disclosures & References
- **Student Name:** YASIR EQBAL
- **Student ID:** E25B070671
- **Course:** M3 — Linear Algebra and Calculus
- **AI Tool Disclosure:** AI tools utilized for script refinement, code structuring, visual layout design, and neural voiceover synthesis under internal assessment guidelines.
- **Mathematical References:** Standard Undergraduate Linear Algebra (Strang, Lay, Anton & Rorres).
