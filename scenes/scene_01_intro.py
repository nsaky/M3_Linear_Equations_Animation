"""
Scene 1: Hook / Context
Duration: Synchronized with audio (23.74s + pad -> ~25s)
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

class Scene01Intro(Scene):
    def construct(self):
        # 1. Opening Equations
        eq1 = MathTex(r"2x", r"+", r"y", r"=", r"5", font_size=48)
        eq1.set_color_by_tex(r"2x", COLOR_A)
        eq1.set_color_by_tex(r"y", COLOR_X)
        eq1.set_color_by_tex(r"5", COLOR_B)
        
        eq2 = MathTex(r"x", r"-", r"y", r"=", r"1", font_size=48)
        eq2.set_color_by_tex(r"x", COLOR_A)
        eq2.set_color_by_tex(r"y", COLOR_X)
        eq2.set_color_by_tex(r"1", COLOR_B)
        
        eq_group = VGroup(eq1, eq2).arrange(DOWN, buff=0.8)
        eq_group.shift(UP * 0.8)
        
        self.play(Write(eq1), run_time=1.5)
        self.wait(0.5)
        self.play(Write(eq2), run_time=1.5)
        self.wait(1.0)
        
        # 2. Pulsing Question Mark
        qmark = Text("?", font="Helvetica", weight=BOLD, color=COLOR_X).scale(1.8)
        qmark.next_to(eq_group, RIGHT, buff=1.2)
        
        callout = Text("Can two equations become one matrix equation?", font="Helvetica", color=TEXT_COLOR).scale(0.6)
        callout.next_to(eq_group, DOWN, buff=1.0)
        
        self.play(FadeIn(qmark, scale=1.2), Write(callout), run_time=1.8)
        self.wait(1.5)
        
        # 3. Equations move towards each other & Matrix outline forms
        matrix_box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.2, color=COLOR_A, stroke_width=2.5)
        matrix_box.move_to(eq_group.get_center())
        
        self.play(
            FadeOut(qmark),
            FadeOut(callout),
            eq1.animate.shift(DOWN * 0.25),
            eq2.animate.shift(UP * 0.25),
            Create(matrix_box),
            run_time=2.0
        )
        self.wait(1.0)
        
        # 4. Cinematic Title & Academic Metadata
        title_block = create_title(PROJECT_TITLE, PROJECT_SUBTITLE)
        
        student_meta = VGroup(
            Text(f"Student: {STUDENT_NAME}", font="Helvetica", color=TEXT_COLOR).scale(0.45),
            Text(f"Student ID: {STUDENT_ID}", font="Helvetica", color=LABEL_COLOR).scale(0.45),
            Text(COURSE_NAME, font="Helvetica", color=COLOR_A).scale(0.45),
        ).arrange(DOWN, buff=0.15)
        student_meta.to_edge(DOWN, buff=0.6)
        
        self.play(
            FadeOut(matrix_box),
            FadeOut(eq_group),
            FadeIn(title_block, shift=DOWN*0.5),
            FadeIn(student_meta, shift=UP*0.5),
            run_time=2.2
        )
        self.wait(3.0)
        
        # 5. Outro Transition
        self.play(
            FadeOut(title_block),
            FadeOut(student_meta),
            run_time=1.5
        )
        
        # Exact audio synchronization
        sync_wait_to_audio(self, 1, min_extra=0.8)

if __name__ == "__main__":
    pass
