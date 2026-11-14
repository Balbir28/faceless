#!/usr/bin/env python3
"""
ApexTube Auto-Pilot - Autonomous Background Video Production Worker
Monitors the publishing schedule and automatically bakes daily high-CPM Shorts
into 'output/ready_to_publish/', triggering a macOS notification when ready.
"""

import os
import sys
import time
import json
import shutil
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.config import OUTPUT_DIR, DATA_DIR, NICHES
from app.agents.orchestrator import MasterOrchestrator
from scheduler import ChannelScheduler

READY_DIR = OUTPUT_DIR / "ready_to_publish"
READY_DIR.mkdir(parents=True, exist_ok=True)


def notify_mac(title: str, subtitle: str, message: str):
    """Sends a native macOS desktop notification."""
    try:
        script = f'display notification "{message}" with title "{title}" subtitle "{subtitle}"'
        subprocess.run(["osascript", "-e", script], capture_output=True)
    except Exception:
        pass


class AutoPilotWorker:
    def __init__(self):
        self.orchestrator = MasterOrchestrator()
        self.scheduler = ChannelScheduler()
        self.calendar_path = OUTPUT_DIR / "content_calendar.json"

    def ensure_calendar(self):
        if not self.calendar_path.exists():
            print("📅 Generating fresh 7-day content schedule...")
            self.scheduler.generate_calendar_and_batch(days=7, auto_render=False)

    def produce_next_scheduled(self) -> Path:
        self.ensure_calendar()
        with open(self.calendar_path, "r") as f:
            calendar = json.load(f)

        # Find next QUEUED item
        target_item = None
        for item in calendar:
            if item.get("status") == "QUEUED":
                target_item = item
                break

        # If all rendered, regenerate calendar for next 7 days
        if not target_item:
            print("🔄 All scheduled videos rendered. Rolling over to next 7-day cycle...")
            self.scheduler.generate_calendar_and_batch(days=7, auto_render=False)
            with open(self.calendar_path, "r") as f:
                calendar = json.load(f)
            target_item = calendar[0]

        niche_key = target_item["niche_key"]
        print(f"\n=======================================================")
        print(f"🤖 [Auto-Pilot] B換えing Scheduled Short for Day {target_item['day']}")
        print(f"📌 Niche: {target_item['niche_name']} (CPM: {target_item['estimated_cpm']})")
        print(f"🎬 Title: {target_item['suggested_title']}")
        print(f"=======================================================\n")

        # Produce the HQ Short
        package = self.orchestrator.run_pipeline(
            niche=niche_key,
            format_type="shorts"
        )

        # Update calendar item status
        target_item["status"] = "RENDERED"
        target_item["rendered_at"] = datetime.now().isoformat()
        target_item["video_path"] = package.video_path
        target_item["thumbnail_path"] = package.thumbnail_path
        with open(self.calendar_path, "w") as f:
            json.dump(calendar, f, indent=2)

        # Stage files into ready_to_publish
        vid_src = Path(package.video_path)
        thumb_src = Path(package.thumbnail_path)
        dest_vid = READY_DIR / vid_src.name
        dest_thumb = READY_DIR / thumb_src.name
        shutil.copy2(vid_src, dest_vid)
        shutil.copy2(thumb_src, dest_thumb)

        # Create quick posting text file
        summary_txt = READY_DIR / f"{package.session_id}_POST_NOW.txt"
        summary_txt.write_text(
            f"=== READY TO POST: {package.strategy.primary_title} ===\n\n"
            f"📌 YOUTUBE SHORTS TITLE:\n{package.seo_metadata.title}\n\n"
            f"📝 YOUTUBE DESCRIPTION:\n{package.seo_metadata.description}\n\n"
            f"🏷️ YOUTUBE TAGS:\n{', '.join(package.seo_metadata.tags)}\n\n"
            f"📸 INSTAGRAM REELS CAPTION:\n{package.cross_platform.instagram_reels.caption if package.cross_platform else ''}\n\n"
            f"🎵 TIKTOK CAPTION:\n{package.cross_platform.tiktok.caption if package.cross_platform else ''}\n",
            encoding="utf-8"
        )

        # Trigger macOS Notification
        notify_mac(
            title="ApexTube Auto-Pilot",
            subtitle="Daily HQ Short Ready!",
            message=f"'{package.strategy.primary_title[:38]}...' is ready in ready_to_publish/"
        )

        print("\n" + "="*60)
        print("✅ Auto-Pilot Production Complete!")
        print(f"📁 Video Staged: {dest_vid}")
        print(f"📝 Quick Post TXT: {summary_txt}")
        print("="*60 + "\n")
        return dest_vid

    def run_daemon(self, target_hours: tuple = (11, 17)):
        """
        Runs quietly in the background, checking hourly.
        Bakes videos at 11:30 AM and 5:30 PM (30 min before peak posting windows).
        """
        print(f"\n🚀 ApexTube Auto-Pilot Daemon Active.")
        print(f"⏰ Scheduled auto-production triggers at hours: {target_hours} (30 mins before peak windows)")
        print(f"Press CTRL+C to stop.\n")

        last_baked_day_hour = None
        while True:
            now = datetime.now()
            current_day_hour = (now.strftime("%Y-%m-%d"), now.hour)

            if now.hour in target_hours and now.minute >= 30 and current_day_hour != last_baked_day_hour:
                print(f"⏰ Triggering scheduled production for peak posting window...")
                try:
                    self.produce_next_scheduled()
                    last_baked_day_hour = current_day_hour
                except Exception as e:
                    print(f"❌ Auto-pilot error: {e}")

            time.sleep(60)  # Check every 60 seconds


def main():
    parser = argparse.ArgumentParser(description="ApexTube Auto-Pilot Daily Video Worker")
    parser.add_argument(
        "--daemon",
        action="store_true",
        help="Run continuously in background and produce videos before peak posting hours"
    )
    args = parser.parse_args()

    worker = AutoPilotWorker()
    if args.daemon:
        worker.run_daemon()
    else:
        worker.produce_next_scheduled()


if __name__ == "__main__":
    main()

