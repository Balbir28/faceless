#!/usr/bin/env python3
"""
ApexTube Scheduler - Autonomous Content Calendar & Batch Production Engine
Plans, rotates, and schedules multi-day high-CPM video releases to build algorithm momentum.
"""

import sys
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.config import NICHES, OUTPUT_DIR, DATA_DIR
from app.agents.orchestrator import MasterOrchestrator


class ChannelScheduler:
    def __init__(self):
        self.orchestrator = MasterOrchestrator()
        self.tracker_file = DATA_DIR / "channel_tracker.json"

    def get_publishing_plan(self, days: int = 7, videos_per_day: int = 1) -> List[Dict[str, Any]]:
        """
        Creates an algorithmic publishing schedule rotating through top high-CPM niches
        to maximize YouTube Partner Program revenue without triggering repetitious content filters.
        """
        niche_keys = list(NICHES.keys())
        schedule = []
        start_date = datetime.now()

        for day in range(days):
            current_date = start_date + timedelta(days=day)
            date_str = current_date.strftime("%Y-%m-%d")

            for v in range(videos_per_day):
                niche_idx = (day * videos_per_day + v) % len(niche_keys)
                niche_key = niche_keys[niche_idx]
                niche_info = NICHES[niche_key]

                # Peak posting windows (12:00 PM & 6:00 PM)
                hour = 12 if v == 0 else 18
                scheduled_time = f"{date_str}T{hour:02d}:00:00"

                strat = self.orchestrator.strategist.formulate_strategy(niche_key=niche_key)

                schedule.append({
                    "day": day + 1,
                    "scheduled_time": scheduled_time,
                    "niche_key": niche_key,
                    "niche_name": niche_info["name"],
                    "estimated_cpm": niche_info["cpm_range"],
                    "suggested_title": strat.primary_title,
                    "status": "QUEUED"
                })

        return schedule

    def generate_calendar_and_batch(self, days: int = 3, auto_render: bool = False) -> Dict[str, Any]:
        """
        Generates content calendar and optionally batch-renders all videos in sequence.
        """
        plan = self.get_publishing_plan(days=days, videos_per_day=1)
        calendar_path = OUTPUT_DIR / "content_calendar.json"
        calendar_path.write_text(json.dumps(plan, indent=2), encoding="utf-8")

        rendered_packages = []
        if auto_render:
            print(f"\n🚀 Batch Rendering {len(plan)} Scheduled Videos...")
            for idx, item in enumerate(plan):
                print(f"\n--- [Rendering Day {item['day']}/{days}] {item['suggested_title']} ---")
                pkg = self.orchestrator.run_pipeline(
                    niche=item["niche_key"],
                    format_type="shorts"
                )
                item["status"] = "RENDERED"
                item["video_path"] = pkg.video_path
                item["thumbnail_path"] = pkg.thumbnail_path
                item["upload_script"] = pkg.upload_script_path
                rendered_packages.append(pkg.model_dump())

            calendar_path.write_text(json.dumps(plan, indent=2), encoding="utf-8")

        # Update tracker stats
        tracker_data = {
            "last_updated": datetime.now().isoformat(),
            "scheduled_videos": len(plan),
            "rendered_videos": len(rendered_packages),
            "target_average_cpm": "$15.40",
            "projected_revenue": {
                "at_100k_views": "$1,200 - $2,200",
                "at_500k_views": "$6,000 - $11,000",
                "at_1m_views": "$12,000 - $22,000"
            },
            "schedule": plan
        }
        self.tracker_file.write_text(json.dumps(tracker_data, indent=2), encoding="utf-8")

        return tracker_data


if __name__ == "__main__":
    scheduler = ChannelScheduler()
    print("="*60)
    print("📅 Generating 7-Day Autonomous YouTube Content Calendar...")
    print("="*60)
    data = scheduler.generate_calendar_and_batch(days=7, auto_render=False)
    for s in data["schedule"]:
        print(f"[{s['scheduled_time']}] ({s['niche_name']}) -> {s['suggested_title']} (CPM: {s['estimated_cpm']})")
    print(f"\n✅ Content calendar saved to: {OUTPUT_DIR / 'content_calendar.json'}")
    print(f"📊 Channel revenue projections saved to: {DATA_DIR / 'channel_tracker.json'}\n")

