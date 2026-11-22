"""
Generates a professional Storyboard PDF document for academic assessment submission.
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

DOCS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(DOCS_DIR)
OUTPUT_PDF = os.path.join(DOCS_DIR, "storyboard.pdf")

def build_pdf():
    pdf = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=40, rightMargin=40,
        topMargin=40, bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0B1220'),
        alignment=1, # Center
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#39C6E6'),
        alignment=1,
        spaceAfter=15
    )
    
    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#4A5568'),
        alignment=1,
        spaceAfter=20
    )
    
    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#0B1220'),
        spaceBefore=12,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#2D3748'),
        spaceAfter=6
    )
    
    label_style = ParagraphStyle(
        'LabelBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1A202C')
    )

    story = []
    
    # Header block
    story.append(Paragraph("M3 MATHEMATICS ANIMATION VIDEO: STORYBOARD", title_style))
    story.append(Paragraph("Systems of Linear Equations — From Equations to Matrices: Understanding Ax = b", subtitle_style))
    meta_text = (
        "<b>Subject:</b> Linear Algebra and Calculus (M3) &nbsp;|&nbsp; "
        "<b>Student:</b> YASIR EQBAL (ID: E25B070671)<br/>"
        "<b>Target Duration:</b> 270 seconds (4m 30s) &nbsp;|&nbsp; "
        "<b>Resolution:</b> 1920×1080 (30 FPS) &nbsp;|&nbsp; "
        "<b>Animation Engine:</b> Python + Manim"
    )
    story.append(Paragraph(meta_text, meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#39C6E6'), spaceAfter=15))
    
    # Palette summary table
    palette_data = [
        [Paragraph("<b>Component</b>", label_style), Paragraph("<b>Visual Identity & Hex Code</b>", label_style), Paragraph("<b>Mathematical Role</b>", label_style)],
        [Paragraph("Background", body_style), Paragraph("Midnight Navy (#0B1220)", body_style), Paragraph("Dark mathematical canvas", body_style)],
        [Paragraph("Matrix A / Coefficients", body_style), Paragraph("Cyan (#39C6E6)", body_style), Paragraph("Encodes system coefficients and equations", body_style)],
        [Paragraph("Vector x / Variables", body_style), Paragraph("Amber (#FFBF69)", body_style), Paragraph("Encodes unknown variables [x, y]^T", body_style)],
        [Paragraph("Vector b / Constants", body_style), Paragraph("Green (#55D6A5)", body_style), Paragraph("Encodes target constants [5, 1]^T", body_style)],
        [Paragraph("Solution / Intersection", body_style), Paragraph("Bright Green (#22C55E)", body_style), Paragraph("Unique intersection point (2, 1)", body_style)],
    ]
    t_palette = Table(palette_data, colWidths=[120, 160, 250])
    t_palette.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EDF2F7')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_palette)
    story.append(Spacer(1, 15))
    
    # 6 Scenes
    scenes_data = [
        {
            "num": "Scene 1",
            "title": "Hook & Context",
            "time": "00:00 – 00:25 (25s)",
            "purpose": "Pose the central guiding question: Can two separate equations become one compact matrix equation?",
            "visuals": "Dark background; 2x + y = 5 and x - y = 1 write on with glowing cyan and amber colors. A pulsing question mark appears, followed by title 'SYSTEMS OF LINEAR EQUATIONS' and author credits.",
            "math": "2x + y = 5, x - y = 1 --> Ax = b?",
            "narration": "Imagine two equations with two unknowns... How do we represent both together in a single expression? Linear algebra gives us matrix notation."
        },
        {
            "num": "Scene 2",
            "title": "Concept Introduction",
            "time": "00:25 – 01:00 (35s)",
            "purpose": "Establish linear system vocabulary and define the general matrix equation Ax = b with dimensional compatibility.",
            "visuals": "Equation highlighting: Cyan coefficients, Amber variables, Green constants with badges. Ax = b appears with dimensional breakdown cards: A (m x n), x (n x 1), b (m x 1).",
            "math": "A_(m x n) x_(n x 1) = b_(m x 1)",
            "narration": "A system of linear equations contains multiple conditions that hold true simultaneously. Matrix notation unifies this into Ax = b."
        },
        {
            "num": "Scene 3",
            "title": "Visual Intuition & Matrix Construction",
            "time": "01:00 – 01:55 (55s)",
            "purpose": "Trace the step-by-step extraction of coefficients and prove matrix multiplication equivalence.",
            "visuals": "Coefficients [2, 1] travel into Row 1 of A; [1, -1] travel into Row 2 of A. Column vectors x and b form. Matrix multiplication expands to show [2x + y, x - y]^T = [5, 1]^T.",
            "math": "[ [2, 1], [1, -1] ] [x, y]^T = [2x + y, x - y]^T = [5, 1]^T",
            "narration": "Let's build the matrix equation from our example... When we multiply A by x, the first row recreates our first equation, and the second row recreates our second equation."
        },
        {
            "num": "Scene 4",
            "title": "Worked Example & Verification",
            "time": "01:55 – 03:35 (100s)",
            "purpose": "Solve the system algebraically with elimination, substitution, and formally verify Ax = b.",
            "visuals": "Equations (1) and (2) add together; +y and -y cancel out -> 3x = 6 -> x = 2. Substitute x=2 into eq (2) -> y = 1. Solution vector [2, 1]^T multiplies A: [2(2)+1(1), 1(2)-1(1)]^T = [5, 1]^T = b. Green verified checkmark.",
            "math": "(2x+y)+(x-y)=6 => 3x=6 => x=2, y=1. Verification: A [2, 1]^T = [5, 1]^T = b.",
            "narration": "Now let's solve the system algebraically... We verify by substitution into our matrix equation Ax... Ax = b is satisfied, proving our solution is correct."
        },
        {
            "num": "Scene 5",
            "title": "Geometric Interpretation & Solution Sets",
            "time": "03:35 – 04:05 (30s)",
            "purpose": "Bridge the algebraic solution to geometric line intersection and illustrate the 3 solution cases.",
            "visuals": "Cartesian grid plots y = 5 - 2x (Cyan) and y = x - 1 (Amber). Green intersection point pulses at (2, 1). Three mini panels showcase: 1) One Solution (intersecting), 2) No Solution (parallel), 3) Infinitely Many (coincident).",
            "math": "Lines intersect at (2, 1) <-> Solution vector [2, 1]^T. Three cases: Unique, Inconsistent, Dependent.",
            "narration": "Geometrically, each linear equation represents a straight line. Solving the system means finding where the two lines meet. Intersecting, parallel, or coincident."
        },
        {
            "num": "Scene 6",
            "title": "Summary & Credits",
            "time": "04:05 – 04:30 (25s)",
            "purpose": "Recap core takeaways and present academic assessment metadata and credits.",
            "visuals": "Three summary points appear. Ax = b banner. Official credit card: M3 Linear Algebra, Student Yasir Eqbal, ID: E25B070671, Manim animation engine.",
            "math": "Equations <-> Matrices <-> Geometry. Ax = b.",
            "narration": "To summarize, a system of linear equations is compactly represented as Ax = b... This assessment was presented by Yasir Eqbal, ID: E25B070671. Thank you for watching."
        }
    ]
    
    for sc in scenes_data:
        story.append(Paragraph(f"<b>{sc['num']}: {sc['title']}</b> &nbsp;&nbsp;[Timeline: {sc['time']}]", h2_style))
        s_data = [
            [Paragraph("<b>Purpose:</b>", label_style), Paragraph(sc['purpose'], body_style)],
            [Paragraph("<b>Visuals & Animation:</b>", label_style), Paragraph(sc['visuals'], body_style)],
            [Paragraph("<b>Mathematical Content:</b>", label_style), Paragraph(sc['math'], body_style)],
            [Paragraph("<b>Narration Summary:</b>", label_style), Paragraph(sc['narration'], body_style)],
        ]
        t_sc = Table(s_data, colWidths=[120, 410])
        t_sc.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F7FAFC')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#E2E8F0')),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#EDF2F7')),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ]))
        story.append(t_sc)
        story.append(Spacer(1, 10))
        
    pdf.build(story)
    print(f"✓ Storyboard PDF generated successfully: {OUTPUT_PDF}")

if __name__ == "__main__":
    build_pdf()
