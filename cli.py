#!/usr/bin/env python3
"""
ApexTube CLI - Headless Autonomous YouTube Automation Engine
Run video production batches, policy compliance audits, and metadata generation from the terminal.
"""

import sys
import argparse
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.config import NICHES, VOICES, DEFAULT_VOICE
from app.agents.orchestrator import MasterOrchestrator
from app.agents.policy_guardian import PolicyGuardian
from app.agents.guru_strategist import GuruStrategist
from app.agents.retention_writer import RetentionWriter


def print_banner():
    banner = r"""
    ╔════════════════════════════════════════════════════════════════════════╗
    ║      ___             _____      _            ____  _             _ _       ║
    ║     / _ \ _ __   _____|_   _|   _| |__   ___  / ___|| |_ _   _  __| (_) ___  ║
    ║    / /_\ \ '_ \ / _ \ \ | || | | | '_ \ / _ \ \___ \| __| | | |/ _` | |/ _ \ ║
    ║   / /_\\ \ |_) |  __/ / | || |_| | |_) |  __/  ___) | |_| |_| | (_| | | (_) |║
    ║  /_/   \_\ .__/ \___|/  |_| \__,_|_.__/ \___| |____/ \__|\__,_|\__,_|_|\___/ ║
    ║          |_|                                                          ║
    ║          Autonomous YouTube Monetization Squad (100% Free Engine)      ║
    ╚════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def main():
    print_banner()
    parser = argparse.ArgumentParser(description="ApexTube Autonomous YouTube Studio CLI")
    parser.add_argument(
        "--niche",
        choices=list(NICHES.keys()),
        default="curious_leverage",
        help="Select high-CPM viral niche"
    )
    parser.add_argument(
        "--topic",
        type=str,
        default=None,
        help="Custom topic/angle (leave empty for curated viral preset)"
    )
    parser.add_argument(
        "--voice",
        type=str,
        default=DEFAULT_VOICE,
        help="Edge-TTS voice identifier"
    )
    parser.add_argument(
        "--format",
        choices=["shorts"],
        default="shorts",
        help="Video format (Strictly locked to High Quality 9:16 vertical Shorts)"
    )
    parser.add_argument(
        "--audit-only",
        action="store_true",
        help="Only run YPP policy compliance audit on script"
    )
    parser.add_argument(
        "--speed",
        type=str,
        default="+4%",
        help="Narration rate adjustment (e.g. +4%%, +8%%)"
    )
    parser.add_argument(
        "--batch",
        type=int,
        default=0,
        help="Batch produce N videos across rotating high-CPM niches"
    )
    parser.add_argument(
        "--calendar",
        action="store_true",
        help="Generate 7-day content schedule and revenue forecast"
    )

    args = parser.parse_args()

    orchestrator = MasterOrchestrator()

    if args.calendar:
        from scheduler import ChannelScheduler
        sched = ChannelScheduler()
        sched.generate_calendar_and_batch(days=7, auto_render=False)
        sys.exit(0)

    if args.batch > 0:
        print(f"\n🚀 Starting Autonomous Batch Run for {args.batch} Videos...")
        niche_keys = list(NICHES.keys())
        for i in range(args.batch):
            selected_niche = niche_keys[i % len(niche_keys)]
            print(f"\n[{i+1}/{args.batch}] Producing video for Niche: {selected_niche.upper()}...")
            orchestrator.run_pipeline(
                niche=selected_niche,
                format_type=args.format,
                speed_adjustment=args.speed
            )
        print(f"\n🎉 Successfully rendered batch of {args.batch} videos in output/")
        sys.exit(0)

    if args.audit_only:
        print(f"\n🛡️ Running Policy & Monetization Audit for niche: {args.niche}...")
        strat = orchestrator.strategist.formulate_strategy(niche_key=args.niche, custom_topic=args.topic)
        script = orchestrator.writer.generate_script(
            niche=args.niche,
            topic=strat.topic,
            title=strat.primary_title,
            format_type=args.format
        )
        report = orchestrator.guardian.audit_script(
            title=strat.primary_title,
            script_text=script.full_narration,
            niche=args.niche
        )
        print("\n" + "="*50)
        print(f"📊 Compliance Score: {report.compliance_score}/100")
        print(f"⚠️ Risk Level: {report.risk_level}")
        print(f"💰 Monetization Verdict:\n{report.monetization_verdict}")
        print("="*50 + "\n")
        sys.exit(0)

    # Execute full pipeline
    try:
        package = orchestrator.run_pipeline(
            niche=args.niche,
            topic=args.topic,
            voice_id=args.voice,
            format_type=args.format,
            speed_adjustment=args.speed
        )
        print("\n🎉 PRODUCTION COMPLETE!")
        print(f"📹 Video:       {package.video_path}")
        print(f"🖼️ Thumbnail:   {package.thumbnail_path}")
        print(f"🎙️ Mixed Audio: {package.mixed_audio_path}")
        print(f"📋 SEO JSON:    {package.upload_script_path.replace('_publish_to_youtube.py', '_seo.json')}")
        print(f"🚀 Publish:     python {package.upload_script_path}\n")
    except Exception as e:
        print(f"\n❌ Error during production: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

