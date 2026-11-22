# Complete Production Storyboard

**Title:** SYSTEMS OF LINEAR EQUATIONS: From Equations to Matrices (Understanding $Ax = b$)  
**Subject:** Linear Algebra and Calculus (M3) — Internal Assessment  
**Student Name:** YASIR EQBAL  
**Student ID:** E25B070671  
**Target Duration:** 270 seconds (4 minutes 30 seconds)  
**Resolution & Aspect Ratio:** 1920 × 1080 (16:9 landscape)  
**Frame Rate:** 30 FPS  

---

## Visual & Color Identity
- **Canvas:** Deep midnight navy `#0B1220` with subtle secondary dark container `#111C2E`
- **Primary Typography:** Off-white `#F4F6FA` (LaTeX MathTex & Clean Sans-Serif)
- **Matrix A / Coefficients:** Vibrant Cyan `#39C6E6`
- **Vector x / Variables:** Warm Amber `#FFBF69`
- **Vector b / Constants:** Soft Green `#55D6A5`
- **Solution & Intersections:** Emerald Green `#22C55E`
- **Supporting Labels:** Muted Slate Grey `#A6B2C2`

---

## Scene 1: Hook & Context
- **Duration:** 00:00 – 00:25 (25.0s)
- **Purpose:** Create curiosity and introduce the problem: Can two separate equations be represented as one unified matrix equation?
- **Visual Description:**
  - Dark midnight canvas.
  - Equation 1 ($2x + y = 5$) writes on with glowing cyan coefficients and amber variables.
  - Equation 2 ($x - y = 1$) writes on beneath it.
  - A subtle animated question mark pulsates between them.
  - Callout text: *"Can two equations become one matrix equation?"*
  - The two equations converge gracefully as matrix brackets begin to frame them.
  - Main title drops in: **SYSTEMS OF LINEAR EQUATIONS**, Subtitle: *From Equations to Matrices: Understanding $Ax = b$*.
  - Student metadata badge: Yasir Eqbal (E25B070671).
- **Mathematical Content:**
  $$\begin{cases} 2x + y = 5 \\ x - y = 1 \end{cases} \implies Ax = b ?$$
- **Narration Summary:** Introduces the dilemma of handling multiple equations with multiple unknowns and introduces linear algebra's matrix framework.

---

## Scene 2: Concept Introduction
- **Duration:** 00:25 – 01:00 (35.0s)
- **Purpose:** Establish the core anatomy of a linear system and define the general matrix equation $Ax = b$ with dimensional analysis.
- **Visual Description:**
  - Both equations displayed with color-coded highlights:
    - Variables $x, y$ highlighted in Amber.
    - Coefficients $2, 1, 1, -1$ highlighted in Cyan.
    - Constants $5, 1$ highlighted in Green.
  - Semantic badges appear: `[VARIABLES]`, `[COEFFICIENTS]`, `[CONSTANTS]`.
  - The general form $Ax = b$ appears centrally with smooth scaling.
  - Component breakdown appears with labelled cards:
    - $A$: **COEFFICIENT MATRIX** ($m \times n$)
    - $x$: **VARIABLE VECTOR** ($n \times 1$)
    - $b$: **CONSTANT VECTOR** ($m \times 1$)
  - Dimension alignment visualization: $(m \times n) \times (n \times 1) = (m \times 1)$.
- **Mathematical Content:**
  $$A_{(m \times n)} \, x_{(n \times 1)} = b_{(m \times 1)}$$
- **Narration Summary:** Breaks down equations into variables, coefficients, and constants, then introduces the general matrix equation and dimensional compatibility.

---

## Scene 3: Visual Intuition & Matrix Construction
- **Duration:** 01:00 – 01:55 (55.0s)
- **Purpose:** Visually trace the extraction of coefficients and demonstrate that matrix multiplication reproduces the original equations.
- **Visual Description:**
  - Left side: Vertical arrangement of the two equations:
    - Row 1: $2x + 1y = 5$
    - Row 2: $1x - 1y = 1$
  - Right side: Empty matrix templates animate into position.
  - Animated particle paths and smooth transformation:
    - $2$ and $1$ travel into Row 1 of $A$.
    - $1$ and $-1$ travel into Row 2 of $A$.
    - $x$ and $y$ assemble into column vector $x$.
    - $5$ and $1$ travel across into constant vector $b$.
  - Resulting compact equation assembled:
    $$\begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}$$
  - Dynamic expansion of matrix multiplication:
    - Row 1 $\times$ Vector: $2(x) + 1(y) = 2x + y$
    - Row 2 $\times$ Vector: $1(x) - 1(y) = x - y$
  - Visual color link back to original equations showing exact 1-to-1 equivalence.
- **Mathematical Content:**
  $$\begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2x + y \\ x - y \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}$$
- **Narration Summary:** Demonstrates extraction of matrix entries and proves that matrix multiplication is simply compact notation for the simultaneous equations.

---

## Scene 4: Worked Example & Verification
- **Duration:** 01:55 – 03:35 (100.0s)
- **Purpose:** Solve the system algebraically step by step and formally verify the solution in the matrix equation.
- **Visual Description:**
  - Original equations presented with equation labels (1) and (2).
  - Addition of equations animated:
    - $+y$ and $-y$ flash in red and cancel out.
    - $(2x + x) = 3x$ and $(5 + 1) = 6$.
    - $3x = 6 \implies x = 2$ highlighted in an amber solution box.
  - Back-substitution:
    - Equation (2): $x - y = 1 \implies 2 - y = 1$.
    - Step-by-step rearrangement: $-y = -1 \implies y = 1$ in an amber box.
  - Assembling solution vector $x^* = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$.
  - Verification sequence:
    - Matrix $A$ and vector $x^*$ brought together.
    - Row 1 highlighted: $2(2) + 1(1) = 4 + 1 = 5$.
    - Row 2 highlighted: $1(2) - 1(1) = 2 - 1 = 1$.
    - Output vector evaluates to $\begin{bmatrix} 5 \\ 1 \end{bmatrix} = b$.
    - Glowing emerald checkmark and `[VERIFIED: Ax = b]` badge appear.
- **Mathematical Content:**
  $$(2x+y) + (x-y) = 6 \implies 3x = 6 \implies x = 2$$
  $$2 - y = 1 \implies y = 1 \implies x^* = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$
  $$\begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix}\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 2(2)+1(1) \\ 1(2)-1(1) \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \end{bmatrix} = b$$
- **Narration Summary:** Guides viewer through elimination, substitution, and rigorous row-by-column verification.

---

## Scene 5: Geometric Interpretation & Solution Sets
- **Duration:** 03:35 – 04:05 (30.0s)
- **Purpose:** Connect the algebraic solution to the intersection of lines on a Cartesian coordinate plane and introduce the three possible solution-set outcomes.
- **Visual Description:**
  - Coordinate axes appear with crisp gridlines.
  - Line 1 ($y = 5 - 2x$) plotted in Cyan.
  - Line 2 ($y = x - 1$) plotted in Amber.
  - Intersection point $(2, 1)$ pulses with an emerald green highlight.
  - Visual bridge connecting $(2, 1)$ to column vector $\begin{bmatrix} 2 \\ 1 \end{bmatrix}$.
  - Triptych layout showing the three fundamental cases:
    1. **ONE SOLUTION:** Crossing lines ($m_1 \neq m_2$).
    2. **NO SOLUTION:** Parallel lines ($m_1 = m_2, c_1 \neq c_2$).
    3. **INFINITELY MANY:** Overlapping identical lines ($m_1 = m_2, c_1 = c_2$).
- **Mathematical Content:**
  $$y = -2x + 5 \cap y = x - 1 \implies (2, 1)$$
  $$\text{Cases: Unique Solution, No Solution (Inconsistent), Infinitely Many (Dependent)}$$
- **Narration Summary:** Explains how linear equations describe lines whose intersection is the algebraic solution, then contextualizes the three solution set cases.

---

## Scene 6: Summary & Credits
- **Duration:** 04:05 – 04:30 (25.0s)
- **Purpose:** Synthesize key takeaways and present official academic internal assessment credits.
- **Visual Description:**
  - Clean midnight navy backdrop.
  - Core takeaways appear sequentially with glowing bullets:
    1. Matrix $A$ encodes coefficients and system structure.
    2. Vector $x$ holds unknown variables.
    3. Vector $b$ stores constant targets.
  - Central synthesis equation:
    $$Ax = b \iff \text{Equations} \longleftrightarrow \text{Matrices} \longleftrightarrow \text{Geometry}$$
  - Academic submission card:
    - Subject: M3 — Linear Algebra and Calculus
    - Topic: Systems of Linear Equations ($Ax = b$)
    - Student: **YASIR EQBAL**
    - Student ID: **E25B070671**
    - Engine: Python 3.13 + Manim Community Edition
    - Voiceover: Microsoft Edge Neural TTS
  - Smooth cinematic fade to black.
- **Narration Summary:** Recaps the power of $Ax=b$ notation and closes the educational video.
