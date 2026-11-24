"""
Scene 4 (v2): Worked Example & Rigorous Matrix Verification
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

class Scene04WorkedExampleV2(Scene):
    def construct(self):
        # ----------------------------------------------------
        # BEAT 1 (s4_b1: ~4.06s) - Header Setup
        # ----------------------------------------------------
        def beat1_action():
            title = Text("SOLVING THE SYSTEM & MATRIX VERIFICATION", font="Helvetica", weight=BOLD, color=TEXT_COLOR).scale(0.70)
            title.to_edge(UP, buff=0.6)
            sub = Text("Step-by-Step Elimination, Substitution, and Direct Evaluation", font="Helvetica", color=LABEL_COLOR).scale(0.40)
            sub.next_to(title, DOWN, buff=0.18)
            accent = Line(LEFT * 4.4, RIGHT * 4.4, color=COLOR_A, stroke_width=2).next_to(sub, DOWN, buff=0.2)
            
            self.header = VGroup(title, sub, accent)
            self.play(FadeIn(self.header, shift=DOWN*0.3), run_time=1.8)
            
        play_beat_sync(self, "s4_b1", beat1_action)
        
        # ----------------------------------------------------
        # BEAT 2 (s4_b2: ~7.58s) - Display equations (1) and (2)
        # ----------------------------------------------------
        def beat2_action():
            self.eq1 = MathTex(r"2x + y = 5", r"\quad \text{--- (1)}", font_size=44)
            self.eq2 = MathTex(r"x - y = 1",  r"\quad \text{--- (2)}", font_size=44)
            self.eq1[0][0:2].set_color(COLOR_A)
            self.eq2[0][0].set_color(COLOR_A)
            
            sys_group = VGroup(self.eq1, self.eq2).arrange(DOWN, buff=0.45)
            sys_group.to_edge(LEFT, buff=1.2).shift(UP * 0.8)
            
            self.sys_group = sys_group
            self.play(Write(self.eq1), Write(self.eq2), run_time=2.2)
            
        play_beat_sync(self, "s4_b2", beat2_action)
        
        # ----------------------------------------------------
        # BEAT 3 (s4_b3: ~6.46s) - Plus sign and y-cancellation
        # ----------------------------------------------------
        def beat3_action():
            plus = MathTex(r"+", font_size=46, color=LABEL_COLOR).next_to(self.sys_group, LEFT, buff=0.3)
            h_line = Line(
                start=self.sys_group.get_corner(DL) + LEFT*0.6,
                end=self.sys_group.get_corner(DR) + RIGHT*0.4,
                color=LABEL_COLOR, stroke_width=2
            )
            
            slash1 = Line(self.eq1[0][2].get_corner(DL), self.eq1[0][3].get_corner(UR), color=COLOR_HIGHLIGHT, stroke_width=3.5)
            slash2 = Line(self.eq2[0][1].get_corner(DL), self.eq2[0][2].get_corner(UR), color=COLOR_HIGHLIGHT, stroke_width=3.5)
            
            self.elim_helpers = VGroup(plus, h_line, slash1, slash2)
            self.play(FadeIn(plus), Create(h_line), run_time=1.2)
            self.play(Create(slash1), Create(slash2), run_time=1.5)
            
        play_beat_sync(self, "s4_b3", beat3_action)
        
        # ----------------------------------------------------
        # BEAT 4 (s4_b4: ~3.00s) - Result 3x = 6
        # ----------------------------------------------------
        def beat4_action():
            res_3x = MathTex(r"3x = 6", font_size=46)
            res_3x.next_to(self.elim_helpers[1], DOWN, buff=0.35).align_to(self.sys_group, LEFT)
            
            self.res_3x = res_3x
            self.play(Write(res_3x), run_time=1.5)
            
        play_beat_sync(self, "s4_b4", beat4_action)
        
        # ----------------------------------------------------
        # BEAT 5 (s4_b5: ~4.49s) - x = 2
        # ----------------------------------------------------
        def beat5_action():
            sol_x = MathTex(r"\implies x = \frac{6}{3} \implies x = 2", font_size=44)
            sol_x[0][-4:].set_color(COLOR_X)
            sol_x.next_to(self.res_3x, DOWN, buff=0.3).align_to(self.res_3x, LEFT)
            
            self.sol_x = sol_x
            self.play(Write(sol_x), Flash(sol_x[0][-4:], color=COLOR_X), run_time=2.0)
            
        play_beat_sync(self, "s4_b5", beat5_action)
        
        # ----------------------------------------------------
        # BEAT 6 (s4_b6: ~5.40s) - Substitute x = 2 into (2)
        # ----------------------------------------------------
        def beat6_action():
            sub_step1 = MathTex(r"\text{Substitute } x = 2 \text{ into (2): } \quad 2 - y = 1", font_size=40)
            sub_step1.next_to(self.sol_x, DOWN, buff=0.4).align_to(self.sol_x, LEFT)
            
            self.sub_step1 = sub_step1
            self.play(Write(sub_step1), run_time=2.2)
            
        play_beat_sync(self, "s4_b6", beat6_action)
        
        # ----------------------------------------------------
        # BEAT 7 (s4_b7: ~5.64s) - -y = -1 => y = 1
        # ----------------------------------------------------
        def beat7_action():
            sub_step2 = MathTex(r"\implies -y = -1 \implies y = 1", font_size=40)
            sub_step2[0][-4:].set_color(COLOR_X)
            sub_step2.next_to(self.sub_step1, DOWN, buff=0.3).align_to(self.sub_step1, LEFT)
            
            self.sub_step2 = sub_step2
            self.play(Write(sub_step2), Flash(sub_step2[0][-4:], color=COLOR_X), run_time=2.2)
            
        play_beat_sync(self, "s4_b7", beat7_action)
        
        # ----------------------------------------------------
        # BEAT 8 (s4_b8: ~7.75s) - Prominent Solution Vector Card
        # ----------------------------------------------------
        def beat8_action():
            sol_card_bg = RoundedRectangle(
                corner_radius=0.22, width=3.8, height=3.0,
                color=COLOR_X, stroke_width=2.5, fill_color=BG_SECONDARY, fill_opacity=0.95
            ).move_to(RIGHT * 3.5 + UP * 0.2)
            
            sol_badge = create_neon_badge("UNIQUE SOLUTION", COLOR_X)
            sol_badge.next_to(sol_card_bg.get_top(), DOWN, buff=0.25)
            
            sol_vec = MathTex(
                r"\mathbf{x} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}",
                font_size=56, color=COLOR_X
            ).move_to(sol_card_bg.get_center() + DOWN * 0.2)
            
            sol_card = VGroup(sol_card_bg, sol_badge, sol_vec)
            self.sol_card = sol_card
            self.play(FadeIn(sol_card, shift=LEFT*0.4), Flash(sol_card, color=COLOR_X), run_time=2.2)
            
        play_beat_sync(self, "s4_b8", beat8_action)
        
        # ----------------------------------------------------
        # BEAT 9 (s4_b9: ~5.71s) - Shift Left & Open Verification
        # ----------------------------------------------------
        def beat9_action():
            left_elements = VGroup(
                self.sys_group, self.elim_helpers,
                self.res_3x, self.sol_x, self.sub_step1, self.sub_step2
            )
            self.play(
                FadeOut(left_elements),
                self.sol_card.animate.scale(0.85).to_edge(LEFT, buff=1.0).shift(UP * 0.5),
                run_time=1.5
            )
            verif_title = Text("VERIFICATION VIA MATRIX MULTIPLICATION", font="Helvetica", weight=BOLD, color=COLOR_B).scale(0.46)
            verif_title.shift(RIGHT * 1.5 + UP * 1.8)
            
            self.verif_title = verif_title
            self.play(FadeIn(verif_title, shift=DOWN*0.2), run_time=1.2)
            
        play_beat_sync(self, "s4_b9", beat9_action)
        
        # ----------------------------------------------------
        # BEAT 10 (s4_b10: ~4.15s) - Matrix A times Vector x
        # ----------------------------------------------------
        def beat10_action():
            v_prod = MathTex(
                r"A \mathbf{x} = \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix}",
                font_size=44
            )
            v_prod[0][0].set_color(COLOR_A)
            v_prod[0][1].set_color(COLOR_X)
            v_prod[0][3:8].set_color(COLOR_A)
            v_prod[0][10:12].set_color(COLOR_X)
            v_prod.next_to(self.verif_title, DOWN, buff=0.4).align_to(self.verif_title, LEFT)
            
            self.v_prod = v_prod
            self.play(Write(v_prod), run_time=1.8)
            
        play_beat_sync(self, "s4_b10", beat10_action)
        
        # ----------------------------------------------------
        # BEAT 11 (s4_b11: ~6.26s) - Row 1 Evaluation: 2(2) + 1(1) = 5
        # ----------------------------------------------------
        def beat11_action():
            v_row1 = MathTex(
                r"\text{Row 1: } \quad 2(2) + 1(1) = 4 + 1 = 5",
                font_size=40
            )
            v_row1[0][-1].set_color(COLOR_B)
            v_row1.next_to(self.v_prod, DOWN, buff=0.4).align_to(self.v_prod, LEFT)
            
            self.v_row1 = v_row1
            self.play(
                Indicate(self.v_prod[0][3:5], color=COLOR_A),
                Indicate(self.v_prod[0][10:12], color=COLOR_X),
                Write(v_row1),
                run_time=2.2
            )
            
        play_beat_sync(self, "s4_b11", beat11_action)
        
        # ----------------------------------------------------
        # BEAT 12 (s4_b12: ~6.46s) - Row 2 Evaluation: 1(2) - 1(1) = 1
        # ----------------------------------------------------
        def beat12_action():
            v_row2 = MathTex(
                r"\text{Row 2: } \quad 1(2) - 1(1) = 2 - 1 = 1",
                font_size=40
            )
            v_row2[0][-1].set_color(COLOR_B)
            v_row2.next_to(self.v_row1, DOWN, buff=0.35).align_to(self.v_row1, LEFT)
            
            self.v_row2 = v_row2
            self.play(
                Indicate(self.v_prod[0][5:8], color=COLOR_A),
                Indicate(self.v_prod[0][10:12], color=COLOR_X),
                Write(v_row2),
                run_time=2.2
            )
            
        play_beat_sync(self, "s4_b12", beat12_action)
        
        # ----------------------------------------------------
        # BEAT 13 (s4_b13: ~8.76s) - Equals vector b & Verified Badge
        # ----------------------------------------------------
        def beat13_action():
            v_final = MathTex(
                r"= \begin{bmatrix} 5 \\ 1 \end{bmatrix} = \mathbf{b}",
                font_size=46, color=COLOR_B
            )
            v_final.next_to(self.v_row2, DOWN, buff=0.4).align_to(self.v_row2, LEFT)
            
            verif_badge = create_neon_badge("VERIFIED: Ax = b IS EXACTLY SATISFIED", COLOR_B)
            verif_badge.next_to(v_final, DOWN, buff=0.5).align_to(v_final, LEFT)
            
            self.play(Write(v_final), run_time=1.8)
            self.play(FadeIn(verif_badge, scale=1.15), Flash(verif_badge, color=COLOR_B), run_time=1.8)
            self.wait(2.2)
            
            self.play(
                FadeOut(self.header),
                FadeOut(self.sol_card),
                FadeOut(self.verif_title),
                FadeOut(self.v_prod),
                FadeOut(self.v_row1),
                FadeOut(self.v_row2),
                FadeOut(v_final),
                FadeOut(verif_badge),
                run_time=1.5
            )
            
        play_beat_sync(self, "s4_b13", beat13_action)

if __name__ == "__main__":
    pass
