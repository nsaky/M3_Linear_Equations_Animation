"""
Scene 2: Concept Introduction
Duration: Synchronized with audio (~40s)
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

class Scene02Concept(Scene):
    def construct(self):
        # 1. Title
        title = create_title("UNDERSTANDING LINEAR SYSTEMS", "Components and the Matrix Equation Ax = b")
        self.play(FadeIn(title, shift=DOWN*0.3), run_time=1.0)
        
        # 2. Display System with Highlighted Colors
        eq1 = MathTex("2", "x", "+", "1", "y", "=", "5", font_size=46)
        eq1[0].set_color(COLOR_A)
        eq1[1].set_color(COLOR_X)
        eq1[3].set_color(COLOR_A)
        eq1[4].set_color(COLOR_X)
        eq1[6].set_color(COLOR_B)
        
        eq2 = MathTex("1", "x", "-", "1", "y", "=", "1", font_size=46)
        eq2[0].set_color(COLOR_A)
        eq2[1].set_color(COLOR_X)
        eq2[3].set_color(COLOR_A)
        eq2[4].set_color(COLOR_X)
        eq2[6].set_color(COLOR_B)
        
        sys_group = VGroup(eq1, eq2).arrange(DOWN, buff=0.6)
        sys_group.shift(UP * 0.8)
        
        self.play(Write(sys_group), run_time=2.0)
        self.wait(1.5)
        
        # 3. Component Annotation Badges
        badge_coeff = create_badge("COEFFICIENTS (A)", COLOR_A)
        badge_var   = create_badge("VARIABLES (x)", COLOR_X)
        badge_const = create_badge("CONSTANTS (b)", COLOR_B)
        
        badges = VGroup(badge_coeff, badge_var, badge_const).arrange(RIGHT, buff=0.6)
        badges.next_to(sys_group, DOWN, buff=0.8)
        
        self.play(FadeIn(badges, shift=UP*0.3), run_time=1.8)
        self.wait(2.5)
        
        # 4. Transition to General Form Ax = b
        self.play(
            FadeOut(sys_group),
            FadeOut(badges),
            run_time=1.2
        )
        
        gen_eq = MathTex("A", "x", "=", "b", font_size=72)
        gen_eq[0].set_color(COLOR_A)
        gen_eq[1].set_color(COLOR_X)
        gen_eq[3].set_color(COLOR_B)
        gen_eq.shift(UP * 1.0)
        
        self.play(Write(gen_eq), run_time=1.5)
        self.wait(1.5)
        
        # 5. Component breakdown cards
        card_A = VGroup(
            MathTex("A", font_size=48, color=COLOR_A),
            Text("Coefficient Matrix", font="Helvetica", color=TEXT_COLOR).scale(0.45),
            Text("Dimension: m × n", font="Helvetica", color=COLOR_A).scale(0.4)
        ).arrange(DOWN, buff=0.2)
        
        card_x = VGroup(
            MathTex("x", font_size=48, color=COLOR_X),
            Text("Variable Vector", font="Helvetica", color=TEXT_COLOR).scale(0.45),
            Text("Dimension: n × 1", font="Helvetica", color=COLOR_X).scale(0.4)
        ).arrange(DOWN, buff=0.2)
        
        card_b = VGroup(
            MathTex("b", font_size=48, color=COLOR_B),
            Text("Constant Vector", font="Helvetica", color=TEXT_COLOR).scale(0.45),
            Text("Dimension: m × 1", font="Helvetica", color=COLOR_B).scale(0.4)
        ).arrange(DOWN, buff=0.2)
        
        cards = VGroup(card_A, card_x, card_b).arrange(RIGHT, buff=1.2)
        cards.next_to(gen_eq, DOWN, buff=1.0)
        
        self.play(FadeIn(card_A, shift=UP*0.3), run_time=1.2)
        self.wait(1.0)
        self.play(FadeIn(card_x, shift=UP*0.3), run_time=1.2)
        self.wait(1.0)
        self.play(FadeIn(card_b, shift=UP*0.3), run_time=1.2)
        self.wait(2.5)
        
        # 6. Dimensions matching summary
        dim_summary = MathTex(
            r"(m \times n) \times (n \times 1) = (m \times 1)",
            font_size=40,
            color=LABEL_COLOR
        )
        dim_summary.next_to(cards, DOWN, buff=0.6)
        
        self.play(Write(dim_summary), run_time=1.5)
        self.wait(2.0)
        
        # Outro Transition
        self.play(
            FadeOut(title),
            FadeOut(gen_eq),
            FadeOut(cards),
            FadeOut(dim_summary),
            run_time=1.5
        )
        
        # Exact audio synchronization
        sync_wait_to_audio(self, 2, min_extra=0.8)

if __name__ == "__main__":
    pass
