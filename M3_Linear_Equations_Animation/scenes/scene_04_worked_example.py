"""
Scene 4: Worked Example & Verification
Duration: Synchronized with audio (~74s)
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

class Scene04WorkedExample(Scene):
    def construct(self):
        title = create_title("SOLVING THE SYSTEM & VERIFICATION", "Elimination Method and Rigorous Matrix Substitution")
        self.play(FadeIn(title, shift=DOWN*0.3), run_time=1.0)
        
        # 1. Original system with equation labels
        eq1 = MathTex(r"2x + y = 5", r"\quad \text{--- (1)}", font_size=42)
        eq2 = MathTex(r"x - y = 1",  r"\quad \text{--- (2)}", font_size=42)
        eq1[0][0:2].set_color(COLOR_A)
        eq2[0][0].set_color(COLOR_A)
        
        sys_eqs = VGroup(eq1, eq2).arrange(DOWN, buff=0.4)
        sys_eqs.to_edge(LEFT, buff=1.0).shift(UP * 1.0)
        
        self.play(Write(sys_eqs), run_time=2.0)
        self.wait(1.5)
        
        # 2. Add equations (1) and (2)
        plus_sign = MathTex(r"+", font_size=42, color=LABEL_COLOR).next_to(sys_eqs, LEFT, buff=0.3)
        h_line = Line(start=sys_eqs.get_corner(DL) + LEFT*0.5, end=sys_eqs.get_corner(DR) + RIGHT*0.2, color=LABEL_COLOR)
        
        self.play(FadeIn(plus_sign), Create(h_line), run_time=1.0)
        self.wait(1.0)
        
        # Highlight cancellation of +y and -y
        cancel_y1 = Line(start=eq1[0][2].get_corner(DL), end=eq1[0][3].get_corner(UR), color=RED, stroke_width=3)
        cancel_y2 = Line(start=eq2[0][1].get_corner(DL), end=eq2[0][2].get_corner(UR), color=RED, stroke_width=3)
        self.play(Create(cancel_y1), Create(cancel_y2), run_time=1.2)
        self.wait(1.5)
        
        # Result of addition: 3x = 6 => x = 2
        res_add = MathTex(r"3x = 6 \implies x = 2", font_size=44)
        res_add[0][9:13].set_color(COLOR_X)
        res_add.next_to(h_line, DOWN, buff=0.4).align_to(sys_eqs, LEFT)
        
        self.play(Write(res_add), run_time=1.8)
        self.wait(2.0)
        
        # 3. Back substitution into (2)
        sub_title = Text("Substitute x = 2 into (2):", font="Helvetica", color=LABEL_COLOR).scale(0.42)
        sub_title.next_to(res_add, DOWN, buff=0.6).align_to(res_add, LEFT)
        
        step_sub = MathTex(r"2 - y = 1 \implies -y = -1 \implies y = 1", font_size=42)
        step_sub[0][-4:].set_color(COLOR_X)
        step_sub.next_to(sub_title, DOWN, buff=0.3).align_to(sub_title, LEFT)
        
        self.play(FadeIn(sub_title), Write(step_sub), run_time=2.5)
        self.wait(2.5)
        
        # 4. Prominent Solution Vector Card
        sol_box = RoundedRectangle(corner_radius=0.2, width=3.4, height=2.8, color=COLOR_X, fill_color=BG_SECONDARY, fill_opacity=0.9)
        sol_title = Text("UNIQUE SOLUTION", font="Helvetica", weight=BOLD, color=COLOR_X).scale(0.4)
        sol_vec = MathTex(r"x = \begin{bmatrix} 2 \\ 1 \end{bmatrix}", font_size=52)
        sol_vec[0][0].set_color(COLOR_X)
        sol_vec[0][3:5].set_color(COLOR_X)
        
        sol_content = VGroup(sol_title, sol_vec).arrange(DOWN, buff=0.4)
        sol_box.move_to(RIGHT * 3.5 + UP * 0.2)
        sol_content.move_to(sol_box.get_center())
        sol_card = VGroup(sol_box, sol_content)
        
        self.play(FadeIn(sol_card, shift=LEFT*0.5), run_time=1.8)
        self.wait(3.0)
        
        # 5. Clear screen for Verification Section
        self.play(
            FadeOut(sys_eqs), FadeOut(plus_sign), FadeOut(h_line),
            FadeOut(cancel_y1), FadeOut(cancel_y2),
            FadeOut(res_add), FadeOut(sub_title), FadeOut(step_sub),
            sol_card.animate.shift(LEFT * 5.5 + UP * 0.8).scale(0.85),
            run_time=1.5
        )
        
        # 6. Matrix Verification Ax = b
        verif_title = Text("VERIFICATION VIA MATRIX MULTIPLICATION", font="Helvetica", weight=BOLD, color=COLOR_B).scale(0.45)
        verif_title.shift(RIGHT * 1.5 + UP * 1.8)
        
        step_verif_1 = MathTex(
            r"A \cdot x = \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix}",
            font_size=42
        )
        step_verif_1[0][0].set_color(COLOR_A)
        step_verif_1[0][2].set_color(COLOR_X)
        step_verif_1[0][5:10].set_color(COLOR_A)
        step_verif_1[0][12:14].set_color(COLOR_X)
        step_verif_1.next_to(verif_title, DOWN, buff=0.4).align_to(verif_title, LEFT)
        
        self.play(FadeIn(verif_title), Write(step_verif_1), run_time=2.0)
        self.wait(2.5)
        
        step_verif_2 = MathTex(
            r"= \begin{bmatrix} 2(2) + 1(1) \\ 1(2) - 1(1) \end{bmatrix} = \begin{bmatrix} 4 + 1 \\ 2 - 1 \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}",
            font_size=42
        )
        step_verif_2[0][-4:-2].set_color(COLOR_B)
        step_verif_2.next_to(step_verif_1, DOWN, buff=0.4).align_to(step_verif_1, LEFT)
        
        self.play(Write(step_verif_2), run_time=3.5)
        self.wait(3.0)
        
        badge_verified = create_badge("VERIFIED: Ax = b SATISFIED", COLOR_B)
        badge_verified.next_to(step_verif_2, DOWN, buff=0.6).align_to(step_verif_2, LEFT)
        
        self.play(FadeIn(badge_verified, scale=1.1), run_time=1.5)
        self.wait(3.0)
        
        # Outro Transition
        self.play(
            FadeOut(title),
            FadeOut(sol_card),
            FadeOut(verif_title),
            FadeOut(step_verif_1),
            FadeOut(step_verif_2),
            FadeOut(badge_verified),
            run_time=1.5
        )
        
        # Exact audio synchronization
        sync_wait_to_audio(self, 4, min_extra=0.8)

if __name__ == "__main__":
    pass
