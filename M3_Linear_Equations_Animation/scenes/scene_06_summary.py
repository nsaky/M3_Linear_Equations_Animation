"""
Scene 6: Summary & Academic Credits
Duration: Synchronized with audio (~29s)
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

class Scene06Summary(Scene):
    def construct(self):
        # 1. Summary Title
        title = create_title("SUMMARY & KEY TAKEAWAYS", "Connecting Equations, Matrices, and Solution Sets")
        self.play(FadeIn(title, shift=DOWN*0.3), run_time=1.0)
        
        # 2. Three Takeaway Cards
        card1 = VGroup(
            MathTex(r"A", font_size=42, color=COLOR_A),
            Text("Coefficient Matrix", font="Helvetica", weight=BOLD, color=COLOR_A).scale(0.38),
            Text("Encodes system coefficients & structure", font="Helvetica", color=TEXT_COLOR).scale(0.32)
        ).arrange(DOWN, buff=0.15)
        
        card2 = VGroup(
            MathTex(r"x", font_size=42, color=COLOR_X),
            Text("Variable Vector", font="Helvetica", weight=BOLD, color=COLOR_X).scale(0.38),
            Text("Holds unknown column vector [x, y]^T", font="Helvetica", color=TEXT_COLOR).scale(0.32)
        ).arrange(DOWN, buff=0.15)
        
        card3 = VGroup(
            MathTex(r"b", font_size=42, color=COLOR_B),
            Text("Constant Vector", font="Helvetica", weight=BOLD, color=COLOR_B).scale(0.38),
            Text("Stores target right-hand constants [5, 1]^T", font="Helvetica", color=TEXT_COLOR).scale(0.32)
        ).arrange(DOWN, buff=0.15)
        
        cards = VGroup(card1, card2, card3).arrange(RIGHT, buff=0.8)
        cards.shift(UP * 0.8)
        
        self.play(FadeIn(cards, shift=UP*0.3), run_time=2.0)
        self.wait(1.5)
        
        # 3. Central Synthesis Formula
        synthesis = MathTex(
            r"Ax = b \quad \Longleftrightarrow \quad \text{Equations} \longleftrightarrow \text{Matrices} \longleftrightarrow \text{Solutions}",
            font_size=36,
            color=TEXT_COLOR
        )
        synthesis.next_to(cards, DOWN, buff=0.8)
        
        subtitle_takeaway = Text(
            "One system. One compact representation. Three possible solution-set outcomes.",
            font="Helvetica", color=LABEL_COLOR
        ).scale(0.38)
        subtitle_takeaway.next_to(synthesis, DOWN, buff=0.3)
        
        self.play(Write(synthesis), FadeIn(subtitle_takeaway), run_time=2.0)
        self.wait(2.5)
        
        # 4. Fade to Formal Academic Submission Credits
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(synthesis),
            FadeOut(subtitle_takeaway),
            run_time=1.2
        )
        
        credits_title = Text("ACADEMIC ASSESSMENT CREDITS", font="Helvetica", weight=BOLD, color=COLOR_A).scale(0.55)
        credits_title.to_edge(UP, buff=0.8)
        
        cred_items = [
            ("Course:", "M3 — Linear Algebra and Calculus (Internal Assessment)"),
            ("Topic:", "Systems of Linear Equations (From Equations to Matrices: Ax = b)"),
            ("Student Name:", "YASIR EQBAL"),
            ("Student ID:", "E25B070671"),
            ("Animation Framework:", "Python 3.13 + Manim Community Edition"),
            ("Typography & Math:", "LaTeX (pdflatex, dvisvgm, MathTex)"),
            ("Narration:", "Microsoft Edge Neural TTS (en-IN-PrabhatNeural)"),
            ("AI Assistance:", "AI tools used for scripting, coding, visual development and narration"),
            ("References:", "M3 Course Syllabus & Standard Undergraduate Linear Algebra"),
        ]
        
        credit_rows = []
        for label, val in cred_items:
            lbl_m = Text(label, font="Helvetica", weight=BOLD, color=LABEL_COLOR).scale(0.35)
            val_m = Text(val, font="Helvetica", color=TEXT_COLOR).scale(0.35)
            row = VGroup(lbl_m, val_m).arrange(RIGHT, buff=0.3)
            credit_rows.append(row)
            
        credits_group = VGroup(*credit_rows).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        credits_group.next_to(credits_title, DOWN, buff=0.5)
        
        self.play(FadeIn(credits_title), FadeIn(credits_group, shift=UP*0.2), run_time=2.0)
        self.wait(3.0)
        
        # Final fade to black
        self.play(
            FadeOut(credits_title),
            FadeOut(credits_group),
            run_time=1.5
        )
        
        # Exact audio synchronization
        sync_wait_to_audio(self, 6, min_extra=0.8)

if __name__ == "__main__":
    pass
