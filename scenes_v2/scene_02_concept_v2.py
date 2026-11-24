"""
Scene 2 (v2): Concept Introduction, Anatomy, and Dimensions
Full beat-by-beat synchronization with audio.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from manim import *
from scenes_v2.v2_utils import *

config.background_color = BG_COLOR
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

class Scene02ConceptV2(Scene):
    def construct(self):
        # ----------------------------------------------------
        # BEAT 1 (s2_b1: ~5.54s) - Header and framing
        # ----------------------------------------------------
        def beat1_action():
            title = Text("ANATOMY OF A LINEAR SYSTEM", font="Helvetica", weight=BOLD, color=TEXT_COLOR).scale(0.75)
            title.to_edge(UP, buff=0.6)
            sub = Text("Deconstructing Equations into Coefficients, Variables & Constants", font="Helvetica", color=LABEL_COLOR).scale(0.42)
            sub.next_to(title, DOWN, buff=0.18)
            accent = Line(LEFT * 4, RIGHT * 4, color=COLOR_A, stroke_width=2).next_to(sub, DOWN, buff=0.2)
            
            self.header = VGroup(title, sub, accent)
            self.play(FadeIn(self.header, shift=DOWN*0.3), run_time=1.8)
            
        play_beat_sync(self, "s2_b1", beat1_action)
        
        # ----------------------------------------------------
        # BEAT 2 (s2_b2: ~6.53s) - Display System in container
        # ----------------------------------------------------
        def beat2_action():
            self.eq1 = MathTex("2", "x", "+", "1", "y", "=", "5", font_size=52)
            self.eq2 = MathTex("1", "x", "-", "1", "y", "=", "1", font_size=52)
            
            eq_group = VGroup(self.eq1, self.eq2).arrange(DOWN, buff=0.6)
            eq_group.shift(UP * 0.4)
            
            card = RoundedRectangle(
                corner_radius=0.2, width=6.2, height=2.4,
                color=LABEL_COLOR, stroke_width=1.5, fill_color=BG_SECONDARY, fill_opacity=0.7
            ).move_to(eq_group.get_center())
            
            self.card = card
            self.eq_group = eq_group
            self.play(Create(card), Write(self.eq1), Write(self.eq2), run_time=2.5)
            
        play_beat_sync(self, "s2_b2", beat2_action)
        
        # ----------------------------------------------------
        # BEAT 3 (s2_b3: ~3.34s) - Variables highlight (Amber)
        # ----------------------------------------------------
        def beat3_action():
            badge_var = create_neon_badge("VARIABLES (x, y)", COLOR_X)
            badge_var.next_to(self.card, LEFT, buff=0.6)
            
            self.play(
                self.eq1[1].animate.set_color(COLOR_X).scale(1.15),
                self.eq1[4].animate.set_color(COLOR_X).scale(1.15),
                self.eq2[1].animate.set_color(COLOR_X).scale(1.15),
                self.eq2[4].animate.set_color(COLOR_X).scale(1.15),
                FadeIn(badge_var, shift=RIGHT*0.3),
                run_time=1.6
            )
            self.badge_var = badge_var
            
        play_beat_sync(self, "s2_b3", beat3_action)
        
        # ----------------------------------------------------
        # BEAT 4 (s2_b4: ~5.88s) - Coefficients highlight (Cyan)
        # ----------------------------------------------------
        def beat4_action():
            badge_coeff = create_neon_badge("COEFFICIENTS (A)", COLOR_A)
            badge_coeff.next_to(self.card, DOWN, buff=0.5).shift(LEFT * 1.5)
            
            self.play(
                self.eq1[0].animate.set_color(COLOR_A).scale(1.15),
                self.eq1[3].animate.set_color(COLOR_A).scale(1.15),
                self.eq2[0].animate.set_color(COLOR_A).scale(1.15),
                self.eq2[3].animate.set_color(COLOR_A).scale(1.15),
                FadeIn(badge_coeff, shift=UP*0.3),
                run_time=2.0
            )
            self.badge_coeff = badge_coeff
            
        play_beat_sync(self, "s2_b4", beat4_action)
        
        # ----------------------------------------------------
        # BEAT 5 (s2_b5: ~4.44s) - Constants highlight (Green)
        # ----------------------------------------------------
        def beat5_action():
            badge_const = create_neon_badge("CONSTANTS (b)", COLOR_B)
            badge_const.next_to(self.card, RIGHT, buff=0.6)
            
            self.play(
                self.eq1[6].animate.set_color(COLOR_B).scale(1.15),
                self.eq2[6].animate.set_color(COLOR_B).scale(1.15),
                FadeIn(badge_const, shift=LEFT*0.3),
                run_time=1.8
            )
            self.badge_const = badge_const
            
        play_beat_sync(self, "s2_b5", beat5_action)
        
        # ----------------------------------------------------
        # BEAT 6 (s2_b6: ~6.43s) - Morph into Ax = b
        # ----------------------------------------------------
        def beat6_action():
            self.play(
                FadeOut(self.card),
                FadeOut(self.eq_group),
                FadeOut(self.badge_var),
                FadeOut(self.badge_coeff),
                FadeOut(self.badge_const),
                run_time=1.0
            )
            
            gen_eq = MathTex("A", r"\mathbf{x}", "=", r"\mathbf{b}", font_size=76)
            gen_eq[0].set_color(COLOR_A)
            gen_eq[1].set_color(COLOR_X)
            gen_eq[3].set_color(COLOR_B)
            gen_eq.shift(UP * 1.0)
            
            glow_box = RoundedRectangle(
                corner_radius=0.25, width=4.5, height=2.0,
                color=COLOR_A, stroke_width=2.5, fill_color=BG_SECONDARY, fill_opacity=0.85
            ).move_to(gen_eq.get_center())
            
            self.gen_group = VGroup(glow_box, gen_eq)
            self.play(
                FadeIn(glow_box, scale=1.1),
                Write(gen_eq),
                run_time=2.2
            )
            self.play(
                Flash(gen_eq[0], color=COLOR_A),
                Flash(gen_eq[1], color=COLOR_X),
                Flash(gen_eq[3], color=COLOR_B),
                run_time=1.5
            )
            
        play_beat_sync(self, "s2_b6", beat6_action)
        
        # ----------------------------------------------------
        # BEAT 7 (s2_b7: ~5.26s) - Component Cards (A, x, b)
        # ----------------------------------------------------
        def beat7_action():
            c_A = VGroup(
                MathTex("A", font_size=42, color=COLOR_A),
                Text("Coefficient Matrix", font="Helvetica", weight=BOLD, color=TEXT_COLOR).scale(0.36),
                Text("Encodes system equations", font="Helvetica", color=LABEL_COLOR).scale(0.30)
            ).arrange(DOWN, buff=0.15)
            
            c_x = VGroup(
                MathTex(r"\mathbf{x}", font_size=42, color=COLOR_X),
                Text("Variable Vector", font="Helvetica", weight=BOLD, color=TEXT_COLOR).scale(0.36),
                Text("Column vector of unknowns", font="Helvetica", color=LABEL_COLOR).scale(0.30)
            ).arrange(DOWN, buff=0.15)
            
            c_b = VGroup(
                MathTex(r"\mathbf{b}", font_size=42, color=COLOR_B),
                Text("Constant Vector", font="Helvetica", weight=BOLD, color=TEXT_COLOR).scale(0.36),
                Text("Right-hand target values", font="Helvetica", color=LABEL_COLOR).scale(0.30)
            ).arrange(DOWN, buff=0.15)
            
            cards = VGroup(c_A, c_x, c_b).arrange(RIGHT, buff=0.8)
            cards.next_to(self.gen_group, DOWN, buff=0.6)
            
            self.cards = cards
            self.play(FadeIn(cards, shift=UP*0.3), run_time=2.0)
            
        play_beat_sync(self, "s2_b7", beat7_action)
        
        # ----------------------------------------------------
        # BEAT 8 (s2_b8: ~9.70s) - Dimensional Puzzle Lock
        # ----------------------------------------------------
        def beat8_action():
            dim_formula = MathTex(
                r"(m \times n)", r"\times", r"(n \times 1)", r"=", r"(m \times 1)",
                font_size=44
            )
            dim_formula[0].set_color(COLOR_A)
            dim_formula[2].set_color(COLOR_X)
            dim_formula[4].set_color(COLOR_B)
            dim_formula.next_to(self.cards, DOWN, buff=0.6)
            
            # Connect inner dimensions
            inner_link = MathTex(r"\text{Inner dimensions match: } n = n", font_size=32, color=COLOR_HIGHLIGHT)
            inner_link.next_to(dim_formula, DOWN, buff=0.3)
            
            self.play(Write(dim_formula), run_time=2.2)
            self.play(FadeIn(inner_link, shift=UP*0.1), run_time=1.8)
            self.wait(2.5)
            
            # Outro Transition
            self.play(
                FadeOut(self.header),
                FadeOut(self.gen_group),
                FadeOut(self.cards),
                FadeOut(dim_formula),
                FadeOut(inner_link),
                run_time=1.8
            )
            
        play_beat_sync(self, "s2_b8", beat8_action)

if __name__ == "__main__":
    pass
