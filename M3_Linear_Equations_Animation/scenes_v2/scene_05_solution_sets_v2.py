"""
Scene 5 (v2): Geometric Interpretation & The Three Solution Sets
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

class Scene05SolutionSetsV2(Scene):
    def construct(self):
        # ----------------------------------------------------
        # BEAT 1 (s5_b1: ~5.69s) - Header & Cartesian Axes
        # ----------------------------------------------------
        def beat1_action():
            title = Text("GEOMETRIC INTERPRETATION & SOLUTION SETS", font="Helvetica", weight=BOLD, color=TEXT_COLOR).scale(0.70)
            title.to_edge(UP, buff=0.6)
            sub = Text("Intersection of Lines and the Three Fundamental Geometric Realities", font="Helvetica", color=LABEL_COLOR).scale(0.40)
            sub.next_to(title, DOWN, buff=0.18)
            accent = Line(LEFT * 4.4, RIGHT * 4.4, color=COLOR_A, stroke_width=2).next_to(sub, DOWN, buff=0.2)
            
            self.header = VGroup(title, sub, accent)
            
            axes = Axes(
                x_range=[-1, 5, 1],
                y_range=[-3, 6, 1],
                x_length=6.2,
                y_length=5.0,
                axis_config={"color": LABEL_COLOR, "stroke_width": 2},
                tips=True
            )
            axes.shift(LEFT * 2.8 + DOWN * 0.4)
            
            self.axes = axes
            self.play(FadeIn(self.header, shift=DOWN*0.3), Create(axes), run_time=2.2)
            
        play_beat_sync(self, "s5_b1", beat1_action)
        
        # ----------------------------------------------------
        # BEAT 2 (s5_b2: ~7.22s) - Plot Both Lines Dynamically
        # ----------------------------------------------------
        def beat2_action():
            # Line 1: y = 5 - 2x
            line1 = self.axes.plot(lambda x: 5 - 2*x, x_range=[-0.4, 3.8], color=COLOR_A, stroke_width=4.0)
            lbl1 = MathTex(r"2x + y = 5", font_size=32, color=COLOR_A)
            lbl1.next_to(line1.point_from_proportion(0.18), RIGHT, buff=0.15)
            
            # Line 2: y = x - 1
            line2 = self.axes.plot(lambda x: x - 1, x_range=[-0.5, 4.5], color=COLOR_X, stroke_width=4.0)
            lbl2 = MathTex(r"x - y = 1", font_size=32, color=COLOR_X)
            lbl2.next_to(line2.point_from_proportion(0.82), UP, buff=0.15)
            
            self.line1 = line1
            self.line2 = line2
            self.lbl1 = lbl1
            self.lbl2 = lbl2
            
            self.play(Create(line1), FadeIn(lbl1), run_time=1.8)
            self.play(Create(line2), FadeIn(lbl2), run_time=1.8)
            
        play_beat_sync(self, "s5_b2", beat2_action)
        
        # ----------------------------------------------------
        # BEAT 3 (s5_b3: ~6.60s) - Target radar pulse at (2, 1)
        # ----------------------------------------------------
        def beat3_action():
            pt_coords = self.axes.c2p(2, 1)
            dot = Dot(point=pt_coords, color=COLOR_POINT, radius=0.14)
            
            ring_pulse = Circle(radius=0.4, color=COLOR_POINT, stroke_width=2.5).move_to(pt_coords)
            lbl_pt = MathTex(r"(2, 1)", font_size=36, color=COLOR_POINT).next_to(dot, UR, buff=0.2)
            
            self.dot_group = VGroup(dot, ring_pulse, lbl_pt)
            self.play(FadeIn(dot, scale=1.5), Create(ring_pulse), Write(lbl_pt), run_time=1.8)
            self.play(ring_pulse.animate.scale(2.0).set_opacity(0), Flash(dot, color=COLOR_POINT), run_time=1.5)
            
        play_beat_sync(self, "s5_b3", beat3_action)
        
        # ----------------------------------------------------
        # BEAT 4 (s5_b4: ~6.24s) - Connect point (2, 1) to vector [2, 1]
        # ----------------------------------------------------
        def beat4_action():
            bridge_box = RoundedRectangle(
                corner_radius=0.2, width=4.5, height=3.0,
                color=COLOR_B, stroke_width=2.0, fill_color=BG_SECONDARY, fill_opacity=0.9
            ).shift(RIGHT * 3.4 + DOWN * 0.4)
            
            b_title = Text("GEOMETRIC ISOMORPHISM", font="Helvetica", weight=BOLD, color=COLOR_B).scale(0.36)
            b_pt = MathTex(r"\text{Intersection Point: } (2, 1)", font_size=34, color=COLOR_POINT)
            b_arrow = MathTex(r"\Updownarrow", font_size=36, color=LABEL_COLOR)
            b_vec = MathTex(r"\text{Solution Vector: } \mathbf{x} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}", font_size=34, color=COLOR_X)
            
            bridge_content = VGroup(b_title, b_pt, b_arrow, b_vec).arrange(DOWN, buff=0.22)
            bridge_content.move_to(bridge_box.get_center())
            
            self.bridge_group = VGroup(bridge_box, bridge_content)
            self.play(FadeIn(self.bridge_group, shift=LEFT*0.3), run_time=2.2)
            
        play_beat_sync(self, "s5_b4", beat4_action)
        
        # ----------------------------------------------------
        # BEAT 5 (s5_b5: ~4.87s) - Transition to Three Cases
        # ----------------------------------------------------
        def beat5_action():
            self.play(
                FadeOut(self.axes),
                FadeOut(self.line1),
                FadeOut(self.line2),
                FadeOut(self.lbl1),
                FadeOut(self.lbl2),
                FadeOut(self.dot_group),
                FadeOut(self.bridge_group),
                run_time=1.2
            )
            
            subtitle_cases = Text("THE THREE POSSIBLE SOLUTION-SET OUTCOMES", font="Helvetica", weight=BOLD, color=COLOR_X).scale(0.50)
            subtitle_cases.next_to(self.header[2], DOWN, buff=0.3)
            self.play(FadeIn(subtitle_cases, shift=DOWN*0.2), run_time=1.2)
            self.subtitle_cases = subtitle_cases
            
        play_beat_sync(self, "s5_b5", beat5_action)
        
        # ----------------------------------------------------
        # BEAT 6 (s5_b6: ~9.05s) - Three Triptych Panels
        # ----------------------------------------------------
        def beat6_action():
            # Panel 1: Unique Solution
            p1_bg = RoundedRectangle(corner_radius=0.18, width=3.8, height=3.6, color=COLOR_POINT, fill_color=BG_SECONDARY, fill_opacity=0.9)
            p1_t = Text("ONE SOLUTION", font="Helvetica", weight=BOLD, color=COLOR_POINT).scale(0.38)
            p1_d = Text("Intersecting Lines", font="Helvetica", color=TEXT_COLOR).scale(0.32)
            p1_m = MathTex(r"\begin{cases} 2x+y=5 \\ x-y=1 \end{cases}", font_size=28, color=LABEL_COLOR)
            p1_sub = Text("Unique point (2, 1)", font="Helvetica", color=COLOR_POINT).scale(0.30)
            c1 = VGroup(p1_t, p1_d, p1_m, p1_sub).arrange(DOWN, buff=0.22).move_to(p1_bg.get_center())
            panel1 = VGroup(p1_bg, c1)
            
            # Panel 2: No Solution
            p2_bg = RoundedRectangle(corner_radius=0.18, width=3.8, height=3.6, color=COLOR_HIGHLIGHT, fill_color=BG_SECONDARY, fill_opacity=0.9)
            p2_t = Text("NO SOLUTION", font="Helvetica", weight=BOLD, color=COLOR_HIGHLIGHT).scale(0.38)
            p2_d = Text("Parallel Lines", font="Helvetica", color=TEXT_COLOR).scale(0.32)
            p2_m = MathTex(r"\begin{cases} x+y=2 \\ x+y=5 \end{cases}", font_size=28, color=LABEL_COLOR)
            p2_sub = Text("Never meet (Empty set)", font="Helvetica", color=COLOR_HIGHLIGHT).scale(0.30)
            c2 = VGroup(p2_t, p2_d, p2_m, p2_sub).arrange(DOWN, buff=0.22).move_to(p2_bg.get_center())
            panel2 = VGroup(p2_bg, c2)
            
            # Panel 3: Infinitely Many
            p3_bg = RoundedRectangle(corner_radius=0.18, width=3.8, height=3.6, color=COLOR_A, fill_color=BG_SECONDARY, fill_opacity=0.9)
            p3_t = Text("INFINITELY MANY", font="Helvetica", weight=BOLD, color=COLOR_A).scale(0.38)
            p3_d = Text("Coincident Lines", font="Helvetica", color=TEXT_COLOR).scale(0.32)
            p3_m = MathTex(r"\begin{cases} x+y=3 \\ 2x+2y=6 \end{cases}", font_size=28, color=LABEL_COLOR)
            p3_sub = Text("Overlap everywhere", font="Helvetica", color=COLOR_A).scale(0.30)
            c3 = VGroup(p3_t, p3_d, p3_m, p3_sub).arrange(DOWN, buff=0.22).move_to(p3_bg.get_center())
            panel3 = VGroup(p3_bg, c3)
            
            triptych = VGroup(panel1, panel2, panel3).arrange(RIGHT, buff=0.55).shift(DOWN * 0.4)
            
            self.play(FadeIn(panel1, shift=UP*0.3), run_time=1.2)
            self.play(FadeIn(panel2, shift=UP*0.3), run_time=1.2)
            self.play(FadeIn(panel3, shift=UP*0.3), run_time=1.2)
            self.wait(2.5)
            
            self.play(
                FadeOut(self.header),
                FadeOut(self.subtitle_cases),
                FadeOut(triptych),
                run_time=1.5
            )
            
        play_beat_sync(self, "s5_b6", beat6_action)

if __name__ == "__main__":
    pass
