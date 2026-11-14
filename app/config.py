"""
ApexTube Studio - Global Configuration & Niche Knowledge Base
Engineered for High-CPM, High-Retention YouTube Automation & Strict YPP Policy Compliance.
"""

from pathlib import Path

# Base Paths
ROOT_DIR = Path(__file__).resolve().parent.parent
APP_DIR = ROOT_DIR / "app"
OUTPUT_DIR = ROOT_DIR / "output"
TEMP_DIR = ROOT_DIR / "temp"
ASSETS_DIR = APP_DIR / "assets"
DATA_DIR = ROOT_DIR / "data"

for path in [OUTPUT_DIR, TEMP_DIR, DATA_DIR, ASSETS_DIR / "audio", ASSETS_DIR / "fonts"]:
    path.mkdir(parents=True, exist_ok=True)

# Free Neural Voices (Edge-TTS)
VOICES = {
    "christopher": {
        "id": "en-US-ChristopherNeural",
        "name": "Christopher (Deep Storyteller / Documentary)",
        "gender": "male",
        "style": "dramatic, deep, authoritative",
    },
    "guy": {
        "id": "en-US-GuyNeural",
        "name": "Guy (Modern Explainer / Energetic)",
        "gender": "male",
        "style": "conversational, fast-paced, engaging",
    },
    "eric": {
        "id": "en-US-EricNeural",
        "name": "Eric (Serious / Mysterious)",
        "gender": "male",
        "style": "tense, serious, high-stakes",
    },
    "ava": {
        "id": "en-US-AvaNeural",
        "name": "Ava (Expressive / Warm / Captivating)",
        "gender": "female",
        "style": "warm, dynamic, relatable",
    },
    "emma": {
        "id": "en-US-EmmaNeural",
        "name": "Emma (Refined / Intellectual)",
        "gender": "female",
        "style": "calm, sophisticated, analytical",
    },
    "ryan": {
        "id": "en-GB-RyanNeural",
        "name": "Ryan (British Drama / Historical Deep-Dive)",
        "gender": "male",
        "style": "sophisticated, cinematic, dramatic",
    },
}

DEFAULT_VOICE = "en-US-ChristopherNeural"

# High-CPM & Viral Niches Knowledge Base
NICHES = {
    "curious_leverage": {
        "name": "🍋 Business Leverage Metaphors (The Curious Plot Style)",
        "cpm_range": "$22.00 - $42.00",
        "viral_potential": "Unmatched (Global Curiosity, 95% APV & Viral Comment Floods)",
        "monetization_speed": "Maximum (Top finance advertiser bids + digital products)",
        "target_audience": "Entrepreneurs, wealth builders, young professionals, all ages",
        "voice_recommendation": "en-US-GuyNeural",
        "visual_style": "2D vector motion graphic, dark indigo spotlight, big bold cartoon typography with 3D drop shadow, 4-tier leverage stage tracker, formula cards, cute vector lemonade stalls and character Leo",
        "music_mood": "curious_lofi",
        "hook_patterns": [
            "$20 to $120,000 using nothing but a lemonade stand. Here are the 4 levels of leverage most people never find...",
            "$50 to $500,000 with a simple lawn mower. The 4 levels of leverage that separate working from wealth...",
            "$100 to $1,500,000 using a mobile coffee cart. How the same beans 15x in value...",
        ],
        "compliance_rules": [
            "Clearly frame as educational business and economic metaphors.",
            "Include disclaimer: 'Metaphorical breakdown for educational purposes, not guaranteed financial advice.'",
            "Keep math transparent, logical, and easy to follow.",
        ],
    },
    "simulation_explainer": {
        "name": "🧬 3D Mannequin Simulation (Zack D. Style)",
        "cpm_range": "$12.00 - $25.00",
        "viral_potential": "Legendary (Massive Global Algorithm Appeal & Replay Loops)",
        "monetization_speed": "Explosive (High retention, universally shareable)",
        "target_audience": "Curious viewers worldwide, all ages (Global broad appeal)",
        "voice_recommendation": "en-US-ChristopherNeural",
        "visual_style": "3D Blender human mannequin simulation, Unreal Engine 5 anatomical cutaway, glowing bones and muscles, medical forensic cross-section, dramatic clinical studio lighting, Zack D Films aesthetic",
        "music_mood": "clinical_suspense",
        "hook_patterns": [
            "If you ever tried to finish an entire marathon doing the worm, here is what would happen to your body...",
            "What actually happens inside your stomach if you accidentally swallow a magnet and a coin?",
            "If you tried to survive falling from a skyscraper by landing on a mattress, here is the brutal physics...",
        ],
        "compliance_rules": [
            "Frame simulations strictly as hypothetical physics and biomechanical education.",
            "Do NOT present lethal self-harm challenges as real-world encouragement.",
            "Include educational disclaimer on extreme hypothetical scenarios.",
        ],
    },
    "dark_psychology": {
        "name": "🧠 Dark Psychology (Magnates Media Style)",
        "cpm_range": "$9.00 - $17.50",
        "viral_potential": "Extreme (High Curiosity Gap & Replayability)",
        "monetization_speed": "Fast (High retention & comment flame wars)",
        "target_audience": "Curious viewers, self-improvers, psychology enthusiasts (18-35)",
        "voice_recommendation": "en-US-ChristopherNeural",
        "visual_style": "Dark cinematic lighting, neo-noir, shadow portraits, glowing neural circuits, 8k moody atmosphere",
        "music_mood": "dark_ambient",
        "hook_patterns": [
            "If someone ever does this to you, they're not being nice. They are using...",
            "Psychologists call this the darkest trick in human conversation...",
            "There is a terrifying reason why manipulative people always...",
        ],
        "compliance_rules": [
            "Do NOT promote real-world harm, harassment, or self-harm.",
            "Frame lessons ethically as defensive awareness and behavioral science.",
            "Use original transformative commentary, never copy Reddit text word-for-word.",
        ],
    },
    "wealth_secrets": {
        "name": "💎 Hidden Wealth (Magnates Media Style)",
        "cpm_range": "$18.00 - $38.00",
        "viral_potential": "Very High (Universal desire for financial independence)",
        "monetization_speed": "Rapid (Advertisers pay top dollar for finance audiences)",
        "target_audience": "Aspiring entrepreneurs, investors, business students (20-45)",
        "voice_recommendation": "en-US-GuyNeural",
        "visual_style": "Sleek luxury interiors, gold accents, stock charts, corporate architecture, high-contrast hyperrealistic",
        "music_mood": "corporate_modern",
        "hook_patterns": [
            "The 1% never keep their money in savings accounts. Here is where it actually goes...",
            "This hidden financial law made Warren Buffett 90% of his fortune after age 50...",
            "Most people spend 40 years working because they fell for this financial trap...",
        ],
        "compliance_rules": [
            "Include financial disclaimer: 'Educational purposes only, not financial advice.'",
            "Avoid get-rich-quick scams or deceptive crypto guarantees.",
            "Back claims with historical or economic rationale.",
        ],
    },
    "modern_stoicism": {
        "name": "🏛️ Modern Stoicism (Magnates Media Style)",
        "cpm_range": "$8.00 - $16.00",
        "viral_potential": "Very High (Evergreen, high bookmarking and sharing)",
        "monetization_speed": "Medium-Fast (Builds high subscriber loyalty & merch potential)",
        "target_audience": "Men & women seeking discipline, mental strength, resilience (18-40)",
        "voice_recommendation": "en-US-ChristopherNeural",
        "visual_style": "Marble Greek statues, ancient Roman architecture, dramatic moody lighting, thunderstorm over temples, cinematic 35mm",
        "music_mood": "epic_cinematic",
        "hook_patterns": [
            "Marcus Aurelius wrote this in his private journal when everything was falling apart...",
            "The moment you stop caring about this one thing, you become untouchable...",
            "Seneca warned that a man who suffers before it is necessary, suffers twice...",
        ],
        "compliance_rules": [
            "Synthesize philosophical teachings with modern daily life context.",
            "Keep scripts inspiring and philosophical, avoiding depressive spiraling.",
        ],
    },
    "future_tech": {
        "name": "⚡ AI & Future Tech (Magnates Media Style)",
        "cpm_range": "$12.00 - $26.00",
        "viral_potential": "Extreme (Fast news cycle & speculative wonder)",
        "monetization_speed": "Fast (Tech sponsors & high viewer engagement)",
        "target_audience": "Developers, futurists, tech enthusiasts, career professionals (18-45)",
        "voice_recommendation": "en-US-AvaNeural",
        "visual_style": "Futuristic robotics, glowing quantum cores, holographic interfaces, cyberpunk cityscapes, hyper-detailed",
        "music_mood": "cyberpunk_synth",
        "hook_patterns": [
            "Engineers quietly tested this AI model, and the result shocked even its creators...",
            "In 24 months, these 3 jobs will completely vanish due to autonomous systems...",
            "The trillion-dollar tech race nobody is talking about just crossed a terrifying line...",
        ],
        "compliance_rules": [
            "Strictly comply with YouTube Synthetic Media Policy (disclose generative visuals).",
            "Do not spread fabricated conspiracy theories or false safety emergencies.",
        ],
    },
    "unsolved_mysteries": {
        "name": "🔍 Unsolved Mysteries (Magnates Media Style)",
        "cpm_range": "$7.00 - $14.50",
        "viral_potential": "Insane (Unbeatable average percentage viewed)",
        "monetization_speed": "Fast (Viral Shorts feed algorithm favorite)",
        "target_audience": "Curiosity seekers, mystery fans, late-night scrollers (all ages)",
        "voice_recommendation": "en-GB-RyanNeural",
        "visual_style": "Foggy desolate landscapes, mysterious deep sea trenches, ancient forbidden vaults, vintage polaroid suspense, cinematic grain",
        "music_mood": "mystery_suspense",
        "hook_patterns": [
            "In 1977, astronomers recorded a signal from deep space that lasted exactly 72 seconds...",
            "Deep inside the ocean, scientists discovered a sound that should not exist...",
            "This photograph was taken moments before the entire crew disappeared without a trace...",
        ],
        "compliance_rules": [
            "Respect real victims and historical incidents with dignified framing.",
            "Categorize as historical curiosity/documentary, not misleading panic bait.",
        ],
    },
}

# YouTube Partner Program (YPP) Hard Policy Criteria
YPP_POLICY_CHECKS = {
    "reused_content": {
        "rule": "Videos must contain significant original commentary, analysis, or narrative value.",
        "penalty": "Demonetization / Ineligible for YPP.",
        "enforcement": "Never stitch uncredited viral clips without voiceover or critique.",
    },
    "repetitious_content": {
        "rule": "Content cannot be mass-generated using identical templates or programmatically repeated phrasing.",
        "penalty": "Channel demonetization.",
        "enforcement": "Dynamic story pacing, variable hooks, and unique visual composition for every scene.",
    },
    "synthetic_media_disclosure": {
        "rule": "Must flag if realistic AI synthetic media depicts real events or altered realities.",
        "penalty": "Video removal or monetization suspension.",
        "enforcement": "Automatic metadata tagging: 'Altered or synthetic content: Yes/No'.",
    },
    "clickbait_metadata_mismatch": {
        "rule": "Thumbnail and title must not mislead the viewer about the actual video contents.",
        "penalty": "Reach restriction / algorithmic penalty.",
        "enforcement": "Title and script must deliver on the promised hook within the first 15 seconds.",
    },
}

# Video Formatting - Locked strictly to High Quality (HQ) YouTube Shorts (9:16)
VIDEO_CONFIGS = {
    "shorts": {
        "width": 1080,
        "height": 1920,
        "fps": 30,
        "aspect_ratio": "9:16",
        "ideal_duration": (30, 52),  # seconds (Optimal viral Shorts retention window)
        "target_word_count": (75, 125),
        "video_bitrate": "8000k",
        "audio_bitrate": "320k",
        "crf": 18,  # Visually lossless HQ master
    }
}

# System Fonts for Subtitles and Thumbnails
FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Black.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/System/Library/Fonts/Helvetica.ttc",
]

def get_best_font() -> str:
    for font_path in FONT_CANDIDATES:
        if Path(font_path).exists():
            return font_path
    return "Arial"

