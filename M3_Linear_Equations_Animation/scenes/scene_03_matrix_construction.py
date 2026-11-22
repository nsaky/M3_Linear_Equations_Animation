"""
Scene 3: Visual Intuition & Matrix Construction
Duration: Synchronized with audio (~52s)
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from manim import *
from config import *

config.background_color = BG_COLOR
config.pixel_width = PIXEL_WIDTH
config.pixel_height = PIXEL_HEIGHT
config.frame_rate = TARGET_FPS

class Scene03MatrixConstruction(Scene):
    def construct(self):
        title = create_title("CONSTRUCTING THE MATRIX EQUATION", "Extracting Coefficients and Expanding Matrix Multiplication")
        self.play(FadeIn(title, shift=DOWN*0.3), run_time=1.0)
        
        # 1. Left side: The original equations
        eq1 = MathTex("2", "x", "+", "1", "y", "=", "5", font_size=42)
        eq1[0].set_color(COLOR_A)
        eq1[3].set_color(COLOR_A)
        eq1[6].set_color(COLOR_B)
        
        eq2 = MathTex("1", "x", "-", "1", "y", "=", "1", font_size=42)
        eq2[0].set_color(COLOR_A)
        eq2[3].set_color(COLOR_A)
        eq2[6].set_color(COLOR_B)
        
        eqs = VGroup(eq1, eq2).arrange(DOWN, buff=0.6)
        eqs.to_edge(LEFT, buff=1.2).shift(UP * 0.4)
        
        box_eqs = SurroundingRectangle(eqs, color=LABEL_COLOR, buff=0.3, corner_radius=0.1)
        lbl_eqs = Text("Original System", font="Helvetica", color=LABEL_COLOR).scale(0.38)
        lbl_eqs.next_to(box_eqs, UP, buff=0.15)
        
        self.play(Write(eqs), Create(box_eqs), FadeIn(lbl_eqs), run_time=2.0)
        self.wait(1.5)
        
        # 2. Extract Row 1 & Row 2 coefficients into Matrix A
        mat_A_full = MathTex(r"A = \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix}", font_size=48)
        mat_A_full[0][0].set_color(COLOR_A)
        mat_A_full[0][3:8].set_color(COLOR_A)
        mat_A_full.shift(RIGHT * 1.5 + UP * 1.2)
        
        arrow_row1 = Arrow(start=eq1.get_right(), end=mat_A_full.get_left() + UP*0.3, color=COLOR_A, stroke_width=2.5)
        self.play(GrowArrow(arrow_row1), run_time=1.2)
        self.wait(0.8)
        
        arrow_row2 = Arrow(start=eq2.get_right(), end=mat_A_full.get_left() + DOWN*0.3, color=COLOR_A, stroke_width=2.5)
        self.play(FadeIn(mat_A_full), GrowArrow(arrow_row2), run_time=1.8)
        self.wait(2.0)
        
        self.play(FadeOut(arrow_row1), FadeOut(arrow_row2), run_time=0.8)
        
        # 3. Form vectors x and b
        vec_x = MathTex(r"x = \begin{bmatrix} x \\ y \end{bmatrix}", font_size=48)
        vec_x[0][0].set_color(COLOR_X)
        vec_x[0][3:5].set_color(COLOR_X)
        
        vec_b = MathTex(r"b = \begin{bmatrix} 5 \\ 1 \end{bmatrix}", font_size=48)
        vec_b[0][0].set_color(COLOR_B)
        vec_b[0][3:5].set_color(COLOR_B)
        
        vec_group = VGroup(vec_x, vec_b).arrange(RIGHT, buff=0.8)
        vec_group.next_to(mat_A_full, DOWN, buff=0.6)
        
        self.play(FadeIn(vec_x, shift=UP*0.2), run_time=1.2)
        self.wait(0.8)
        self.play(FadeIn(vec_b, shift=UP*0.2), run_time=1.2)
        self.wait(2.5)
        
        # 4. Clean and Assemble into Complete Ax = b Matrix Equation
        self.play(
            FadeOut(eqs), FadeOut(box_eqs), FadeOut(lbl_eqs),
            FadeOut(mat_A_full), FadeOut(vec_group),
            run_time=1.2
        )
        
        full_matrix_eq = MathTex(
            r"\begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix}",
            r"\begin{bmatrix} x \\ y \end{bmatrix}",
            r"=",
            r"\begin{bmatrix} 5 \\ 1 \end{bmatrix}",
            font_size=46
        )
        full_matrix_eq[0].set_color(COLOR_A)
        full_matrix_eq[1].set_color(COLOR_X)
        full_matrix_eq[3].set_color(COLOR_B)
        full_matrix_eq.shift(UP * 1.0)
        
        lbl_Ax_b = MathTex(r"A \cdot x = b", font_size=42, color=LABEL_COLOR).next_to(full_matrix_eq, UP, buff=0.4)
        
        self.play(Write(full_matrix_eq), FadeIn(lbl_Ax_b), run_time=2.0)
        self.wait(2.5)
        
        # 5. Expand Matrix Multiplication
        mult_expansion = MathTex(
            r"\begin{bmatrix} 2(x) + 1(y) \\ 1(x) - 1(y) \end{bmatrix} = \begin{bmatrix} 2x + y \\ x - y \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}",
            font_size=40
        )
        mult_expansion[0][1:13].set_color(COLOR_A)
        mult_expansion[0][17:23].set_color(TEXT_COLOR)
        mult_expansion[0][27:29].set_color(COLOR_B)
        mult_expansion.next_to(full_matrix_eq, DOWN, buff=0.8)
        
        self.play(Write(mult_expansion), run_time=3.5)
        self.wait(3.5)
        
        # 6. Row correspondence highlight callouts
        callout_r1 = create_badge("Row 1 reproduces 2x + y = 5", COLOR_A)
        callout_r2 = create_badge("Row 2 reproduces x - y = 1", COLOR_B)
        callouts = VGroup(callout_r1, callout_r2).arrange(RIGHT, buff=0.8)
        callouts.next_to(mult_expansion, DOWN, buff=0.6)
        
        self.play(FadeIn(callouts, shift=UP*0.2), run_time=1.5)
        self.wait(3.0)
        
        # Outro Transition
        self.play(
            FadeOut(title),
            FadeOut(full_matrix_eq),
            FadeOut(lbl_Ax_b),
            FadeOut(mult_expansion),
            FadeOut(callouts),
            run_time=1.5
        )
        
        # Exact audio synchronization
        sync_wait_to_audio(self, 3, min_extra=0.8)

if __name__ == "__main__":
    pass
