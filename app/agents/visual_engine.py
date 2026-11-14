"""
VisualEngine - Multi-Style Visual Director (Zack D. 3D Simulation & Magnates Media 4K B-Roll)
Combines real 1080p stock video footage, 3D anatomical mannequin rendering,
and animated medical telemetry HUD overlays for high-retention YouTube Shorts.
"""

import urllib.parse
from pathlib import Path
from typing import List, Optional
import requests
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from app.config import TEMP_DIR, OUTPUT_DIR, VIDEO_CONFIGS, get_best_font
from app.agents.retention_writer import ScriptScene
from app.agents.stock_director import StockDirector


class VisualEngine:
    def __init__(self):
        self.font_path = get_best_font()
        self.stock_director = StockDirector()

    def generate_procedural_simulation_canvas(
        self,
        width: int,
        height: int,
        scene_num: int,
        on_screen_text: str,
        output_path: Path
    ) -> Path:
        """
        Creates a high-tech Zack D. Films style 3D medical / forensic simulation canvas.
        Draws clinical dark-grid background, glowing anatomical mannequin silhouette,
        and biometric telemetry monitors.
        """
        img = Image.new("RGB", (width, height), color=(10, 14, 22))
        draw = ImageDraw.Draw(img)

        # 1. Subtle 3D Perspective Floor / Grid
        grid_color = (25, 38, 55)
        # Vertical grid lines converging
        for x in range(0, width, 80):
            draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
        for y in range(0, height, 80):
            draw.line([(0, y), (width, y)], fill=grid_color, width=1)

        # 2. Glowing Anatomical Mannequin Silhouette in Center
        cx, cy = width // 2, height // 2 + 50
        # Head / Skull
        draw.ellipse([cx - 90, cy - 380, cx + 90, cy - 200], fill=(50, 65, 85), outline=(0, 220, 255), width=3)
        # Neck & Spine
        draw.rectangle([cx - 30, cy - 200, cx + 30, cy - 130], fill=(40, 55, 75))
        # Torso / Ribcage
        draw.polygon([
            (cx - 180, cy - 130), (cx + 180, cy - 130),
            (cx + 130, cy + 180), (cx - 130, cy + 180)
        ], fill=(35, 48, 68), outline=(0, 220, 255), width=3)

        # Glowing internal spine / vertebrae (Zack D. cross-section look)
        for vy in range(cy - 120, cy + 160, 35):
            draw.rectangle([cx - 24, vy, cx + 24, vy + 20], fill=(0, 220, 255), outline=(255, 255, 255), width=1)

        # Glowing heart / organ stress indicator
        draw.ellipse([cx - 80, cy - 70, cx - 20, cy - 10], fill=(240, 40, 40), outline=(255, 220, 0), width=3)

        # Pelvis & Limbs
        draw.polygon([(cx - 130, cy + 180), (cx + 130, cy + 180), (cx + 90, cy + 280), (cx - 90, cy + 280)], fill=(30, 42, 60))
        draw.rectangle([cx - 110, cy + 280, cx - 40, cy + 550], fill=(45, 58, 78), outline=(0, 220, 255), width=2)
        draw.rectangle([cx + 40, cy + 280, cx + 110, cy + 550], fill=(45, 58, 78), outline=(0, 220, 255), width=2)

        # 3. Biometric Telemetry Panels
        try:
            font_hud = ImageFont.truetype(self.font_path, 32)
            font_small = ImageFont.truetype(self.font_path, 20)
            font_alert = ImageFont.truetype(self.font_path, 48)
        except Exception:
            font_hud = ImageFont.load_default()
            font_small = ImageFont.load_default()
            font_alert = ImageFont.load_default()

        # Top status bar
        draw.rectangle([40, 60, width - 40, 130], fill=(15, 23, 38), outline=(0, 220, 255), width=2)
        draw.text((60, 75), f"BIOMECHANICAL SIMULATION // SEQUENCE 0{scene_num}", font=font_hud, fill=(0, 220, 255))
        draw.text((60, 105), "OCTANE PHYSICS ENGINE • 60 FPS • SKELETAL RIG ACTIVE", font=font_small, fill=(160, 185, 210))

        # Right telemetry readout
        draw.rectangle([width - 320, 160, width - 40, 360], fill=(12, 18, 30), outline=(50, 70, 95), width=1)
        draw.text((width - 300, 180), "HEART RATE: 168 BPM", font=font_small, fill=(255, 60, 60))
        draw.text((width - 300, 215), "SPO2: 82% [CRITICAL]", font=font_small, fill=(255, 180, 0))
        draw.text((width - 300, 250), "LUMBAR STRESS: 420 kPa", font=font_small, fill=(255, 60, 60))
        draw.text((width - 300, 285), "LACTIC ACID: 14.8 mmol/L", font=font_small, fill=(255, 180, 0))
        draw.text((width - 300, 320), "STATUS: TISSUE FAILURE", font=font_small, fill=(255, 255, 255))

        # Animated-style ECG Heartbeat Line
        ecg_points = [
            (60, 300), (120, 300), (140, 270), (160, 340), (180, 250),
            (200, 310), (220, 300), (320, 300), (340, 270), (360, 340),
            (380, 250), (400, 310), (420, 300), (500, 300)
        ]
        for i in range(len(ecg_points) - 1):
            draw.line([ecg_points[i], ecg_points[i+1]], fill=(0, 255, 160), width=3)

        # 4. Central Zack D. Callout Banner
        if on_screen_text:
            badge_text = on_screen_text.upper()
            bbox = draw.textbbox((0, 0), badge_text, font=font_alert)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            bx = (width - tw) // 2
            by = height - 360

            # Warning banner in neon amber & dark red
            pad_x, pad_y = 35, 18
            draw.rectangle(
                [bx - pad_x, by - pad_y, bx + tw + pad_x, by + th + pad_y],
                fill=(180, 15, 15),
                outline=(255, 230, 0),
                width=4
            )
            # Drop shadow
            draw.text((bx + 3, by + 3), badge_text, font=font_alert, fill=(0, 0, 0))
            draw.text((bx, by), badge_text, font=font_alert, fill=(255, 255, 255))

        img.save(output_path, "JPEG", quality=94)
        return output_path

    def overlay_hud_telemetry(self, image_path: Path, on_screen_text: str, scene_num: int) -> Path:
        """
        Overlays Zack D. Films style 3D medical / forensic HUD telemetry onto AI images.
        """
        try:
            img = Image.open(image_path).convert("RGBA")
            draw = ImageDraw.Draw(img)
            w, h = img.size

            try:
                font_hud = ImageFont.truetype(self.font_path, 42)
                font_small = ImageFont.truetype(self.font_path, 22)
            except Exception:
                font_hud = ImageFont.load_default()
                font_small = ImageFont.load_default()

            # Medical warning banner in upper-middle area
            if on_screen_text:
                badge_text = on_screen_text.upper()
                bbox = draw.textbbox((0, 0), badge_text, font=font_hud)
                tw = bbox[2] - bbox[0]
                th = bbox[3] - bbox[1]
                tx = (w - tw) // 2
                ty = int(h * 0.18)

                pad_x, pad_y = 25, 14
                # Dark red warning backing
                draw.rectangle(
                    [tx - pad_x, ty - pad_y, tx + tw + pad_x, ty + th + pad_y],
                    fill=(190, 20, 20, 225),
                    outline=(255, 230, 0, 255),
                    width=4
                )
                draw.text((tx, ty), badge_text, font=font_hud, fill=(255, 255, 255, 255))

                # Telemetry header label
                sub_label = f"SIMULATION ANALYSIS // BEAT 0{scene_num}"
                draw.text((tx - pad_x, ty - pad_y - 28), sub_label, font=font_small, fill=(255, 230, 0, 255))

            # Target Reticle Crosshair in center
            cx, cy = w // 2, h // 2
            reticle_color = (0, 220, 255, 180)
            draw.arc([cx - 80, cy - 80, cx + 80, cy + 80], 0, 360, fill=reticle_color, width=2)
            draw.line([(cx - 100, cy), (cx - 40, cy)], fill=reticle_color, width=2)
            draw.line([(cx + 40, cy), (cx + 100, cy)], fill=reticle_color, width=2)
            draw.line([(cx, cy - 100), (cx, cy - 40)], fill=reticle_color, width=2)
            draw.line([(cx, cy + 40), (cx, cy + 100)], fill=reticle_color, width=2)

            final_img = img.convert("RGB")
            final_img.save(image_path, "JPEG", quality=94)
        except Exception as e:
            print(f"HUD overlay notice: {e}")
        return image_path

    def fetch_scene_image(
        self,
        prompt: str,
        width: int,
        height: int,
        output_path: Path,
        scene_num: int = 1,
        on_screen_text: str = ""
    ) -> Path:
        """
        Renders 3D anatomical mannequin visual using dedicated Octane/Blender prompts.
        Falls back seamlessly to high-tech procedural simulation canvas on network errors.
        """
        full_prompt = (
            f"3D Blender render, Zack D Films style, stylized clay gray human mannequin, "
            f"anatomical cross section showing glowing bones, internal organs, and muscle tissues, "
            f"clinical medical laboratory lighting, Octane render, raytraced subsurface scattering, "
            f"8k resolution, photorealistic physics simulation, 9:16 vertical portrait: {prompt}"
        )

        encoded_prompt = urllib.parse.quote(full_prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&model=flux&nologo=true"

        downloaded = False
        try:
            res = requests.get(url, timeout=25)
            if res.status_code == 200 and len(res.content) > 10000:
                output_path.write_bytes(res.content)
                with Image.open(output_path) as img:
                    img.verify()
                downloaded = True
        except Exception:
            pass

        if not downloaded:
            self.generate_procedural_simulation_canvas(
                width=width,
                height=height,
                scene_num=scene_num,
                on_screen_text=on_screen_text,
                output_path=output_path
            )

        # Apply Zack D. Films style medical HUD telemetry
        if on_screen_text:
            self.overlay_hud_telemetry(output_path, on_screen_text, scene_num)

        return output_path

    def prepare_scene_visuals(
        self,
        scenes: List[ScriptScene],
        format_type: str = "shorts",
        session_id: str = "demo",
        niche: str = "wealth_secrets"
    ) -> List[Path]:
        """
        Prepares scene visual media based on niche style:
        - Style 3 (Magnates Media): Real 1080p vertical video B-Roll footage from Coverr/Mixkit.
        - Style 1 (Zack D. Films): 3D anatomical mannequin simulation visuals with HUD telemetry.
        """
        cfg = VIDEO_CONFIGS.get(format_type, VIDEO_CONFIGS["shorts"])
        width, height = cfg["width"], cfg["height"]

        media_paths = []

        # Style: 2D Vector Infographic ("The Curious Plot" 4 Levels of Leverage Style)
        if niche == "curious_leverage":
            from app.agents.vector_motion_engine import VectorMotionEngine
            vec_engine = VectorMotionEngine()

            for i, scene in enumerate(scenes):
                frame_path = TEMP_DIR / f"{session_id}_vec_scene_{scene.scene_number}.png"
                wallet = getattr(scene, 'wallet_amount', None) or ("$120,000" if i == len(scenes)-1 else f"${20 * (i+1) * 2}")
                hero = getattr(scene, 'hero_text', None) or ("$20 -> $120,000" if i == 0 else wallet)
                level_str = getattr(scene, 'level_str', None) or f"LEVEL {min(4, i)}: {['HOOK', 'LABOR', 'CAPITAL', 'SYSTEMS', 'DEALS'][min(4, i)]}"
                formula = getattr(scene, 'formula_text', None) or scene.on_screen_text
                active_level = getattr(scene, 'active_level', None) or min(4, max(1, i))

                vec_engine.render_scene_frame(
                    brand_name="THE CURIOUS PLOT",
                    wallet_amount=wallet,
                    hero_text=hero,
                    level_str=level_str,
                    formula_text=formula,
                    active_level=active_level,
                    output_path=frame_path
                )
                media_paths.append(frame_path)

            return media_paths

        is_3d_simulation = (niche == "simulation_explainer")

        for i, scene in enumerate(scenes):
            scene_num = scene.scene_number

            # If Style 3 (Documentary / Finance / Psychology / Tech / Stoicism):
            # Attempt to fetch real 1080p video clip first!
            if not is_3d_simulation:
                search_query = f"{scene.on_screen_text} {niche.replace('_', ' ')}"
                video_clip = self.stock_director.fetch_scene_broll(
                    scene_keywords=search_query,
                    niche=niche,
                    scene_index=i,
                    session_id=session_id
                )
                if video_clip and video_clip.exists():
                    media_paths.append(video_clip)
                    continue

            # If Style 1 (Zack D. 3D Simulation) or fallback:
            scene_img_path = TEMP_DIR / f"{session_id}_scene_{scene_num}.jpg"
            self.fetch_scene_image(
                prompt=scene.visual_prompt,
                width=width,
                height=height,
                output_path=scene_img_path,
                scene_num=scene_num,
                on_screen_text=scene.on_screen_text
            )
            media_paths.append(scene_img_path)

        return media_paths

    def generate_high_ctr_thumbnail(
        self,
        title: str,
        overlay_text: str,
        focal_prompt: str,
        output_path: Path,
        width: int = 1280,
        height: int = 720
    ) -> Path:
        """
        Designs high-CTR click-magnet thumbnail:
        1. Generates high-impact focal visual
        2. Applies contrast vignette & rim shadow
        3. Renders 2-3 word bold text in high-visibility yellow/white with heavy stroke
        """
        bg_path = TEMP_DIR / "thumb_raw.jpg"
        self.fetch_scene_image(
            prompt=f"{focal_prompt}, intense dramatic expression, high contrast chiaroscuro, viral youtube thumbnail aesthetic",
            width=width,
            height=height,
            output_path=bg_path,
            scene_num=1,
            on_screen_text=""
        )

        img = Image.open(bg_path).convert("RGBA")
        if img.size != (width, height):
            img = img.resize((width, height), Image.Resampling.LANCZOS)

        # Create dramatic dark vignette overlay so text pops
        overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw_ov = ImageDraw.Draw(overlay)
        for x in range(width // 2):
            alpha = int(180 * (1.0 - (x / (width // 2))))
            draw_ov.line([(x, 0), (x, height)], fill=(0, 0, 0, alpha))

        img = Image.alpha_composite(img, overlay)
        draw = ImageDraw.Draw(img)

        clean_text = (overlay_text or "THE TRUTH").upper()

        font_size = 92
        try:
            font = ImageFont.truetype(self.font_path, font_size)
        except Exception:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), clean_text, font=font)
        tx = 80
        ty = (height - (bbox[3] - bbox[1])) // 2

        stroke_width = 8
        for dx in range(-stroke_width, stroke_width + 1):
            for dy in range(-stroke_width, stroke_width + 1):
                if dx * dx + dy * dy <= stroke_width * stroke_width:
                    draw.text((tx + dx, ty + dy), clean_text, font=font, fill=(0, 0, 0, 255))

        draw.text((tx + 6, ty + 6), clean_text, font=font, fill=(0, 0, 0, 220))
        draw.text((tx, ty), clean_text, font=font, fill=(255, 234, 0, 255))

        final_thumb = img.convert("RGB")
        final_thumb.save(output_path, "JPEG", quality=95)
        return output_path
