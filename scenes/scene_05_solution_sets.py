"""
Scene 5: Geometric Interpretation & Solution Sets
Duration: Synchronized with audio (32.86s + pad -> ~34s)
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

class Scene05SolutionSets(Scene):
    def construct(self):
        title = create_title("GEOMETRIC INTERPRETATION & SOLUTION SETS", "From Coordinate Intersections to the Three Possible Outcomes")
        self.play(FadeIn(title, shift=DOWN*0.3), run_time=1.0)
        
        # 1. Coordinate Axes
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-3, 6, 1],
            x_length=6.0,
            y_length=5.0,
            axis_config={"color": LABEL_COLOR, "stroke_width": 2},
            tips=True
        )
        axes.shift(LEFT * 2.8 + DOWN * 0.4)
        
        self.play(Create(axes), run_time=1.5)
        
        # 2. Plot Lines: y = 5 - 2x and y = x - 1
        line1 = axes.plot(lambda x: 5 - 2*x, x_range=[-0.4, 3.8], color=COLOR_LINE_1, stroke_width=3.5)
        label_line1 = MathTex(r"2x + y = 5", font_size=30, color=COLOR_LINE_1).next_to(line1.point_from_proportion(0.2), RIGHT, buff=0.1)
        
        line2 = axes.plot(lambda x: x - 1, x_range=[-0.5, 4.5], color=COLOR_LINE_2, stroke_width=3.5)
        label_line2 = MathTex(r"x - y = 1", font_size=30, color=COLOR_LINE_2).next_to(line2.point_from_proportion(0.85), UP, buff=0.1)
        
        self.play(Create(line1), FadeIn(label_line1), run_time=1.5)
        self.play(Create(line2), FadeIn(label_line2), run_time=1.5)
        self.wait(1.0)
        
        # 3. Intersection Point at (2, 1)
        pt_coords = axes.c2p(2, 1)
        dot = Dot(point=pt_coords, color=COLOR_POINT, radius=0.12)
        dot_pulse = Circle(radius=0.3, color=COLOR_POINT, stroke_width=2).move_to(pt_coords)
        
        label_pt = MathTex(r"(2, 1)", font_size=34, color=COLOR_POINT).next_to(dot, UR, buff=0.2)
        
        self.play(FadeIn(dot, scale=1.5), Create(dot_pulse), Write(label_pt), run_time=1.5)
        self.wait(1.5)
        
        # Connect to solution vector card on right
        bridge_card = VGroup(
            Text("GEOMETRIC INTERSECTION", font="Helvetica", weight=BOLD, color=COLOR_POINT).scale(0.38),
            MathTex(r"(x, y) = (2, 1)", font_size=36, color=TEXT_COLOR),
            MathTex(r"\Updownarrow", font_size=34, color=LABEL_COLOR),
            MathTex(r"x = \begin{bmatrix} 2 \\ 1 \end{bmatrix}", font_size=42, color=COLOR_X)
        ).arrange(DOWN, buff=0.25)
        bridge_card.shift(RIGHT * 3.5 + DOWN * 0.4)
        
        self.play(FadeIn(bridge_card, shift=LEFT*0.3), run_time=1.5)
        self.wait(2.5)
        
        # 4. Transition to 3 Possible Outcomes Triptych
        self.play(
            FadeOut(axes), FadeOut(line1), FadeOut(line2),
            FadeOut(label_line1), FadeOut(label_line2),
            FadeOut(dot), FadeOut(dot_pulse), FadeOut(label_pt),
            FadeOut(bridge_card),
            run_time=1.2
        )
        
        # Three Case Panels
        # Case 1: One Solution
        box1 = RoundedRectangle(corner_radius=0.15, width=3.8, height=3.8, color=COLOR_POINT, fill_color=BG_SECONDARY, fill_opacity=0.85)
        t1 = Text("ONE SOLUTION", font="Helvetica", weight=BOLD, color=COLOR_POINT).scale(0.38)
        desc1 = Text("Intersecting Lines", font="Helvetica", color=TEXT_COLOR).scale(0.32)
        eq_ex1 = MathTex(r"\begin{cases} 2x+y=5 \\ x-y=1 \end{cases}", font_size=28, color=LABEL_COLOR)
        c1_group = VGroup(t1, desc1, eq_ex1).arrange(DOWN, buff=0.25)
        panel1 = VGroup(box1, c1_group)
        c1_group.move_to(box1.get_center())
        
        # Case 2: No Solution
        box2 = RoundedRectangle(corner_radius=0.15, width=3.8, height=3.8, color=RED, fill_color=BG_SECONDARY, fill_opacity=0.85)
        t2 = Text("NO SOLUTION", font="Helvetica", weight=BOLD, color=RED).scale(0.38)
        desc2 = Text("Parallel Lines", font="Helvetica", color=TEXT_COLOR).scale(0.32)
        eq_ex2 = MathTex(r"\begin{cases} x+y=2 \\ x+y=5 \end{cases}", font_size=28, color=LABEL_COLOR)
        c2_group = VGroup(t2, desc2, eq_ex2).arrange(DOWN, buff=0.25)
        panel2 = VGroup(box2, c2_group)
        c2_group.move_to(box2.get_center())
        
        # Case 3: Infinitely Many Solutions
        box3 = RoundedRectangle(corner_radius=0.15, width=3.8, height=3.8, color=COLOR_A, fill_color=BG_SECONDARY, fill_opacity=0.85)
        t3 = Text("INFINITELY MANY", font="Helvetica", weight=BOLD, color=COLOR_A).scale(0.38)
        desc3 = Text("Coincident Lines", font="Helvetica", color=TEXT_COLOR).scale(0.32)
        eq_ex3 = MathTex(r"\begin{cases} x+y=3 \\ 2x+2y=6 \end{cases}", font_size=28, color=LABEL_COLOR)
        c3_group = VGroup(t3, desc3, eq_ex3).arrange(DOWN, buff=0.25)
        panel3 = VGroup(box3, c3_group)
        c3_group.move_to(box3.get_center())
        
        triptych = VGroup(panel1, panel2, panel3).arrange(RIGHT, buff=0.6)
        triptych.shift(DOWN * 0.4)
        
        self.play(FadeIn(triptych, shift=UP*0.3), run_time=2.0)
        self.wait(3.0)
        
        # Outro Transition
        self.play(
            FadeOut(title),
            FadeOut(triptych),
            run_time=1.5
        )
        
        # Exact audio synchronization
        sync_wait_to_audio(self, 5, min_extra=0.8)

if __name__ == "__main__":
    pass
