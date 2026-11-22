# Production Notes & Technical Specifications

**Project:** Systems of Linear Equations — From Equations to Matrices: Understanding $Ax = b$  
**Course:** M3 — Linear Algebra and Calculus (Internal Assessment)  
**Author / Presenter:** YASIR EQBAL (Student ID: E25B070671)  
**Production Date:** November 2026  

---

## 1. Executive Summary
This production is an end-to-end mathematical animation video engineered specifically for an M3 internal assessment in Linear Algebra. The video explains the transition from simultaneous linear equations to the compact matrix equation $Ax = b$, interprets matrix-vector multiplication as a simultaneous system of linear equations, solves a worked example algebraically with substitution verification, and bridges the algebraic solution to geometric lines and the three fundamental solution set classes.

---

## 2. Technical Video Specifications
- **Container:** MP4
- **Video Codec:** H.264 (AVC)
- **Audio Codec:** AAC (192 kbps, 44.1 kHz, Stereo)
- **Resolution:** 1920 × 1080 (1080p, Full HD)
- **Aspect Ratio:** 16:9 Landscape
- **Target Frame Rate:** 30.00 FPS
- **Target Duration:** 270 seconds (4 minutes 30 seconds)
- **Duration Constraint:** Strictly $< 300$ seconds (5 minutes)

---

## 3. Visual Styling & Color Hierarchy
A dark mathematical canvas was implemented to ensure optimal readability and aesthetic presentation:
- **Background:** Deep Midnight Navy (`#0B1220`)
- **Container Background:** Dark Indigo (`#111C2E`)
- **Primary Text:** Crisp Off-White (`#F4F6FA`)
- **Matrix $A$ & Coefficients:** Electric Cyan (`#39C6E6`)
- **Vector $x$ & Unknowns:** Radiant Amber (`#FFBF69`)
- **Vector $b$ & Constants:** Soft Emerald Green (`#55D6A5`)
- **Intersection Point / Solution:** Vivid Green (`#22C55E`)
- **Supporting Annotations & Grids:** Slate Muted Grey (`#A6B2C2`)

---

## 4. Software Stack & Tooling
- **Animation Framework:** Python 3.13 + Manim Community Edition v0.22.1
- **Mathematical Typesetting:** LaTeX (TinyTeX / pdflatex + dvisvgm)
- **Audio Narration Engine:** Microsoft Edge Neural TTS (`en-IN-PrabhatNeural`)
- **Video Composition & Transcoding:** FFmpeg 9.0.2
- **Document Generation:** ReportLab 5.1 (PDF compilation)
