# Баннер профиля в двух темах, как на chestor.site: «Человек» (светлая) и «Гуль» (тёмная).
# GitHub показывает SVG через <img>, веб-шрифты там не грузятся, поэтому текст — контуры.
# Запуск: python assets/src/banner.py [папка со шрифтами Unbounded.ttf и Onest.ttf]
import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[2]
FONTS = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "chestor_site/web/src/og/fonts"

W, H = 1280, 320

THEMES = {
    "human": {
        "bg": "#ffffff",
        "pattern": "rgba(51,144,236,0.10)",
        "glow": "rgba(51,144,236,0.14)",
        "title": "#0f0f0f",
        "text": "#5d6166",
        "accent": "#1665b5",
        "border": "#e3e5e8",
        "sclera": "#ffffff",
        "iris": "#3f8ddb",
        "pupil": "#0d1b2a",
        "outline": "#0f0f0f",
        "veins": None,
        "pupil_rx": 4,
    },
    "ghoul": {
        "bg": "#0e0b0c",
        "pattern": "rgba(214,31,60,0.09)",
        "glow": "rgba(226,32,63,0.22)",
        "title": "#f1e9ea",
        "text": "#a19295",
        "accent": "#ff4d66",
        "border": "#2a1f22",
        "sclera": "#050304",
        "iris": "#ff1f3d",
        "pupil": "#120003",
        "outline": "#e2203f",
        "veins": "#ff1f3d",
        "pupil_rx": 3.2,
    },
}


class Face:
    def __init__(self, path: Path) -> None:
        self.font = TTFont(path)
        self.glyphs = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()
        self.upm = self.font["head"].unitsPerEm

    def width(self, text: str, size: float, tracking: float = 0) -> float:
        scale = size / self.upm
        advances = [self.glyphs[self.cmap[ord(ch)]].width * scale for ch in text]
        return sum(advances) + tracking * (len(text) - 1)

    def path(self, text: str, x: float, y: float, size: float, tracking: float = 0) -> str:
        scale = size / self.upm
        pen = SVGPathPen(self.glyphs)
        for ch in text:
            glyph = self.glyphs[self.cmap[ord(ch)]]
            glyph.draw(TransformPen(pen, (scale, 0, 0, -scale, x, y)))
            x += glyph.width * scale + tracking
        return pen.getCommands()


def eye(theme: dict, cx: float, cy: float, scale: float) -> str:
    veins = ""
    if theme["veins"]:
        paths = "".join(
            f'<path d="{d}"/>'
            for d in (
                "M23 18 Q15 14 8 17",
                "M24 23 Q16 27 10 25",
                "M41 17 Q49 12 56 16",
                "M40 24 Q48 29 55 25",
                "M30 11 Q29 6 25 4",
                "M35 29 Q37 34 41 36",
            )
        )
        veins = f'<g class="veins" fill="none" stroke="{theme["veins"]}" stroke-width="1.1" stroke-linecap="round">{paths}</g>'
    return f"""
  <g transform="translate({cx - 32 * scale} {cy - 20 * scale}) scale({scale})">
    <g class="lid">
      <clipPath id="almond"><path d="M4 20 Q32 -6 60 20 Q32 46 4 20 Z"/></clipPath>
      <g clip-path="url(#almond)">
        <rect width="64" height="40" fill="{theme["sclera"]}"/>
        {veins}
        <circle class="iris" cx="32" cy="20" r="9.5" fill="{theme["iris"]}"/>
        <ellipse cx="32" cy="20" rx="{theme["pupil_rx"]}" ry="{4.8 if theme["veins"] else 4}" fill="{theme["pupil"]}"/>
        <circle cx="35.5" cy="16.5" r="1.8" fill="#ffffff" opacity="0.85"/>
      </g>
      <path d="M4 20 Q32 -6 60 20 Q32 46 4 20 Z" fill="none" stroke="{theme["outline"]}" stroke-width="2.2"/>
    </g>
  </g>"""


def pattern(theme: dict) -> str:
    # Фон как обои чата на сайте: редкие глифы Telegram и «Гуля».
    marks = []
    glyphs = [
        "M0 6 L14 0 L10 14 L7 9 Z",  # самолётик
        "M0 4 Q7 -4 14 4 Q7 12 0 4 Z",  # глаз
        "M2 0 L0 7 L2 14 M12 0 L14 7 L12 14",  # { }
        "M7 0 L9 5 L14 5 L10 8 L12 14 L7 10 L2 14 L4 8 L0 5 L5 5 Z",  # звезда
    ]
    step = 64
    for row in range(H // step + 1):
        for col in range(W // step + 1):
            if (row * 7 + col * 3) % 5:
                continue
            d = glyphs[(row + col) % len(glyphs)]
            x, y = col * step + (row % 2) * 32, row * step + 18
            marks.append(f'<path transform="translate({x} {y})" d="{d}"/>')
    return (
        f'<g fill="none" stroke="{theme["pattern"]}" stroke-width="1.6" stroke-linejoin="round">'
        + "".join(marks)
        + "</g>"
    )


def banner(name: str, theme: dict, display: Face, body: Face) -> str:
    left = 400
    title = display.path("CheStor", left, 150, 104, tracking=-2)
    line1 = body.path("Self · бэкенд на Python · Telegram Bot API", left, 205, 30)
    line2 = body.path("свой фреймворк, RPG-бот по «Токийскому гулю»", left, 245, 30)
    site = display.path("chestor.site", left, 290, 24, tracking=1)
    awaken = (
        """
    .iris { animation: pulse 3.2s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }
    .veins { animation: veins 3.2s ease-in-out infinite; }
    @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.12); } }
    @keyframes veins { 0%, 100% { opacity: 0.35; } 50% { opacity: 1; } }"""
        if theme["veins"]
        else ""
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="CheStor — Self: бэкенд на Python, Telegram Bot API, «Токийский гуль»">
  <style>
    .lid {{ animation: blink 6s infinite; transform-box: fill-box; transform-origin: center; }}
    @keyframes blink {{ 0%, 94%, 100% {{ transform: scaleY(1); }} 97% {{ transform: scaleY(0.08); }} }}{awaken}
    @media (prefers-reduced-motion: reduce) {{ .lid, .iris, .veins {{ animation: none; }} }}
  </style>
  <defs>
    <radialGradient id="glow-{name}" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{theme["glow"]}"/>
      <stop offset="1" stop-color="{theme["glow"]}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="24" fill="{theme["bg"]}"/>
  {pattern(theme)}
  <circle cx="200" cy="160" r="170" fill="url(#glow-{name})"/>
  {eye(theme, 200, 160, 4.2)}
  <path d="{title}" fill="{theme["title"]}"/>
  <path d="{line1}" fill="{theme["text"]}"/>
  <path d="{line2}" fill="{theme["text"]}"/>
  <path d="{site}" fill="{theme["accent"]}"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="23.5" fill="none" stroke="{theme["border"]}"/>
</svg>
"""


def main() -> None:
    display = Face(FONTS / "Unbounded.ttf")
    body = Face(FONTS / "Onest.ttf")
    out = ROOT / "assets"
    for name, theme in THEMES.items():
        (out / f"banner-{name}.svg").write_text(banner(name, theme, display, body), encoding="utf-8")
        print(f"assets/banner-{name}.svg")


if __name__ == "__main__":
    main()
