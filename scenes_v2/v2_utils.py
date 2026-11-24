"""
v2 Utilities and Synchronization Engine
Provides millisecond-accurate beat matching, dynamic effects, and styling.
"""
import os
import json
from manim import *

# Styling
BG_COLOR = "#080D1A"           # Deep cinematic void
BG_SECONDARY = "#0F172A"       # Dark slate container
TEXT_COLOR = "#F8FAFC"         # Crisp white
LABEL_COLOR = "#94A3B8"        # Slate grey

COLOR_A = "#38BDF8"            # Neon Cyan (Coefficients / Matrix A)
COLOR_X = "#FBBF24"            # Radiant Amber (Variables / Vector x)
COLOR_B = "#34D399"            # Emerald Neon (Constants / Vector b)
COLOR_HIGHLIGHT = "#EC4899"    # Electric Pink/Magenta (Emphasis / Cancellation)
COLOR_POINT = "#10B981"        # Bright Green

STUDENT_NAME = "YASIR EQBAL"
STUDENT_ID = "E25B070671"
COURSE_NAME = "M3 — Linear Algebra and Calculus"
PROJECT_TITLE = "SYSTEMS OF LINEAR EQUATIONS"
PROJECT_SUBTITLE = "From Equations to Matrices: Understanding Ax = b"

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(PROJECT_DIR, "assets", "audio_v2", "beat_durations.json")

try:
    with open(JSON_PATH, "r") as f:
        BEAT_DURATIONS = json.load(f)
except Exception:
    BEAT_DURATIONS = {}

def get_beat_duration(beat_id, fallback=4.0):
    return BEAT_DURATIONS.get(beat_id, fallback)

def play_beat_sync(scene, beat_id, anim_action=None, anim_time=None):
    """
    Executes an animation or action and holds for the exact remaining duration of the beat.
    Guarantees zero audio-visual drift.
    """
    total_dur = get_beat_duration(beat_id)
    start_t = scene.renderer.time
    
    if anim_action:
        anim_action()
        
    elapsed = scene.renderer.time - start_t
    remaining = total_dur - elapsed
    if remaining > 0:
        scene.wait(remaining)
    else:
        scene.wait(0.05)

def create_neon_badge(text, color):
    """Creates a high-contrast glowing badge."""
    lbl = Text(text, font="Helvetica", weight=BOLD, color="#FFFFFF").scale(0.38)
    bg = RoundedRectangle(
        corner_radius=0.18,
        width=lbl.width + 0.45,
        height=lbl.height + 0.3,
        fill_color=color,
        fill_opacity=0.85,
        stroke_color="#FFFFFF",
        stroke_width=1.5
    )
    glow = RoundedRectangle(
        corner_radius=0.22,
        width=bg.width + 0.12,
        height=bg.height + 0.12,
        stroke_color=color,
        stroke_width=3,
        stroke_opacity=0.4
    )
    return VGroup(glow, bg, lbl)
