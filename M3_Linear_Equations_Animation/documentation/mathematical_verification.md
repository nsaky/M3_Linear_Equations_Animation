# Mathematical Verification Document

**Subject:** Linear Algebra and Calculus (M3)  
**Topic:** Systems of Linear Equations — From Equations to Matrices  
**Student:** YASIR EQBAL (ID: E25B070671)  

---

## 1. The Original System of Linear Equations

Consider the system of two simultaneous linear equations in two unknowns $x, y \in \mathbb{R}$:
$$\begin{aligned}
2x + y &= 5 \quad \text{--- (Equation 1)} \\
x - y &= 1 \quad \text{--- (Equation 2)}
\end{aligned}$$

- **Variables (unknowns):** $\mathbf{x} = \begin{bmatrix} x \\ y \end{bmatrix}$
- **Coefficients:**
  - Row 1: $a_{11} = 2, a_{12} = 1$
  - Row 2: $a_{21} = 1, a_{22} = -1$
- **Constants (right-hand sides):**
  - $b_1 = 5, b_2 = 1$

---

## 2. Construction of Matrix Equation $Ax = b$

### 2.1 Coefficient Matrix $A \in \mathbb{R}^{2 \times 2}$
Extracting coefficients row-by-row in variable order $(x, y)$:
$$A = \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix}$$

### 2.2 Unknown Variable Vector $x \in \mathbb{R}^{2 \times 1}$
$$x = \begin{bmatrix} x \\ y \end{bmatrix}$$

### 2.3 Constant Vector $b \in \mathbb{R}^{2 \times 1}$
$$b = \begin{bmatrix} 5 \\ 1 \end{bmatrix}$$

### 2.4 Dimension Consistency
$$A_{(2 \times 2)} \, x_{(2 \times 1)} = b_{(2 \times 1)}$$
The inner dimensions match ($2 = 2$), producing an outer dimension of $2 \times 1$.

---

## 3. Equivalence via Matrix Multiplication

Expanding the matrix-vector product $Ax$:
$$Ax = \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2 \cdot x + 1 \cdot y \\ 1 \cdot x + (-1) \cdot y \end{bmatrix} = \begin{bmatrix} 2x + y \\ x - y \end{bmatrix}$$

Equating to $b$:
$$\begin{bmatrix} 2x + y \\ x - y \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \end{bmatrix} \iff \begin{cases} 2x + y = 5 \\ x - y = 1 \end{cases}$$
The matrix equation $Ax = b$ is mathematically identical to the original system.

---

## 4. Step-by-Step Algebraic Solution

### 4.1 Elimination Method
Add Equation (1) and Equation (2):
$$(2x + y) + (x - y) = 5 + 1$$
$$(2x + x) + (y - y) = 6$$
$$3x = 6 \implies x = \frac{6}{3} = 2$$

### 4.2 Back-Substitution
Substitute $x = 2$ into Equation (2):
$$2 - y = 1 \implies -y = 1 - 2 = -1 \implies y = 1$$

### 4.3 Solution Vector
$$x^* = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$

---

## 5. Formal Verification of $Ax^* = b$

Compute the matrix-vector product with the computed solution:
$$A x^* = \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$

- **Row 1:** $2(2) + 1(1) = 4 + 1 = 5 = b_1$
- **Row 2:** $1(2) + (-1)(1) = 2 - 1 = 1 = b_2$

$$A x^* = \begin{bmatrix} 5 \\ 1 \end{bmatrix} = b$$
Both scalar equations are satisfied simultaneously. The algebraic solution is formally verified.

---

## 6. Geometric Interpretation on the Cartesian Plane

Express both linear equations in slope-intercept form $y = mx + c$:
1. $2x + y = 5 \iff y = -2x + 5$ (Slope $m_1 = -2$, y-intercept $(0, 5)$)
2. $x - y = 1 \iff y = x - 1$ (Slope $m_2 = 1$, y-intercept $(0, -1)$)

### Intersection Point:
Set $-2x + 5 = x - 1$:
$$6 = 3x \implies x = 2$$
$$y = 2 - 1 = 1$$
The lines intersect at exactly one point in $\mathbb{R}^2$: $(2, 1)$, precisely isomorphic to the solution vector $\begin{bmatrix} 2 \\ 1 \end{bmatrix}$.

---

## 7. The Three Possible Solution Sets for Linear Systems

For any $2 \times 2$ system $Ax = b$:

| Case | Geometric Configuration | Algebraic Condition | Example System | Solution Set |
| :--- | :--- | :--- | :--- | :--- |
| **Case 1: Unique Solution** | Distinct intersecting lines ($m_1 \neq m_2$) | $\det(A) \neq 0$ (Invertible matrix) | $\begin{cases} 2x+y=5 \\ x-y=1 \end{cases}$ | Single point: $(2, 1)$ |
| **Case 2: No Solution (Inconsistent)** | Parallel distinct lines ($m_1 = m_2, c_1 \neq c_2$) | $\det(A) = 0$, $b \notin \text{Col}(A)$ | $\begin{cases} x+y=2 \\ x+y=5 \end{cases}$ | Empty set: $\emptyset$ |
| **Case 3: Infinitely Many Solutions (Dependent)** | Coincident identical lines ($m_1 = m_2, c_1 = c_2$) | $\det(A) = 0$, $b \in \text{Col}(A)$ | $\begin{cases} x+y=3 \\ 2x+2y=6 \end{cases}$ | Line: $\{(x, y) \mid y = 3 - x\}$ |

All calculations and geometric models are verified.
