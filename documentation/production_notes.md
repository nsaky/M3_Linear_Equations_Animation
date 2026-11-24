# Production Notes & Technical Specifications

## Master Video Details
- **Title:** Systems of Linear Equations: From Equations to Matrices ($Ax = b$)
- **Course:** College-Level Linear Algebra and Calculus (M3)
- **Student Name:** Yasir Eqbal
- **Student ID:** E25B070671
- **File Name:** `output/final_video_m3_animation.mp4`
- **Duration:** 280.15 seconds (4 minutes 40.15 seconds) — **Strictly compliant with [240s, 300s]**
- **Resolution:** 1920 × 1080 (1080p Full HD)
- **Frame Rate:** 30.00 FPS
- **Video Codec:** H.264 (libx264, yuv420p, crf=18)
- **Audio Codec:** AAC (192 kbps, 24 kHz)

---

## Key Animation Features & Innovations

### 1. High-Energy Hook
- **Visual Opening:**
  - Dynamic camera sweep over an illuminated coordinate plane and cyber-vector radar scanner.
  - Floating 3D matrix array displaying $10^6 \times 10^6$ computational systems.
  - Direct contextual hook: satellite orbital dynamics, neural network training, aerodynamic CFD simulations, and real-time ray tracing all rely on solving $Ax = b$.

### 2. Beat-by-Beat Audio-Visual Synchronization
- **Zero Drift Architecture:**
  - Narration script segmented into 44 discrete vocal beats across 6 scenes.
  - Each individual beat MP3 timed to the exact millisecond (`assets/audio_v2/beat_durations.json`).
  - Implemented `play_beat_sync()` in `scenes_v2/v2_utils.py` to dynamically measure the execution time of on-screen animations (equations writing, line drawing, matrix morphing) and clamp pauses to match spoken syllables precisely.
  - Mathematical terms illuminate and pulse on-screen at the exact millisecond they are vocalized.

### 3. Visual FX & Polish
- **Neon Badges & Dynamic Cards:**
  - Modern translucent glassmorphic cards (`create_glass_card()`).
  - High-visibility pulsing neon badges (`UNIQUE SOLUTION`, `SYSTEM INCONSISTENT`, `VERIFIED: Ax = b`).
- **Mathematical Color Consistency:**
  - Cyan (`#39C6E6`): Matrix $A$, coefficients, Line 1 ($2x + y = 5$).
  - Amber (`#FFBF69`): Vector $\mathbf{x}$, variables, Line 2 ($x - y = 1$).
  - Green (`#55D6A5`): Vector $\mathbf{b}$, constants, matrix product verification.
  - Bright Green (`#00FFA3`): Intersection point $(2, 1)$, target radar beacon.

### 4. Mathematical Content Coverage
1. **Scene 1:** Introduction to simultaneous systems & hook into modern computation.
2. **Scene 2:** Dissection of algebraic anatomy (coefficients, variables, constants) and general matrix dimensions ($m \times n$, $n \times 1$, $m \times 1$).
3. **Scene 3:** Progressive extraction of coefficients into $A$, unknowns into $\mathbf{x}$, constants into $\mathbf{b}$, and expansion showing $A\mathbf{x} = \mathbf{b}$ reproduces the original equations row by row.
4. **Scene 4:** Step-by-step algebraic elimination ($y$-cancellation, $3x = 6 \implies x = 2$), substitution ($y = 1$), and formal matrix verification ($A\mathbf{x} = [5, 1]^T = \mathbf{b}$).
5. **Scene 5:** Dynamic Cartesian coordinate plot of both lines, intersection point radar ping at $(2, 1)$, and comparison of the 3 fundamental geometric cases:
   - Unique solution: intersecting lines ($\det(A) \neq 0$).
   - No solution: parallel non-intersecting lines (inconsistent).
   - Infinitely many solutions: coincident lines (linearly dependent).
6. **Scene 6:** Synthesis, 3 foundational pillars of $Ax = b$, and academic assessment credits for Yasir Eqbal (`E25B070671`).
