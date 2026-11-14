"""
VectorMotionEngine - Broadcast-Grade 2D Vector Motion Graphics & Physics Animation Engine
Replicates the visual and animation style of "The Curious Plot" ($20 -> $120,000 🍋)
with true 30fps frame-by-frame animation, live rolling number counters, falling coin physics,
moving conveyor bottling lines, and celebratory particle explosions.
"""

import os
import math
import random
import subprocess
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
from PIL import Image, ImageDraw, ImageFont

from app.config import TEMP_DIR, get_best_font


class VectorMotionEngine:
    def __init__(self):
        self.width = 1080
        self.height = 1920
        self.font_path = get_best_font()

        # Load fonts with clean sizing
        try:
            self.font_hero = ImageFont.truetype(self.font_path, 106)
            self.font_badge = ImageFont.truetype(self.font_path, 34)
            self.font_math = ImageFont.truetype(self.font_path, 40)
            self.font_tag = ImageFont.truetype(self.font_path, 18)
            self.font_hud = ImageFont.truetype(self.font_path, 26)
            self.font_tracker = ImageFont.truetype(self.font_path, 22)
            self.font_sub = ImageFont.truetype(self.font_path, 20)
            self.font_sign = ImageFont.truetype(self.font_path, 42)
        except Exception:
            self.font_hero = self.font_badge = self.font_math = self.font_tag = ImageFont.load_default()
            self.font_hud = self.font_tracker = self.font_sub = self.font_sign = ImageFont.load_default()

    def create_base_canvas(self) -> Image.Image:
        """Draws rich royal-violet radial spotlight background."""
        w, h = self.width, self.height
        bg = Image.new("RGBA", (w, h), (18, 10, 34, 255))
        draw_bg = ImageDraw.Draw(bg)
        cx, cy = w // 2, 400
        for r in range(1100, 0, -35):
            factor = 1.0 - (r / 1100)
            col = (
                int(18 + 48 * factor),
                int(10 + 22 * factor),
                int(34 + 68 * factor),
                255
            )
            draw_bg.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)

        # Ambient dust particles
        random.seed(42)
        for _ in range(25):
            px = random.randint(40, w - 40)
            py = random.randint(120, h - 300)
            pr = random.randint(2, 4)
            draw_bg.ellipse([px - pr, py - pr, px + pr, py + pr], fill=(253, 224, 71, 160))

        return bg

    def create_lemonade_stand_component(self) -> Image.Image:
        """Pre-renders detailed scalable Lemonade Stand."""
        stand_w, stand_h = 560, 500
        stand = Image.new("RGBA", (stand_w, stand_h), (0, 0, 0, 0))
        sd = ImageDraw.Draw(stand)
        # Poles
        sd.rectangle([50, 70, 66, 340], fill=(120, 53, 15))
        sd.rectangle([494, 70, 510, 340], fill=(120, 53, 15))
        # Awning
        sd.polygon([(30, 70), (530, 70), (550, 150), (10, 150)], fill=(185, 28, 28))
        for s in range(9):
            sx = 10 + s * 60
            scol = (239, 68, 68) if s % 2 == 0 else (255, 255, 255)
            sd.rectangle([sx, 70, sx + 60, 150], fill=scol)
            sd.chord([sx, 130, sx + 60, 175], start=0, end=180, fill=scol)
        # Countertop
        sd.rounded_rectangle([20, 330, 540, 370], radius=8, fill=(217, 119, 6), outline=(120, 53, 15), width=3)
        # Base Box
        sd.rounded_rectangle([40, 365, 520, 490], radius=12, fill=(253, 230, 138), outline=(180, 83, 9), width=4)
        # Plaque Sign
        sd.rounded_rectangle([80, 400, 480, 475], radius=16, fill=(255, 255, 255), outline=(15, 23, 42), width=5)
        sd.text((150, 415), "LEMONADE", font=self.font_sign, fill=(15, 23, 42))
        return stand

    def create_leo_component(self) -> Image.Image:
        """Pre-renders character Leo in navy suit."""
        leo = Image.new("RGBA", (300, 520), (0, 0, 0, 0))
        ld = ImageDraw.Draw(leo)
        # Legs & Shoes
        ld.rounded_rectangle([90, 320, 135, 500], radius=12, fill=(15, 23, 42))
        ld.rounded_rectangle([165, 320, 210, 500], radius=12, fill=(15, 23, 42))
        ld.rounded_rectangle([80, 490, 145, 515], radius=8, fill=(2, 6, 23))
        ld.rounded_rectangle([155, 490, 220, 515], radius=8, fill=(2, 6, 23))
        # Torso & Suit Jacket
        ld.rounded_rectangle([70, 180, 230, 340], radius=24, fill=(30, 41, 59))
        ld.polygon([(150, 180), (125, 230), (175, 230)], fill=(255, 255, 255))
        ld.polygon([(145, 210), (155, 210), (160, 300), (150, 320), (140, 300)], fill=(239, 68, 68))
        # Head & Face
        ld.rectangle([130, 140, 170, 190], fill=(254, 215, 170))
        ld.ellipse([85, 30, 215, 160], fill=(254, 215, 170), outline=(234, 88, 12), width=2)
        ld.chord([85, 15, 215, 125], start=180, end=360, fill=(69, 26, 3))
        # Eyes
        ld.ellipse([115, 85, 132, 102], fill=(15, 23, 42))
        ld.ellipse([122, 88, 128, 94], fill=(255, 255, 255))
        ld.ellipse([168, 85, 185, 102], fill=(15, 23, 42))
        ld.ellipse([175, 88, 181, 94], fill=(255, 255, 255))
        ld.arc([130, 110, 170, 140], start=20, end=160, fill=(154, 52, 18), width=4)
        return leo

    def render_animated_scene_clip(
        self,
        scene_num: int,
        duration: float,
        output_path: Path,
        fps: int = 30
    ) -> Path:
        """
        Renders complete, broadcast-quality frame-by-frame animated clip
        with rolling numbers, falling coins, moving graphics, and live HUD.
        """
        w, h = self.width, self.height
        total_frames = max(30, int(duration * fps))

        # Scene-specific parameters
        if scene_num == 1:
            start_val, end_val = 20, 120000
            level_name = "LEVEL 0: THE TRAP"
            formula_text = "$20 BUDGET = 80 CUPS"
            badge_sub = "100% TIME TRAPPED"
            theme_color = (14, 165, 233)
            theme_border = (56, 189, 248)
            active_step = 1
        elif scene_num == 2:
            start_val, end_val = 20, 80
            level_name = "LEVEL 1: LABOR"
            formula_text = "80 CUPS × $1 = $80 REVENUE"
            badge_sub = "SWEAT EQUITY"
            theme_color = (14, 165, 233)
            theme_border = (56, 189, 248)
            active_step = 1
        elif scene_num == 3:
            start_val, end_val = 80, 240
            level_name = "LEVEL 2: CAPITAL"
            formula_text = "3 STANDS × $40 = $120/DAY"
            badge_sub = "3 HIRED WORKERS (20% CUT)"
            theme_color = (16, 185, 129)
            theme_border = (52, 211, 153)
            active_step = 2
        elif scene_num == 4:
            start_val, end_val = 240, 3873
            level_name = "LEVEL 3: SYSTEMS"
            formula_text = "5 STORES × 200 BOTTLES = $3,873/MO"
            badge_sub = "AUTOMATED BOTTLING"
            theme_color = (245, 158, 11)
            theme_border = (251, 191, 36)
            active_step = 3
        else:
            start_val, end_val = 3873, 120000
            level_name = "LEVEL 4: DEALS"
            formula_text = "$40,000 EBITDA × 3X = $120,000"
            badge_sub = "FRANCHISE SALE EXIT"
            theme_color = (168, 85, 247)
            theme_border = (192, 132, 252)
            active_step = 4

        bg = self.create_base_canvas()
        stand = self.create_lemonade_stand_component()
        leo = self.create_leo_component()

        # Coin sprite
        coin = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
        cd = ImageDraw.Draw(coin)
        cd.ellipse([2, 2, 48, 48], fill=(250, 204, 21), outline=(202, 138, 4), width=3)
        cd.text((18, 10), "$", font=self.font_sub, fill=(113, 63, 18))

        # Coin rain physics
        random.seed(scene_num * 100 + 42)
        coins = [{"x": random.randint(220, 860), "y_start": random.randint(-400, -50), "speed": random.randint(320, 600)} for _ in range(12)]

        cmd = [
            "ffmpeg", "-y",
            "-f", "rawvideo",
            "-vcodec", "rawvideo",
            "-s", f"{w}x{h}",
            "-pix_fmt", "rgba",
            "-r", str(fps),
            "-i", "-",
            "-c:v", "libx264",
            "-preset", "veryfast",
            "-threads", "2",
            "-pix_fmt", "yuv420p",
            str(output_path)
        ]
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)

        for f in range(total_frames):
            t = f / float(fps)
            frame = bg.copy()
            draw = ImageDraw.Draw(frame)

            # 1. Top HUD
            # Brand Pill
            draw.rounded_rectangle([50, 60, 380, 125], radius=32, fill=(35, 24, 58, 220), outline=(255, 255, 255, 45), width=2)
            draw.ellipse([75, 84, 95, 104], fill=(250, 204, 21))
            draw.text((115, 78), "THE CURIOUS PLOT", font=self.font_hud, fill=(241, 245, 249))

            # Dynamic Rolling Number Counter (ease-out cubic over 1.8s)
            roll_p = min(1.0, t / 1.8)
            ease_p = 1.0 - math.pow(1.0 - roll_p, 3)
            cur_val = int(start_val + (end_val - start_val) * ease_p)
            wallet_str = f"${cur_val:,}"

            # Wallet Pill
            draw.rounded_rectangle([720, 60, 1030, 125], radius=32, fill=(245, 158, 11, 70), outline=(245, 158, 11, 150), width=2)
            draw.text((750, 78), f"💰 {wallet_str}", font=self.font_hud, fill=(254, 240, 138))

            # 2. Hero Headline (Big Rolling Numbers with 3D drop shadow)
            hero_display = wallet_str if scene_num > 1 else f"${start_val} ➔ ${end_val:,}"
            h_bb = draw.textbbox((0, 0), hero_display, font=self.font_hero)
            hw = h_bb[2] - h_bb[0]
            hx = (w - hw) // 2
            for off in range(10, 0, -2):
                draw.text((hx, 175 + off), hero_display, font=self.font_hero, fill=(0, 0, 0, 220))
            draw.text((hx, 175), hero_display, font=self.font_hero, fill=(250, 204, 21))

            # 3. Level Badge
            draw.rounded_rectangle([(w - 460)//2, 315, (w + 460)//2, 385], radius=35, fill=theme_color, outline=theme_border, width=3)
            b_bb = draw.textbbox((0, 0), level_name, font=self.font_badge)
            bw = b_bb[2] - b_bb[0]
            draw.text(((w - bw)//2, 330), level_name, font=self.font_badge, fill=(255, 255, 255))

            # 4. Glassmorphic Formula Card
            card_x, card_y, card_w, card_h = 80, 420, 920, 130
            draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=28, fill=(255, 255, 255, 245), outline=(255, 255, 255), width=3)
            draw.text((card_x + 35, card_y + 22), "ACTIVE EQUATION", font=self.font_tag, fill=(37, 99, 235))
            draw.text((card_x + 35, card_y + 55), formula_text, font=self.font_math, fill=(15, 23, 42))
            
            sub_bb = draw.textbbox((0, 0), badge_sub, font=self.font_sub)
            sw = sub_bb[2] - sub_bb[0] + 40
            draw.rounded_rectangle([card_x + card_w - sw - 20, card_y + 35, card_x + card_w - 20, card_y + 95], radius=16, fill=(219, 234, 254))
            draw.text((card_x + card_w - sw, card_y + 52), badge_sub, font=self.font_sub, fill=(30, 64, 175))

            # 5. Center Stage Dynamic Graphics per Scene
            leo_bob = int(math.sin(t * 3.5) * 8)

            if scene_num in [1, 2]:
                # Single Stand + Bobbing Leo
                frame.paste(leo, (180, 840 + leo_bob), leo)
                frame.paste(stand, (460, 870), stand)
                # Falling Coins Rain
                for c in coins:
                    cy = int(c["y_start"] + t * c["speed"])
                    if cy < 1300:
                        frame.paste(coin, (c["x"], cy), coin)

            elif scene_num == 3:
                # 3 Branch Stands side by side popping in
                for i in range(3):
                    # Staggered pop-in bounce
                    pop_delay = i * 0.3
                    if t >= pop_delay:
                        stand_scale = min(1.0, (t - pop_delay) / 0.4)
                        sx = 80 + i * 320
                        # Scaled small stand
                        s_small = stand.resize((300, 270), Image.Resampling.LANCZOS)
                        frame.paste(s_small, (sx, 920), s_small)
                        draw.rounded_rectangle([sx + 60, 860, sx + 240, 905], radius=12, fill=(16, 185, 129))
                        draw.text((sx + 85, 872), f"STAND #{i+1}", font=self.font_sub, fill=(255, 255, 255))
                        draw.text((sx + 85, 1210), "$40 PROFIT", font=self.font_tracker, fill=(250, 204, 21))

            elif scene_num == 4:
                # Systems: Moving Conveyor Bottling Line
                conv_y = 1000
                draw.rectangle([100, conv_y, 980, conv_y + 40], fill=(71, 85, 105))
                # Animated conveyor stripes sliding right
                shift = int((t * 220) % 60)
                for cx_line in range(100 + shift, 980, 60):
                    draw.line([(cx_line, conv_y), (cx_line - 15, conv_y + 40)], fill=(30, 41, 59), width=4)

                # Bottles sliding along conveyor
                bottle = Image.new("RGBA", (90, 160), (0, 0, 0, 0))
                bd = ImageDraw.Draw(bottle)
                bd.rounded_rectangle([15, 30, 75, 150], radius=16, fill=(250, 204, 21), outline=(255, 255, 255), width=3)
                bd.rectangle([35, 10, 55, 30], fill=(202, 138, 4))
                bd.rounded_rectangle([25, 70, 65, 110], radius=6, fill=(255, 255, 255))
                bd.text((32, 82), "LEMON", font=self.font_tag, fill=(15, 23, 42))

                for b_idx in range(5):
                    bx = int(120 + ((b_idx * 180 + t * 220) % 800))
                    frame.paste(bottle, (bx, conv_y - 145), bottle)

            else:
                # Level 4: Lemon Corp Skyscraper + Golden Confetti Burst
                hq_w, hq_h = 480, 400
                hx = (w - hq_w) // 2
                hy = 850
                draw.rounded_rectangle([hx, hy, hx + hq_w, hy + hq_h], radius=18, fill=(30, 58, 138), outline=(96, 165, 250), width=6)
                draw.polygon([(hx - 20, hy), (hx + hq_w + 20, hy), (w // 2, hy - 80)], fill=(250, 204, 21), outline=(120, 53, 15), width=4)
                draw.rounded_rectangle([hx + 70, hy + 30, hx + hq_w - 70, hy + 105], radius=16, fill=(255, 255, 255), outline=(15, 23, 42), width=4)
                draw.text((hx + 120, hy + 48), "LEMON CORP", font=self.font_sign, fill=(15, 23, 42))

                # Office windows grid
                for wx in range(hx + 40, hx + hq_w - 40, 75):
                    for wy in range(hy + 130, hy + hq_h - 40, 60):
                        draw.rounded_rectangle([wx, wy, wx + 50, wy + 42], radius=6, fill=(254, 240, 138))

                # Confetti particles bursting radially
                for p_idx in range(24):
                    angle = (p_idx / 24.0) * 2 * math.pi
                    dist = (t * 280) % 450
                    px = int(w // 2 + math.cos(angle) * dist)
                    py = int(hy + 150 + math.sin(angle) * dist)
                    if 0 <= px < w and 0 <= py < h:
                        pcol = [(250, 204, 21), (239, 68, 68), (14, 165, 233), (16, 185, 129)][p_idx % 4]
                        draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=pcol)

            # 6. Bottom 4-Stage Progress Tracker
            bar_x, bar_y, bar_w = 50, 1750, 980
            draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + 110], radius=28, fill=(15, 7, 32, 210), outline=(255, 255, 255, 30), width=2)
            step_w = (bar_w - 50) // 4
            labels = ["LABOR", "CAPITAL", "SYSTEMS", "DEALS"]
            for s in range(4):
                sx = bar_x + 10 + s * (step_w + 10)
                is_active = (s == (active_step - 1))
                if is_active:
                    pulse = 0.85 + 0.15 * math.sin(t * 6.0)
                    draw.rounded_rectangle([sx, bar_y + 10, sx + step_w, bar_y + 100], radius=20, fill=theme_color, outline=theme_border, width=3)
                    draw.text((sx + 20, bar_y + 22), f"STEP {s+1}", font=self.font_tag, fill=(255, 255, 255))
                    draw.text((sx + 20, bar_y + 50), labels[s], font=self.font_tracker, fill=(255, 255, 255))
                else:
                    draw.rounded_rectangle([sx, bar_y + 10, sx + step_w, bar_y + 100], radius=20, fill=(255, 255, 255, 12))
                    draw.text((sx + 20, bar_y + 22), f"STEP {s+1}", font=self.font_tag, fill=(255, 255, 255, 100))
                    draw.text((sx + 20, bar_y + 50), labels[s], font=self.font_tracker, fill=(255, 255, 255, 100))

            proc.stdin.write(frame.tobytes())

        proc.stdin.close()
        proc.wait()
        return output_path
