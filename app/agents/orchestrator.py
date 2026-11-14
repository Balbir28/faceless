"""
MasterOrchestrator - The Autonomous YouTube Monetization Guru & Studio Lead
Coordinates the entire agent squad to autonomously plan, audit, script, voice, animate,
composite, and prepare high-CPM viral YouTube videos for 100% free production.
"""

import uuid
import json
import time
from pathlib import Path
from typing import Dict, Any, Optional
from pydantic import BaseModel

from app.config import OUTPUT_DIR, TEMP_DIR, DEFAULT_VOICE, NICHES
from app.agents.guru_strategist import GuruStrategist, VideoStrategy
from app.agents.retention_writer import RetentionWriter, RetentionScript
from app.agents.policy_guardian import PolicyGuardian, ComplianceReport
from app.agents.audio_director import AudioDirector, AudioProductionResult
from app.agents.visual_engine import VisualEngine
from app.agents.video_compositor import VideoCompositor, VideoRenderResult
from app.agents.publisher_seo import PublisherSEO, SEOMetadata
from app.agents.repurposer import MultiPlatformRepurposer, CrossPlatformPackage


class FullProductionPackage(BaseModel):
    session_id: str
    video_path: str
    thumbnail_path: str
    mixed_audio_path: str
    subtitles_ass_path: str
    subtitles_srt_path: str
    seo_metadata: SEOMetadata
    strategy: VideoStrategy
    compliance_report: ComplianceReport
    script: RetentionScript
    duration_seconds: float
    file_size_mb: float
    upload_script_path: str
    cross_platform: Optional[CrossPlatformPackage] = None
    production_time_sec: float


class MasterOrchestrator:
    def __init__(self):
        self.strategist = GuruStrategist()
        self.writer = RetentionWriter()
        self.guardian = PolicyGuardian()
        self.audio_director = AudioDirector()
        self.visual_engine = VisualEngine()
        self.compositor = VideoCompositor()
        self.publisher = PublisherSEO()
        self.repurposer = MultiPlatformRepurposer()

    def run_pipeline(
        self,
        niche: str = "dark_psychology",
        topic: Optional[str] = None,
        voice_id: str = DEFAULT_VOICE,
        format_type: str = "shorts",
        music_mood: Optional[str] = None,
        speed_adjustment: str = "+4%"
    ) -> FullProductionPackage:
        start_time = time.time()
        session_id = f"{niche}_{uuid.uuid4().hex[:8]}"

        print(f"\n=======================================================")
        print(f"🚀 [ApexTube Guru] Starting Autonomous Video Production")
        print(f"📌 Niche: {niche} | Format: {format_type} | Voice: {voice_id}")
        print(f"=======================================================")

        # Step 1: Strategy & Viral Formulation
        print(f"\n[Step 1/6] 🧠 Guru Strategist: Formulating high-CTR concept...")
        strategy = self.strategist.formulate_strategy(niche_key=niche, custom_topic=topic)
        print(f" -> Selected Title: {strategy.primary_title}")
        print(f" -> Estimated CPM: {strategy.estimated_cpm} | Viral Velocity: {strategy.viral_velocity_score}/100")

        # Step 2: High-AVD Scriptwriting
        print(f"\n[Step 2/6] ✍️ Retention Writer: Crafting retention-engineered script...")
        script = self.writer.generate_script(
            niche=niche,
            topic=strategy.topic,
            title=strategy.primary_title,
            format_type=format_type
        )
        print(f" -> Script Scenes: {len(script.scenes)} | Words: {script.total_words} | Est. Duration: {script.estimated_duration_sec:.1f}s")

        # Step 3: YPP Compliance & Monetization Audit
        print(f"\n[Step 3/6] 🛡️ Policy Guardian: Auditing against YouTube Partner Program guidelines...")
        compliance = self.guardian.audit_script(
            title=strategy.primary_title,
            script_text=script.full_narration,
            niche=niche
        )
        print(f" -> Monetization Status: {'APPROVED' if compliance.is_safe_for_monetization else 'WARNING'}")
        print(f" -> Compliance Score: {compliance.compliance_score}/100 | Risk: {compliance.risk_level}")

        # Step 4: Audio Engineering & Free Voiceover Synthesis
        print(f"\n[Step 4/6] 🎙️ Audio Director: Synthesizing neural voiceover & dynamic audio bed...")
        selected_mood = music_mood or NICHES.get(niche, {}).get("music_mood", "dark_ambient")
        scene_durations = [s.estimated_duration for s in script.scenes]
        audio_res = self.audio_director.synthesize_and_mix(
            script_text=script.full_narration,
            voice_id=voice_id,
            music_mood=selected_mood,
            speed_adjustment=speed_adjustment,
            session_id=session_id,
            video_format=format_type,
            scene_durations=scene_durations,
            niche=niche
        )
        print(f" -> Narration Generated: {audio_res.duration_seconds:.2f}s | Subtitles Synced")

        # Step 5: Visual Curation & High-CTR Thumbnail Design
        print(f"\n[Step 5/6] 🎨 Visual Engine: Curating cinematic visuals & designing thumbnail...")
        scene_images = self.visual_engine.prepare_scene_visuals(
            scenes=script.scenes,
            format_type=format_type,
            session_id=session_id,
            niche=niche
        )

        thumb_output = OUTPUT_DIR / f"{session_id}_thumbnail.jpg"
        self.visual_engine.generate_high_ctr_thumbnail(
            title=strategy.primary_title,
            overlay_text=strategy.thumbnail_concept.overlay_text,
            focal_prompt=strategy.thumbnail_concept.focal_subject,
            output_path=thumb_output
        )
        print(f" -> {len(scene_images)} Scene visuals curated | Thumbnail rendered at {thumb_output.name}")

        # Step 6: Master Video Compositing & Subtitle Burning
        print(f"\n[Step 6/6] 🎬 Video Compositor: Assembling Ken Burns motion, captions & final MP4...")
        final_video_path = OUTPUT_DIR / f"{session_id}_video.mp4"
        render_res = self.compositor.assemble_full_video(
            image_paths=scene_images,
            scenes=script.scenes,
            audio_path=Path(audio_res.mixed_audio_path),
            subtitles_ass_path=Path(audio_res.subtitles_ass_path),
            output_video_path=final_video_path,
            total_audio_duration=audio_res.duration_seconds,
            format_type=format_type,
            session_id=session_id
        )
        print(f" -> Production Finished: {render_res.file_size_mb} MB | {render_res.duration_seconds:.1f}s")

        # SEO Metadata & Publish Script
        seo_meta = self.publisher.generate_seo_pack(
            niche=niche,
            topic=strategy.topic,
            primary_title=strategy.primary_title,
            alternate_titles=[t.title for t in strategy.titles[1:]],
            script_summary=script.full_narration[:240] + "...",
            disclaimer=script.policy_disclaimer
        )
        seo_path = OUTPUT_DIR / f"{session_id}_seo.json"
        self.publisher.save_seo_pack(seo_meta, seo_path)

        upload_script = OUTPUT_DIR / f"{session_id}_publish_to_youtube.py"
        self.publisher.generate_youtube_upload_script(
            video_path=final_video_path,
            thumbnail_path=thumb_output,
            seo_path=seo_path,
            script_path=upload_script
        )

        # Generate Multi-Platform Cross-Posting Package (YouTube + IG Reels + TikTok)
        cross_pack = self.repurposer.generate_cross_platform_pack(
            video_path=str(final_video_path),
            thumbnail_path=str(thumb_output),
            title=strategy.primary_title,
            niche=niche,
            script=script
        )
        cross_pack_path = OUTPUT_DIR / f"{session_id}_cross_platform.json"
        cross_pack_path.write_text(json.dumps(cross_pack.model_dump(), indent=2), encoding="utf-8")

        elapsed = time.time() - start_time
        print(f"\n✨ Video package complete in {elapsed:.1f} seconds!")
        print(f"📁 Video: {final_video_path}")
        print(f"🖼️ Thumbnail: {thumb_output}")
        print(f"📱 Cross-Platform JSON: {cross_pack_path}")
        print(f"📜 Upload Script: {upload_script}")
        print(f"=======================================================\n")

        return FullProductionPackage(
            session_id=session_id,
            video_path=str(final_video_path),
            thumbnail_path=str(thumb_output),
            mixed_audio_path=audio_res.mixed_audio_path,
            subtitles_ass_path=audio_res.subtitles_ass_path,
            subtitles_srt_path=audio_res.subtitles_srt_path,
            seo_metadata=seo_meta,
            strategy=strategy,
            compliance_report=compliance,
            script=script,
            duration_seconds=render_res.duration_seconds,
            file_size_mb=render_res.file_size_mb,
            upload_script_path=str(upload_script),
            cross_platform=cross_pack,
            production_time_sec=round(elapsed, 2)
        )

