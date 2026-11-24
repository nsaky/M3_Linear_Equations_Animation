"""
Scene 6 (v2): Summary & Academic Assessment Credits
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

class Scene06SummaryV2(Scene):
    def construct(self):
        # ----------------------------------------------------
        # BEAT 1 (s6_b1: ~5.88s) - Header & Ax = b Banner
        # ----------------------------------------------------
        def beat1_action():
            title = Text("SUMMARY & MATHEMATICAL SYNTHESIS", font="Helvetica", weight=BOLD, color=TEXT_COLOR).scale(0.72)
            title.to_edge(UP, buff=0.6)
            sub = Text("Unifying Equations, Matrix Representations, and Geometry", font="Helvetica", color=LABEL_COLOR).scale(0.40)
            sub.next_to(title, DOWN, buff=0.18)
            accent = Line(LEFT * 4.2, RIGHT * 4.2, color=COLOR_A, stroke_width=2).next_to(sub, DOWN, buff=0.2)
            
            self.header = VGroup(title, sub, accent)
            
            banner_bg = RoundedRectangle(
                corner_radius=0.2, width=5.5, height=1.6,
                color=COLOR_A, stroke_width=2.5, fill_color=BG_SECONDARY, fill_opacity=0.9
            ).shift(UP * 0.8)
            
            banner_math = MathTex(r"A \mathbf{x} = \mathbf{b}", font_size=58)
            banner_math[0][0].set_color(COLOR_A)
            banner_math[0][1].set_color(COLOR_X)
            banner_math[0][3].set_color(COLOR_B)
            banner_math.move_to(banner_bg.get_center())
            
            self.banner = VGroup(banner_bg, banner_math)
            self.play(FadeIn(self.header, shift=DOWN*0.3), FadeIn(self.banner, scale=1.1), run_time=2.2)
            
        play_beat_sync(self, "s6_b1", beat1_action)
        
        # ----------------------------------------------------
        # BEAT 2 (s6_b2: ~6.34s) - Three Takeaway Pillars
        # ----------------------------------------------------
        def beat2_action():
            p_A = VGroup(
                MathTex("A", font_size=44, color=COLOR_A),
                Text("System Structure", font="Helvetica", weight=BOLD, color=COLOR_A).scale(0.36),
                Text("Coefficient matrix", font="Helvetica", color=TEXT_COLOR).scale(0.30)
            ).arrange(DOWN, buff=0.15)
            
            p_x = VGroup(
                MathTex(r"\mathbf{x}", font_size=44, color=COLOR_X),
                Text("Unknown Variables", font="Helvetica", weight=BOLD, color=COLOR_X).scale(0.36),
                Text("Column vector [x, y]^T", font="Helvetica", color=TEXT_COLOR).scale(0.30)
            ).arrange(DOWN, buff=0.15)
            
            p_b = VGroup(
                MathTex(r"\mathbf{b}", font_size=44, color=COLOR_B),
                Text("Target Constants", font="Helvetica", weight=BOLD, color=COLOR_B).scale(0.36),
                Text("Right-hand constraints", font="Helvetica", color=TEXT_COLOR).scale(0.30)
            ).arrange(DOWN, buff=0.15)
            
            pillars = VGroup(p_A, p_x, p_b).arrange(RIGHT, buff=0.85)
            pillars.next_to(self.banner, DOWN, buff=0.6)
            
            self.pillars = pillars
            self.play(FadeIn(pillars, shift=UP*0.3), run_time=2.2)
            
        play_beat_sync(self, "s6_b2", beat2_action)
        
        # ----------------------------------------------------
        # BEAT 3 (s6_b3: ~6.84s) - Unified Mathematical Bridge
        # ----------------------------------------------------
        def beat3_action():
            bridge = MathTex(
                r"\text{Equations} \quad \Longleftrightarrow \quad A\mathbf{x}=\mathbf{b} \quad \Longleftrightarrow \quad \text{Geometry}",
                font_size=38, color=TEXT_COLOR
            )
            bridge.next_to(self.pillars, DOWN, buff=0.6)
            
            self.bridge = bridge
            self.play(Write(bridge), Flash(bridge, color=COLOR_X), run_time=2.2)
            self.wait(1.5)
            
            self.play(
                FadeOut(self.header),
                FadeOut(self.banner),
                FadeOut(self.pillars),
                FadeOut(bridge),
                run_time=1.2
            )
            
        play_beat_sync(self, "s6_b3", beat3_action)
        
        # ----------------------------------------------------
        # BEAT 4 (s6_b4: ~10.85s) - Full Academic Credits Card
        # ----------------------------------------------------
        def beat4_action():
            cred_title = Text("ACADEMIC ASSESSMENT CREDITS", font="Helvetica", weight=BOLD, color=COLOR_A).scale(0.55)
            cred_title.to_edge(UP, buff=0.8)
            
            cred_items = [
                ("Course:", "M3 — Linear Algebra and Calculus (Internal Assessment)"),
                ("Topic:", "Systems of Linear Equations: From Equations to Matrices (Ax = b)"),
                ("Student Name:", f"{STUDENT_NAME}"),
                ("Student ID:", f"{STUDENT_ID}"),
                ("Animation Framework:", "Python 3.13 + Manim Community Edition v0.22"),
                ("Mathematical Typesetting:", "LaTeX (TinyTeX, dvisvgm, MathTex)"),
                ("Narration Engine:", "Microsoft Edge Neural TTS (en-IN-PrabhatNeural)"),
                ("AI Tool Disclosure:", "AI tools used for script refinement, visual motion design, and narration"),
                ("References:", "Standard Linear Algebra (Gilbert Strang, David Lay)"),
            ]
            
            rows = []
            for label, val in cred_items:
                l_m = Text(label, font="Helvetica", weight=BOLD, color=LABEL_COLOR).scale(0.35)
                v_m = Text(val, font="Helvetica", color=TEXT_COLOR).scale(0.35)
                row = VGroup(l_m, v_m).arrange(RIGHT, buff=0.25)
                rows.append(row)
                
            cred_group = VGroup(*rows).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
            cred_group.next_to(cred_title, DOWN, buff=0.45)
            
            card_bg = RoundedRectangle(
                corner_radius=0.2, width=cred_group.width + 0.8, height=cred_group.height + 1.2,
                color=COLOR_A, stroke_width=1.5, fill_color=BG_SECONDARY, fill_opacity=0.9
            ).move_to(VGroup(cred_title, cred_group).get_center())
            
            credits_card = VGroup(card_bg, cred_title, cred_group)
            
            self.play(FadeIn(credits_card, shift=UP*0.3), run_time=2.2)
            self.wait(4.5)
            self.play(FadeOut(credits_card), run_time=2.0)
            
        play_beat_sync(self, "s6_b4", beat4_action)

if __name__ == "__main__":
    pass
