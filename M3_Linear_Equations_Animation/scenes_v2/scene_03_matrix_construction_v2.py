"""
Scene 3 (v2): Kinetic Matrix Construction & Multiplication
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

class Scene03MatrixConstructionV2(Scene):
    def construct(self):
        # ----------------------------------------------------
        # BEAT 1 (s3_b1: ~5.38s) - Header and System Setup
        # ----------------------------------------------------
        def beat1_action():
            title = Text("CONSTRUCTING MATRIX EQUATION Ax = b", font="Helvetica", weight=BOLD, color=TEXT_COLOR).scale(0.72)
            title.to_edge(UP, buff=0.6)
            sub = Text("Tracing Exact Coefficient Paths & Row-Column Multiplication", font="Helvetica", color=LABEL_COLOR).scale(0.40)
            sub.next_to(title, DOWN, buff=0.18)
            accent = Line(LEFT * 4.2, RIGHT * 4.2, color=COLOR_A, stroke_width=2).next_to(sub, DOWN, buff=0.2)
            
            self.header = VGroup(title, sub, accent)
            
            # Left workstation equations
            self.eq1 = MathTex("2", "x", "+", "1", "y", "=", "5", font_size=44)
            self.eq1[0].set_color(COLOR_A)
            self.eq1[3].set_color(COLOR_A)
            self.eq1[6].set_color(COLOR_B)
            
            self.eq2 = MathTex("1", "x", "-", "1", "y", "=", "1", font_size=44)
            self.eq2[0].set_color(COLOR_A)
            self.eq2[3].set_color(COLOR_A)
            self.eq2[6].set_color(COLOR_B)
            
            sys_eqs = VGroup(self.eq1, self.eq2).arrange(DOWN, buff=0.6)
            sys_eqs.to_edge(LEFT, buff=1.2).shift(UP * 0.4)
            
            frame_left = RoundedRectangle(
                corner_radius=0.15, width=4.0, height=2.4,
                color=LABEL_COLOR, stroke_width=1.5, fill_color=BG_SECONDARY, fill_opacity=0.6
            ).move_to(sys_eqs.get_center())
            lbl_left = Text("Original System", font="Helvetica", color=LABEL_COLOR).scale(0.35).next_to(frame_left, UP, buff=0.15)
            
            self.left_box = VGroup(frame_left, lbl_left, sys_eqs)
            self.play(FadeIn(self.header, shift=DOWN*0.3), Create(frame_left), Write(sys_eqs), FadeIn(lbl_left), run_time=2.5)
            
        play_beat_sync(self, "s3_b1", beat1_action)
        
        # ----------------------------------------------------
        # BEAT 2 (s3_b2: ~5.59s) - Extract Row 1: 2 and 1
        # ----------------------------------------------------
        def beat2_action():
            mat_A = MathTex(
                r"A = \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix}",
                font_size=50
            )
            mat_A[0][0].set_color(COLOR_A)
            mat_A[0][3:8].set_color(COLOR_A)
            mat_A.shift(RIGHT * 2.2 + UP * 1.0)
            
            arrow_r1 = Arrow(start=self.eq1.get_right(), end=mat_A.get_left() + UP*0.3, color=COLOR_A, stroke_width=3)
            
            self.mat_A = mat_A
            self.arrow_r1 = arrow_r1
            self.play(GrowArrow(arrow_r1), FadeIn(mat_A[0][0:5]), run_time=1.8)
            self.play(Flash(mat_A[0][3:5], color=COLOR_A), run_time=1.2)
            
        play_beat_sync(self, "s3_b2", beat2_action)
        
        # ----------------------------------------------------
        # BEAT 3 (s3_b3: ~7.44s) - Extract Row 2: 1 and -1
        # ----------------------------------------------------
        def beat3_action():
            arrow_r2 = Arrow(start=self.eq2.get_right(), end=self.mat_A.get_left() + DOWN*0.3, color=COLOR_A, stroke_width=3)
            
            self.play(
                GrowArrow(arrow_r2),
                FadeIn(self.mat_A[0][5:]),
                run_time=2.0
            )
            self.play(
                Flash(self.mat_A[0][5:8], color=COLOR_A),
                FadeOut(self.arrow_r1),
                FadeOut(arrow_r2),
                run_time=1.8
            )
            
        play_beat_sync(self, "s3_b3", beat3_action)
        
        # ----------------------------------------------------
        # BEAT 4 (s3_b4: ~7.25s) - Build vector x and vector b
        # ----------------------------------------------------
        def beat4_action():
            vec_x = MathTex(r"\mathbf{x} = \begin{bmatrix} x \\ y \end{bmatrix}", font_size=50)
            vec_x[0][0].set_color(COLOR_X)
            vec_x[0][3:5].set_color(COLOR_X)
            
            vec_b = MathTex(r"\mathbf{b} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}", font_size=50)
            vec_b[0][0].set_color(COLOR_B)
            vec_b[0][3:5].set_color(COLOR_B)
            
            vectors = VGroup(vec_x, vec_b).arrange(RIGHT, buff=0.8)
            vectors.next_to(self.mat_A, DOWN, buff=0.6)
            
            self.vectors = vectors
            self.play(
                FadeIn(vec_x, shift=UP*0.3),
                FadeIn(vec_b, shift=UP*0.3),
                run_time=2.2
            )
            self.play(
                Flash(vec_x, color=COLOR_X),
                Flash(vec_b, color=COLOR_B),
                run_time=1.5
            )
            
        play_beat_sync(self, "s3_b4", beat4_action)
        
        # ----------------------------------------------------
        # BEAT 5 (s3_b5: ~5.83s) - Center full Ax = b & Row-Column Scan
        # ----------------------------------------------------
        def beat5_action():
            self.play(
                FadeOut(self.left_box),
                FadeOut(self.mat_A),
                FadeOut(self.vectors),
                run_time=1.0
            )
            
            full_eq = MathTex(
                r"\begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix}",
                r"\begin{bmatrix} x \\ y \end{bmatrix}",
                r"=",
                r"\begin{bmatrix} 5 \\ 1 \end{bmatrix}",
                font_size=48
            )
            full_eq[0].set_color(COLOR_A)
            full_eq[1].set_color(COLOR_X)
            full_eq[3].set_color(COLOR_B)
            full_eq.shift(UP * 0.9)
            
            badge_scan = create_neon_badge("ROW × COLUMN COMPUTATION", COLOR_HIGHLIGHT)
            badge_scan.next_to(full_eq, UP, buff=0.4)
            
            self.full_eq = full_eq
            self.badge_scan = badge_scan
            self.play(Write(full_eq), FadeIn(badge_scan, shift=DOWN*0.2), run_time=2.0)
            
        play_beat_sync(self, "s3_b5", beat5_action)
        
        # ----------------------------------------------------
        # BEAT 6 (s3_b6: ~7.94s) - Row 1 evaluation: 2x + y = 5
        # ----------------------------------------------------
        def beat6_action():
            row1_eval = MathTex(
                r"\text{Row 1: } \quad 2(x) + 1(y) = 2x + y = 5",
                font_size=42
            )
            row1_eval[0][0:5].set_color(COLOR_A)
            row1_eval[0][5:15].set_color(COLOR_A)
            row1_eval[0][16:22].set_color(TEXT_COLOR)
            row1_eval[0][-1].set_color(COLOR_B)
            row1_eval.next_to(self.full_eq, DOWN, buff=0.6)
            
            self.row1_eval = row1_eval
            self.play(
                Indicate(self.full_eq[0], color=COLOR_A),
                Indicate(self.full_eq[1], color=COLOR_X),
                Write(row1_eval),
                run_time=2.5
            )
            
        play_beat_sync(self, "s3_b6", beat6_action)
        
        # ----------------------------------------------------
        # BEAT 7 (s3_b7: ~7.92s) - Row 2 evaluation: x - y = 1
        # ----------------------------------------------------
        def beat7_action():
            row2_eval = MathTex(
                r"\text{Row 2: } \quad 1(x) - 1(y) = x - y = 1",
                font_size=42
            )
            row2_eval[0][0:5].set_color(COLOR_X)
            row2_eval[0][5:15].set_color(COLOR_X)
            row2_eval[0][16:22].set_color(TEXT_COLOR)
            row2_eval[0][-1].set_color(COLOR_B)
            row2_eval.next_to(self.row1_eval, DOWN, buff=0.4)
            
            self.row2_eval = row2_eval
            self.play(
                Indicate(self.full_eq[0], color=COLOR_X),
                Indicate(self.full_eq[1], color=COLOR_X),
                Write(row2_eval),
                run_time=2.5
            )
            
        play_beat_sync(self, "s3_b7", beat7_action)
        
        # ----------------------------------------------------
        # BEAT 8 (s3_b8: ~7.32s) - Equivalent Compact Representation
        # ----------------------------------------------------
        def beat8_action():
            summary_badge = create_neon_badge("EXACT 1-TO-1 EQUIVALENCE TO ORIGINAL SYSTEM", COLOR_B)
            summary_badge.next_to(self.row2_eval, DOWN, buff=0.6)
            
            self.play(
                FadeIn(summary_badge, scale=1.1),
                run_time=1.8
            )
            self.wait(2.2)
            self.play(
                FadeOut(self.header),
                FadeOut(self.full_eq),
                FadeOut(self.badge_scan),
                FadeOut(self.row1_eval),
                FadeOut(self.row2_eval),
                FadeOut(summary_badge),
                run_time=1.5
            )
            
        play_beat_sync(self, "s3_b8", beat8_action)

if __name__ == "__main__":
    pass
