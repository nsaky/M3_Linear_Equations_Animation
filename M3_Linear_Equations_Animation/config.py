"""
Global configuration and styling for M3 Linear Equations Animation video.
"""
import os
import subprocess
from manim import *

# Canvas & Background Colors
BG_COLOR = "#0B1220"           # Deep midnight navy
BG_SECONDARY = "#111C2E"       # Secondary dark background
TEXT_COLOR = "#F4F6FA"         # Off-white primary text
LABEL_COLOR = "#A6B2C2"        # Muted grey for annotations

# Mathematical Identity Colors
COLOR_A = "#39C6E6"            # Cyan for Matrix A and Coefficients
COLOR_X = "#FFBF69"            # Amber for Vector x and Unknown Variables
COLOR_B = "#55D6A5"            # Green for Vector b and Constants

# Geometry Colors
COLOR_LINE_1 = "#39C6E6"       # Cyan for line 2x + y = 5 (y = 5 - 2x)
COLOR_LINE_2 = "#FFBF69"       # Amber for line x - y = 1 (y = x - 1)
COLOR_POINT = "#22C55E"        # Bright green for intersection point (2, 1)

# Student & Assessment Metadata
STUDENT_NAME = "YASIR EQBAL"
STUDENT_ID = "E25B070671"
COURSE_NAME = "M3 — Linear Algebra and Calculus"
PROJECT_TITLE = "SYSTEMS OF LINEAR EQUATIONS"
PROJECT_SUBTITLE = "From Equations to Matrices: Understanding Ax = b"

# Path helpers
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "output")
SCENES_DIR = os.path.join(PROJECT_DIR, "scenes")
DOCS_DIR = os.path.join(PROJECT_DIR, "documentation")

# Video Specs
TARGET_FPS = 30
PIXEL_WIDTH = 1920
PIXEL_HEIGHT = 1080

def create_title(title_text, subtitle_text=None):
    """Creates a consistent cinematic title block."""
    title = Text(title_text, font="Helvetica", weight=BOLD, color=TEXT_COLOR)
    title.scale(0.85)
    title.to_edge(UP, buff=0.6)
    
    if subtitle_text:
        sub = Text(subtitle_text, font="Helvetica", color=LABEL_COLOR)
        sub.scale(0.5)
        sub.next_to(title, DOWN, buff=0.2)
        return VGroup(title, sub)
    return title

def create_badge(text, color):
    """Creates an editorial label pill/badge."""
    label = Text(text, font="Helvetica", weight=BOLD, color="#FFFFFF").scale(0.35)
    bg = RoundedRectangle(
        corner_radius=0.15,
        width=label.width + 0.4,
        height=label.height + 0.25,
        fill_color=color,
        fill_opacity=0.85,
        stroke_color=color,
        stroke_width=1.5
    )
    return VGroup(bg, label)

def get_audio_duration(audio_path):
    """Returns exact audio duration via ffprobe."""
    if not os.path.exists(audio_path):
        return 0.0
    try:
        res = subprocess.run([
            "/opt/homebrew/bin/ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", audio_path
        ], capture_output=True, text=True)
        return float(res.stdout.strip())
    except Exception:
        return 0.0

def sync_wait_to_audio(scene, scene_num, min_extra=0.8):
    """Ensures scene animation runtime matches audio narration perfectly."""
    audio_file = os.path.join(AUDIO_DIR, f"scene_{scene_num:02d}.mp3")
    audio_dur = get_audio_duration(audio_file)
    if audio_dur > 0:
        target_dur = audio_dur + min_extra
        curr_time = scene.renderer.time
        diff = target_dur - curr_time
        if diff > 0:
            scene.wait(diff)
        else:
            scene.wait(0.5)
    else:
        scene.wait(1.0)
