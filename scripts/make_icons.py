#!/usr/bin/env python3
"""Generate small, clean LinkedIn and GitHub header icons (PNG) for the resume.

Icons are simple, monochrome, brand-colored chips that read clearly at ~10px.
Output: resume/assets/linkedin.png, resume/assets/github.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "resume", "assets")
os.makedirs(ASSETS, exist_ok=True)
S = 256  # supersampled canvas; downscaled on save


def _font(size):
    for p in ["/System/Library/Fonts/Supplemental/Arial Bold.ttf",
              "/Library/Fonts/Arial Bold.ttf",
              "/System/Library/Fonts/Helvetica.ttc"]:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def linkedin():
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, S - 1, S - 1], radius=48, fill="#0A66C2")
    f = _font(150)
    text = "in"
    # center the 'in'
    bb = d.textbbox((0, 0), text, font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    d.text(((S - w) / 2 - bb[0], (S - h) / 2 - bb[1] - 6), text, font=f, fill="white")
    img.resize((64, 64), Image.LANCZOS).save(os.path.join(ASSETS, "linkedin.png"))


def github():
    # dark chip with a clean white "git branch" mark (two nodes + branch)
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, S - 1, S - 1], radius=48, fill="#181717")
    white = "#FFFFFF"
    lw = 18
    r = 26
    xL = 84          # left column x
    yT, yB = 66, 190  # top/bottom node centres
    xR = 172         # right (branch) node x
    yR = 128         # right node centre
    # vertical trunk between top and bottom-left nodes
    d.line([(xL, yT), (xL, yB)], fill=white, width=lw)
    # branch from top node out to the right node
    d.line([(xL, yT + 6), (xR, yR)], fill=white, width=lw)

    def node(cx, cy, fill):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill, outline=white, width=lw)
    node(xL, yT, "#181717")
    node(xL, yB, "#181717")
    node(xR, yR, "#181717")
    img.resize((64, 64), Image.LANCZOS).save(os.path.join(ASSETS, "github.png"))


if __name__ == "__main__":
    linkedin()
    github()
    print("wrote", os.path.join(ASSETS, "linkedin.png"))
    print("wrote", os.path.join(ASSETS, "github.png"))
