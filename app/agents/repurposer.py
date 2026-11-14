"""
Repurposer - Multi-Platform Cross-Posting & Traffic Multiplier Agent
Formats every produced video for simultaneous publishing across YouTube Shorts,
Instagram Reels, and TikTok to 3x viewer reach with zero extra production cost.
"""

from typing import Dict, List, Any
from pydantic import BaseModel
from app.agents.retention_writer import RetentionScript


class PlatformMetadata(BaseModel):
    platform: str
    caption: str
    hashtags: List[str]
    call_to_action: str
    recommended_audio: str
    aspect_ratio: str


class CrossPlatformPackage(BaseModel):
    video_path: str
    thumbnail_path: str
    youtube_shorts: PlatformMetadata
    instagram_reels: PlatformMetadata
    tiktok: PlatformMetadata


class MultiPlatformRepurposer:
    def __init__(self):
        pass

    def generate_cross_platform_pack(
        self,
        video_path: str,
        thumbnail_path: str,
        title: str,
        niche: str,
        script: RetentionScript
    ) -> CrossPlatformPackage:
        clean_niche = niche.replace("_", "")
        summary_hook = script.scenes[0].narration

        # 1. YouTube Shorts Metadata
        yt_hashtags = [f"#{clean_niche}", "#shorts", "#viral", "#mindset", "#facts"]
        yt_meta = PlatformMetadata(
            platform="YouTube Shorts",
            caption=(
                f"{title}\n\n"
                f"⚡ {summary_hook}\n\n"
                f"📌 Educational analysis produced with original commentary.\n\n"
                + " ".join(yt_hashtags)
            ),
            hashtags=yt_hashtags,
            call_to_action="Subscribe for daily high-leverage strategic breakdowns.",
            recommended_audio="Original Mixed Audio (-14 LUFS Broadcast Normalized)",
            aspect_ratio="9:16"
        )

        # 2. Instagram Reels Metadata
        ig_hashtags = [
            f"#{clean_niche}", "#reelsinstagram", "#viralreels", "#mindsetshift",
            "#growthmindset", "#highperformance", "#dailymotivation", "#psychologyfacts",
            "#stoicism", "#wealthmindset", "#successprinciples", "#explorepage"
        ]
        ig_meta = PlatformMetadata(
            platform="Instagram Reels",
            caption=(
                f"{title} 🧠\n\n"
                f"\"{summary_hook}\"\n\n"
                f"Drop a 💬 below if you've experienced this.\n"
                f"Save this reel to revisit later. 🔖\n\n"
                + " ".join(ig_hashtags)
            ),
            hashtags=ig_hashtags,
            call_to_action="Follow for daily mental models and strategic breakdowns.",
            recommended_audio="Trending dark ambient or original mixed audio",
            aspect_ratio="9:16"
        )

        # 3. TikTok Metadata
        tt_hashtags = [
            f"#{clean_niche}", "#fyp", "#foryou", "#viral",
            "#learnontiktok", "#mindblown", "#deepthoughts"
        ]
        tt_meta = PlatformMetadata(
            platform="TikTok",
            caption=f"{title} 😳 Watch till the end. " + " ".join(tt_hashtags),
            hashtags=tt_hashtags,
            call_to_action="Follow for more secrets they never teach you in school.",
            recommended_audio="Original Mixed Audio",
            aspect_ratio="9:16"
        )

        return CrossPlatformPackage(
            video_path=video_path,
            thumbnail_path=thumbnail_path,
            youtube_shorts=yt_meta,
            instagram_reels=ig_meta,
            tiktok=tt_meta
        )

