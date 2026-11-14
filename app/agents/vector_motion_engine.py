"""
VectorMotionEngine - High-Retention 2D Vector Infographic & Business Metaphor Engine
Replicates the visual and animation style of "The Curious Plot" ($20 -> $120,000 🍋)
with pixel-perfect 1080x1920 vector rendering, 4-tier leverage stage tracker,
hero typography with 3D drop shadow, formula cards, and animated props.
"""

import math
import random
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from app.config import TEMP_DIR, get_best_font, VIDEO_CONFIGS


class VectorMotionEngine:
    def __init__(self):
        self.font_path = get_best_font()
        self.width = 1080
        self.height = 1920

        # Load fonts with fallbacks
        try:
            self.font_hero = ImageFont.truetype(self.font_path, 96)
            self.font_hero_sm = ImageFont.truetype(self.font_path, 80)
            self.font_badge = ImageFont.truetype(self.font_path, 40)
            self.font_card = ImageFont.truetype(self.font_path, 44)
            self.font_brand = ImageFont.truetype(self.font_path, 28)
            self.font_sub = ImageFont.truetype(self.font_path, 24)
            self.font_nav = ImageFont.truetype(self.font_path, 28)
        except Exception:
            self.font_hero = self.font_hero_sm = self.font_badge = ImageFont.load_default()
            self.font_card = self.font_brand = self.font_sub = self.font_nav = ImageFont.load_default()

    def draw_background_spotlight(self, draw: ImageDraw.Draw, img: Image.Image):
        """Draws deep indigo-purple radial spotlight with upward radiating light beams."""
        w, h = self.width, self.height
        cx, cy = w // 2, 420

        # Radial glow from top center
        for r in range(950, 0, -25):
            factor = 1.0 - (r / 950)
            col = (
                int(16 + 50 * factor),
                int(10 + 28 * factor),
                int(32 + 75 * factor)
            )
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)

        # Radiating spotlight rays
        ray_overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        rdraw = ImageDraw.Draw(ray_overlay)
        for angle in range(-45, 50, 15):
            rad = math.radians(angle)
            x1 = cx + math.sin(rad) * 1700
            y1 = math.cos(rad) * 1700
            rdraw.polygon(
                [(cx - 30, 0), (cx + 30, 0), (x1 + 70, y1), (x1 - 70, y1)],
                fill=(255, 255, 255, 14)
            )

        # Tiny floating dust / star particles
        random.seed(42)
        for _ in range(35):
            px = random.randint(40, w - 40)
            py = random.randint(120, h - 300)
            pr = random.randint(2, 4)
            p_alpha = random.randint(40, 160)
            rdraw.ellipse([px - pr, py - pr, px + pr, py + pr], fill=(255, 255, 255, p_alpha))

        img.paste(
            Image.alpha_composite(Image.new("RGBA", (w, h), (0, 0, 0, 0)), ray_overlay).convert("RGB"),
            (0, 0),
            ray_overlay
        )

        # Horizon / Ground
        ground_y = 1260
        draw.rectangle([0, ground_y, w, h], fill=(22, 14, 38))
        draw.line([(0, ground_y), (w, ground_y)], fill=(48, 34, 80), width=3)

    def draw_top_header(self, draw: ImageDraw.Draw, brand_name: str, wallet_amount: str):
        """Draws [● BRAND] on top-left and live [$WALLET] on top-right."""
        w = self.width
        # Brand Pill
        pill_w = 400
        draw.rounded_rectangle([40, 50, 40 + pill_w, 114], radius=32, fill=(35, 24, 58), outline=(68, 50, 102), width=2)
        draw.ellipse([68, 74, 90, 96], fill=(255, 212, 0))
        clean_brand = brand_name.upper()[:18]
        draw.text((105, 70), clean_brand, font=self.font_brand, fill=(255, 255, 255))

        # Wallet Pill (Bright Yellow with black bold numbers)
        w_pill_w = 210
        wx = w - 40 - w_pill_w
        draw.rounded_rectangle([wx, 50, w - 40, 114], radius=32, fill=(255, 212, 0), outline=(255, 235, 120), width=2)
        w_bbox = draw.textbbox((0, 0), wallet_amount, font=self.font_brand)
        ww = w_bbox[2] - w_bbox[0]
        draw.text((wx + (w_pill_w - ww) // 2, 70), wallet_amount, font=self.font_brand, fill=(20, 14, 30))

    def draw_hero_text(self, draw: ImageDraw.Draw, hero_text: str, y_pos: int = 270):
        """Draws big bold hero typography with 8px dark cartoon stroke and 3D shadow."""
        w = self.width
        f = self.font_hero if len(hero_text) <= 12 else self.font_hero_sm
        bbox = draw.textbbox((0, 0), hero_text, font=f)
        tw = bbox[2] - bbox[0]
        hx = (w - tw) // 2

        # 3D shadow & dark outline
        stroke_color = (20, 12, 32)
        shadow_offset = 7
        for dx in range(-7, 8):
            for dy in range(-7, 8):
                if dx * dx + dy * dy <= 56:
                    draw.text((hx + dx, y_pos + dy + shadow_offset), hero_text, font=f, fill=stroke_color)

        for dx in range(-7, 8):
            for dy in range(-7, 8):
                if dx * dx + dy * dy <= 49:
                    draw.text((hx + dx, y_pos + dy), hero_text, font=f, fill=stroke_color)

        # Foreground Yellow
        draw.text((hx, y_pos), hero_text, font=f, fill=(255, 212, 0))

    def draw_level_badge(self, draw: ImageDraw.Draw, level_str: str, y_pos: int = 420):
        """Draws rounded gradient badge: LEVEL 1: LABOR / LEVEL 2: CAPITAL etc."""
        w = self.width
        colors = {
            "1": ((59, 130, 246), (147, 197, 253)),   # Blue
            "2": ((16, 185, 129), (110, 231, 183)),   # Green
            "3": ((139, 92, 246), (196, 181, 253)),   # Purple
            "4": ((245, 158, 11), (253, 230, 138)),   # Amber/Gold
        }
        key = "1"
        for k in ["1", "2", "3", "4"]:
            if k in level_str:
                key = k
                break
        bg_col, border_col = colors.get(key, ((59, 130, 246), (147, 197, 253)))

        badge_w, badge_h = 480, 86
        bx = (w - badge_w) // 2
        draw.rounded_rectangle([bx, y_pos, bx + badge_w, y_pos + badge_h], radius=43, fill=bg_col, outline=border_col, width=3)
        lbox = draw.textbbox((0, 0), level_str.upper(), font=self.font_badge)
        lw = lbox[2] - lbox[0]
        draw.text(((w - lw) // 2, y_pos + 18), level_str.upper(), font=self.font_badge, fill=(255, 255, 255))

    def draw_formula_card(self, draw: ImageDraw.Draw, formula_text: str, y_pos: int = 535, accent_color: Tuple[int, int, int] = (34, 197, 94)):
        """Draws crisp white formula / math equation card."""
        w = self.width
        cw, ch = 600, 100
        cx = (w - cw) // 2
        # Clean white card with dark outline
        draw.rounded_rectangle([cx, y_pos, cx + cw, y_pos + ch], radius=50, fill=(255, 255, 255), outline=(24, 16, 38), width=4)
        cbox = draw.textbbox((0, 0), formula_text.upper(), font=self.font_card)
        cw_text = cbox[2] - cbox[0]
        draw.text(((w - cw_text) // 2, y_pos + 24), formula_text.upper(), font=self.font_card, fill=accent_color)

    def draw_character(self, draw: ImageDraw.Draw, cx: int, cy: int, suit_color: Tuple[int, int, int] = (45, 65, 110), scale: float = 1.0):
        """Draws cute flat-vector character 'Leo' with head, hair, smiling face, blazer suit, and limbs."""
        r_head = int(48 * scale)
        # Head & Face
        draw.ellipse([cx - r_head, cy - r_head * 2, cx + r_head, cy], fill=(235, 185, 150), outline=(24, 16, 38), width=3)
        # Hair cap
        draw.pieslice([cx - r_head - 2, cy - r_head * 2 - 4, cx + r_head + 2, cy - 20], 180, 360, fill=(50, 35, 25), outline=(24, 16, 38), width=3)
        # Eyes
        eye_offset = int(18 * scale)
        eye_y = int(cy - r_head - 5 * scale)
        draw.ellipse([cx - eye_offset - 4, eye_y, cx - eye_offset + 4, eye_y + 8], fill=(24, 16, 38))
        draw.ellipse([cx + eye_offset - 4, eye_y, cx + eye_offset + 4, eye_y + 8], fill=(24, 16, 38))
        # Smile
        draw.arc([cx - 15, cy - r_head + 5, cx + 15, cy - r_head + 25], 20, 160, fill=(24, 16, 38), width=3)

        # Torso (Suit Jacket)
        tw = int(44 * scale)
        th = int(105 * scale)
        draw.rounded_rectangle([cx - tw, cy, cx + tw, cy + th], radius=16, fill=suit_color, outline=(24, 16, 38), width=3)
        # White shirt collar & tie
        draw.polygon([(cx - 14, cy), (cx + 14, cy), (cx, cy + 22)], fill=(255, 255, 255))
        draw.polygon([(cx - 6, cy + 22), (cx + 6, cy + 22), (cx, cy + 55)], fill=(239, 68, 68))

        # Legs & Shoes
        leg_w = int(14 * scale)
        leg_h = int(80 * scale)
        draw.rectangle([cx - tw + 6, cy + th, cx - tw + 6 + leg_w, cy + th + leg_h], fill=(30, 42, 65), outline=(24, 16, 38), width=3)
        draw.rectangle([cx + tw - 6 - leg_w, cy + th, cx + tw - 6, cy + th + leg_h], fill=(30, 42, 65), outline=(24, 16, 38), width=3)
        draw.ellipse([cx - tw + 2, cy + th + leg_h - 10, cx - tw + 24, cy + th + leg_h + 10], fill=(20, 20, 25))
        draw.ellipse([cx + tw - 24, cy + th + leg_h - 10, cx + tw - 2, cy + th + leg_h + 10], fill=(20, 20, 25))

    def draw_lemonade_stand(self, draw: ImageDraw.Draw, sx: int, sy: int, sw: int = 270, sh: int = 290, label: str = "LEMON"):
        """Draws cute striped lemonade stall with awning, wooden counter, and glass lemonade jar."""
        # Main White Stall Body
        draw.rectangle([sx, sy + 100, sx + sw, sy + sh], fill=(255, 255, 255), outline=(24, 16, 38), width=4)
        # Counter Wooden Ledge
        draw.rectangle([sx - 12, sy + 85, sx + sw + 12, sy + 104], fill=(195, 145, 95), outline=(24, 16, 38), width=4)

        # Lemonade Jar with Tap on Counter
        jar_w, jar_h = 75, 80
        jx = sx + (sw - jar_w) // 2
        jy = sy + 5
        draw.rounded_rectangle([jx, jy, jx + jar_w, jy + jar_h], radius=14, fill=(255, 212, 0), outline=(24, 16, 38), width=4)
        draw.rectangle([jx + 15, jy - 10, jx + jar_w - 15, jy], fill=(175, 125, 75), outline=(24, 16, 38), width=3)
        # Lemon slice detail in jar
        draw.ellipse([jx + 25, jy + 25, jx + 50, jy + 50], fill=(255, 240, 100), outline=(24, 16, 38), width=2)

        # Scalloped Striped Awning
        stripes = 6
        stripe_w = (sw + 24) / stripes
        aw_h = 70
        for st in range(stripes):
            st_x = (sx - 12) + st * stripe_w
            col = (239, 68, 68) if st % 2 == 0 else (255, 255, 255)
            draw.rectangle([st_x, sy - 15, st_x + stripe_w, sy + aw_h], fill=col, outline=(24, 16, 38), width=3)

        # Top Badge (e.g. LEMON)
        badge_bw = 140
        bx = sx + (sw - badge_bw) // 2
        draw.rounded_rectangle([bx, sy - 52, bx + badge_bw, sy - 14], radius=14, fill=(255, 212, 0), outline=(24, 16, 38), width=3)
        draw.text((bx + 25, sy - 45), label, font=self.font_sub, fill=(24, 16, 38))

    def draw_falling_coins(self, draw: ImageDraw.Draw, count: int = 6):
        """Draws sparkling 2D gold coins falling through the spotlight."""
        random.seed( count * 17)
        for i in range(count):
            cx = random.randint(300, 780)
            cy = random.randint(670, 1150)
            cr = 26
            # Gold coin
            draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=(255, 212, 0), outline=(190, 145, 0), width=3)
            draw.ellipse([cx - cr + 4, cy - cr + 4, cx + cr - 4, cy + cr - 4], outline=(255, 245, 140), width=1)
            draw.text((cx - 8, cy - 16), "$", font=self.font_brand, fill=(160, 115, 0))

    def draw_bottom_stage_tracker(self, draw: ImageDraw.Draw, active_index: int = 1):
        """Draws 4-stage progression tracker: [1 LABOR] [2 CAPITAL] [3 SYSTEMS] [4 DEALS] with active glow."""
        w = self.width
        navs = ["1 LABOR", "2 CAPITAL", "3 SYSTEMS", "4 DEALS"]
        pill_w = 224
        gap = 18
        total_w = 4 * pill_w + 3 * gap
        start_x = (w - total_w) // 2
        ny = 1760

        colors = [
            (59, 130, 246),   # 1 Labor (Blue)
            (16, 185, 129),   # 2 Capital (Green)
            (139, 92, 246),   # 3 Systems (Purple)
            (245, 158, 11),   # 4 Deals (Gold)
        ]

        for i, nav in enumerate(navs):
            px = start_x + i * (pill_w + gap)
            is_active = (i + 1 == active_index)
            if is_active:
                bg_col = colors[i]
                border_col = (255, 255, 255)
                text_col = (255, 255, 255)
                draw.rounded_rectangle([px, ny, px + pill_w, ny + 78], radius=39, fill=bg_col, outline=border_col, width=3)
            else:
                bg_col = (34, 25, 52)
                border_col = (58, 44, 82)
                text_col = (130, 120, 155)
                draw.rounded_rectangle([px, ny, px + pill_w, ny + 78], radius=39, fill=bg_col, outline=border_col, width=2)

            nbox = draw.textbbox((0, 0), nav, font=self.font_nav)
            nw = nbox[2] - nbox[0]
            draw.text((px + (pill_w - nw) // 2, ny + 20), nav, font=self.font_nav, fill=text_col)

    def render_scene_frame(
        self,
        brand_name: str,
        wallet_amount: str,
        hero_text: str,
        level_str: str,
        formula_text: str,
        active_level: int,
        scene_type: str = "labor",
        output_path: Optional[Path] = None
    ) -> Path:
        """
        Renders complete, razor-sharp 1080x1920 2D vector infographic frame.
        """
        w, h = self.width, self.height
        img = Image.new("RGB", (w, h), (18, 12, 32))
        draw = ImageDraw.Draw(img)

        # 1. Background & Spotlight
        self.draw_background_spotlight(draw, img)
        draw = ImageDraw.Draw(img)

        # 2. Top Header (Brand + Wallet)
        self.draw_top_header(draw, brand_name=brand_name, wallet_amount=wallet_amount)

        # 3. Hero Typography ($20 -> $120,000 or $80 or $3,873)
        self.draw_hero_text(draw, hero_text=hero_text, y_pos=260)

        # 4. Level Badge (LEVEL 1: LABOR)
        self.draw_level_badge(draw, level_str=level_str, y_pos=410)

        # 5. Formula / Equation Card ($20 = 80 CUPS)
        if formula_text:
            self.draw_formula_card(draw, formula_text=formula_text, y_pos=525)

        # 6. Props & Characters based on scene_type / level
        ground_y = 1260
        if active_level == 1:
            # 1 Stand + Leo
            self.draw_character(draw, cx=330, cy=ground_y - 210, scale=1.0)
            self.draw_lemonade_stand(draw, sx=540, sy=ground_y - 300, sw=280, sh=300)
            self.draw_falling_coins(draw, count=4)
        elif active_level == 2:
            # 3 Stands + 3 Helpers
            sw = 210
            sh = 240
            spacing = 330
            for i in range(3):
                sx = 75 + i * spacing
                self.draw_character(draw, cx=sx - 20, cy=ground_y - 170, suit_color=(50, 110, 80), scale=0.82)
                self.draw_lemonade_stand(draw, sx=sx, sy=ground_y - 250, sw=sw, sh=sh)
            self.draw_falling_coins(draw, count=8)
        elif active_level == 3:
            # 5 Shops + Bottles / Recipe Guide
            sw = 160
            sh = 200
            spacing = 205
            for i in range(5):
                sx = 35 + i * spacing
                self.draw_lemonade_stand(draw, sx=sx, sy=ground_y - 220, sw=sw, sh=sh, label=f"SHOP {i+1}")
            # Floating Recipe Guide Card in Center
            self.draw_falling_coins(draw, count=12)
        elif active_level == 4:
            # Corporate Franchise Valuation / Deal Exit
            hq_w, hq_h = 560, 420
            hx = (w - hq_w) // 2
            hy = ground_y - hq_h
            # Glass skyscraper / headquarters
            draw.rectangle([hx, hy, hx + hq_w, hy + hq_h], fill=(35, 45, 75), outline=(24, 16, 38), width=5)
            # Golden Awning / Roof
            draw.polygon([(hx - 30, hy), (hx + hq_w + 30, hy), (w // 2, hy - 80)], fill=(245, 158, 11), outline=(24, 16, 38), width=4)
            # Golden sign
            draw.rounded_rectangle([hx + 80, hy + 40, hx + hq_w - 80, hy + 120], radius=20, fill=(255, 212, 0), outline=(24, 16, 38), width=4)
            f_sign = ImageFont.truetype(self.font_path, 40)
            draw.text((hx + 120, hy + 55), "LEMON CORP", font=f_sign, fill=(20, 14, 30))
            # Grid windows
            for wx in range(hx + 40, hx + hq_w - 40, 80):
                for wy in range(hy + 150, hy + hq_h - 40, 60):
                    draw.rectangle([wx, wy, wx + 50, wy + 40], fill=(255, 235, 120), outline=(24, 16, 38), width=2)
            # 4 Characters celebrating
            for i in range(4):
                self.draw_character(draw, cx=160 + i * 250, cy=ground_y - 190, suit_color=(45 + i*15, 60, 120), scale=0.9)
            self.draw_falling_coins(draw, count=18)
        else:
            # Intro Hook: Large Lemonade Stand with Spotlight
            self.draw_character(draw, cx=320, cy=ground_y - 210, scale=1.05)
            self.draw_lemonade_stand(draw, sx=520, sy=ground_y - 320, sw=320, sh=320)
            self.draw_falling_coins(draw, count=6)

        # 7. Bottom 4-Stage Navigation Tracker
        self.draw_bottom_stage_tracker(draw, active_index=max(1, min(4, active_level)))

        if output_path is None:
            output_path = TEMP_DIR / f"curious_frame_{active_level}.png"

        img.save(output_path, "PNG")
        return output_path

    def render_scene_clip(
        self,
        frame_image_path: Path,
        duration: float,
        output_clip_path: Path,
        fps: int = 30
    ) -> Path:
        """
        Renders a single scene into an animated video clip with subtle bounce / zoom motion
        using 2 CPU threads for silent, hardware-safe execution.
        """
        total_frames = int(duration * fps)
        # Gentle dynamic float / zoom
        vf = f"zoompan=z='min(zoom+0.0012,1.08)':d={total_frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={self.width}x{self.height}:fps={fps}"

        cmd = [
            "ffmpeg", "-y",
            "-loop", "1",
            "-i", str(frame_image_path),
            "-vf", vf,
            "-t", str(duration),
            "-c:v", "libx264",
            "-preset", "veryfast",
            "-threads", "2",
            "-pix_fmt", "yuv420p",
            str(output_clip_path)
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            raise RuntimeError(f"Vector clip render failed: {res.stderr}")

        return output_clip_path
