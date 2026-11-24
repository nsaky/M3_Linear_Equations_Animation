"""
Scene 1 (v2): High-Impact Hook & Core Dilemma
Full beat-by-beat sync with audio.
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

class Scene01IntroV2(Scene):
    def construct(self):
        # ----------------------------------------------------
        # BEAT 1 (s1_b1: ~8.52s) - Cyber equation swarm & radar scan
        # ----------------------------------------------------
        def beat1_action():
            swarm = VGroup(
                MathTex(r"\mathbf{y} = \mathbf{W}\mathbf{x} + \mathbf{b}", font_size=32, color=COLOR_A),
                MathTex(r"\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}", font_size=28, color=COLOR_X),
                MathTex(r"\text{GPS}: \Delta t = \frac{\sqrt{x^2+y^2+z^2}}{c}", font_size=26, color=COLOR_B),
                MathTex(r"a_{11}x_1 + a_{12}x_2 = b_1", font_size=30, color=COLOR_HIGHLIGHT),
                MathTex(r"2x + y = 5", font_size=36, color=COLOR_A),
                MathTex(r"x - y = 1", font_size=36, color=COLOR_X),
            )
            swarm[0].shift(UL * 2.2 + LEFT * 0.5)
            swarm[1].shift(UR * 2.2 + RIGHT * 0.5)
            swarm[2].shift(DOWN * 2.2 + LEFT * 1.5)
            swarm[3].shift(DOWN * 2.2 + RIGHT * 1.5)
            swarm[4].shift(UP * 0.6 + LEFT * 0.2)
            swarm[5].shift(DOWN * 0.6 + LEFT * 0.2)
            
            # Ambient grid ring
            ring1 = Circle(radius=1.8, color=COLOR_A, stroke_width=1.5, stroke_opacity=0.3)
            ring2 = Circle(radius=3.2, color=COLOR_X, stroke_width=1.5, stroke_opacity=0.2)
            
            self.play(
                FadeIn(swarm[0], shift=DOWN*0.3),
                FadeIn(swarm[1], shift=DOWN*0.3),
                FadeIn(swarm[2], shift=UP*0.3),
                FadeIn(swarm[3], shift=UP*0.3),
                Create(ring1), Create(ring2),
                run_time=2.2
            )
            self.play(
                Write(swarm[4]),
                Write(swarm[5]),
                ring1.animate.scale(1.15),
                run_time=2.0
            )
            self.swarm = swarm
            self.rings = VGroup(ring1, ring2)
            
        play_beat_sync(self, "s1_b1", beat1_action)
        
        # ----------------------------------------------------
        # BEAT 2 (s1_b2: ~4.61s) - Question mark & shockwave chaos
        # ----------------------------------------------------
        def beat2_action():
            qmark = Text("?", font="Helvetica", weight=BOLD, color=COLOR_HIGHLIGHT).scale(2.2)
            q_pulse = Circle(radius=0.8, color=COLOR_HIGHLIGHT, stroke_width=3).move_to(qmark.get_center())
            
            callout = Text("How do we solve massive systems?", font="Helvetica", weight=BOLD, color=TEXT_COLOR).scale(0.55)
            callout.shift(DOWN * 1.8)
            
            self.play(
                FadeIn(qmark, scale=1.5),
                Create(q_pulse),
                Write(callout),
                run_time=1.8
            )
            self.play(
                q_pulse.animate.scale(2.5).set_opacity(0),
                run_time=1.5
            )
            self.q_elements = VGroup(qmark, q_pulse, callout)
            
        play_beat_sync(self, "s1_b2", beat2_action)
        
        # ----------------------------------------------------
        # BEAT 3 (s1_b3: ~6.84s) - Collapse swarm into Ax = b
        # ----------------------------------------------------
        def beat3_action():
            # Clean swarm and question mark
            self.play(
                FadeOut(self.swarm[0]),
                FadeOut(self.swarm[1]),
                FadeOut(self.swarm[2]),
                FadeOut(self.swarm[3]),
                FadeOut(self.rings),
                FadeOut(self.q_elements),
                run_time=1.2
            )
            
            # Central core equations lock in
            core_eqs = VGroup(self.swarm[4], self.swarm[5])
            
            # Matrix bracket outline
            matrix_bracket = RoundedRectangle(
                corner_radius=0.25, width=4.0, height=2.4,
                color=COLOR_A, stroke_width=3.5, fill_color=BG_SECONDARY, fill_opacity=0.75
            )
            matrix_bracket.move_to(core_eqs.get_center())
            
            ax_b_label = MathTex(r"A \mathbf{x} = \mathbf{b}", font_size=52, color=COLOR_X)
            ax_b_label.next_to(matrix_bracket, UP, buff=0.4)
            
            self.play(
                core_eqs.animate.move_to(ORIGIN).scale(1.2),
                Create(matrix_bracket),
                run_time=1.8
            )
            self.play(
                FadeIn(ax_b_label, shift=DOWN*0.2),
                Flash(matrix_bracket, color=COLOR_A, line_length=0.3, num_lines=16),
                run_time=1.5
            )
            self.core_group = VGroup(core_eqs, matrix_bracket, ax_b_label)
            
        play_beat_sync(self, "s1_b3", beat3_action)
        
        # ----------------------------------------------------
        # BEAT 4 (s1_b4: ~4.44s) - Cinematic Title Drop
        # ----------------------------------------------------
        def beat4_action():
            self.play(
                FadeOut(self.core_group),
                run_time=0.8
            )
            title = Text(PROJECT_TITLE, font="Helvetica", weight=BOLD, color=TEXT_COLOR).scale(0.85)
            title.shift(UP * 0.8)
            sub = Text(PROJECT_SUBTITLE, font="Helvetica", color=COLOR_A).scale(0.48)
            sub.next_to(title, DOWN, buff=0.25)
            
            border = Line(LEFT * 4.5, RIGHT * 4.5, color=COLOR_X, stroke_width=2.5)
            border.next_to(sub, DOWN, buff=0.3)
            
            self.play(
                FadeIn(title, shift=DOWN*0.4),
                FadeIn(sub, shift=UP*0.2),
                Create(border),
                run_time=1.8
            )
            self.title_group = VGroup(title, sub, border)
            
        play_beat_sync(self, "s1_b4", beat4_action)
        
        # ----------------------------------------------------
        # BEAT 5 (s1_b5: ~8.62s) - Academic presenter card & outro
        # ----------------------------------------------------
        def beat5_action():
            card_bg = RoundedRectangle(
                corner_radius=0.2, width=8.0, height=2.0,
                color=COLOR_B, stroke_width=2.0, fill_color=BG_SECONDARY, fill_opacity=0.9
            )
            card_bg.next_to(self.title_group, DOWN, buff=0.5)
            
            author_txt = Text(f"Presenter: {STUDENT_NAME}", font="Helvetica", weight=BOLD, color=TEXT_COLOR).scale(0.48)
            id_txt = Text(f"Student ID: {STUDENT_ID}", font="Helvetica", color=COLOR_X).scale(0.42)
            course_txt = Text(COURSE_NAME, font="Helvetica", color=COLOR_A).scale(0.42)
            
            meta = VGroup(author_txt, id_txt, course_txt).arrange(DOWN, buff=0.18)
            meta.move_to(card_bg.get_center())
            presenter_card = VGroup(card_bg, meta)
            
            self.play(
                FadeIn(presenter_card, shift=UP*0.3),
                run_time=2.0
            )
            self.wait(2.5)
            self.play(
                FadeOut(self.title_group),
                FadeOut(presenter_card),
                run_time=1.8
            )
            
        play_beat_sync(self, "s1_b5", beat5_action)

if __name__ == "__main__":
    pass
