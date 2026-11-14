# 🚀 ApexTube Studio - Autonomous YouTube Monetization Guru & Production Squad

> **A full-stack, 100% free multi-agent system designed to plan, strategize, write, voice, animate, composite, and publish high-CPM viral YouTube Shorts matching top industry references (*The Curious Plot*, *Zack D. Films*, *Magnates Media*) while strictly complying with YouTube Partner Program (YPP) policies.**

---

## 💎 The Guru Monetization Philosophy

Most AI automation channels fail, get rejected from YPP, or get demonetized within 30 days due to:
1. **Reused Content (Policy 4.1)**: Scraping Reddit/Wikipedia or reusing generic B-roll compilations without original commentary.
2. **Repetitious Content (Policy 4.2)**: Mass-producing mechanical, identical template videos with robotic monotone speech.
3. **Synthetic Media Non-Disclosure**: Failing to declare AI-generated realistic imagery under YouTube's 2024+ regulations.

### How ApexTube Solves This & Protects Your Channel:
- **Transformative Narrative Engine**: Every script is written using proven retention frameworks (Disruption Hook -> Curiosity Gap -> Deep Mechanism -> Actionable Lesson -> Seamless Loop Hook).
- **Approved Reference Style Renders**:
  - **🍋 The Curious Plot Style (`curious_leverage`)**: 2D vector motion graphic engine with radial indigo spotlight, bold typography with 3D drop shadows, live wallet counter, 4-tier leverage stage tracker, formula cards, animated vector characters & stalls, and synchronized Foley sound effects (coin clinks, level-up chimes, cash registers).
  - **🧬 Zack D. Films Style (`simulation_explainer`)**: Biomechanical 3D mannequin simulations, anatomical cutaways, clinical lighting, heartbeat and bone crack Foley SFX.
  - **💎 Magnates Media Style (`wealth_secrets`)**: High-contrast kinetic b-roll, motion graphics, whoosh transitions, and deep 808 bass riser hits.
- **Multi-Agent YPP Policy Guardian**: Audits every script, title, and visual prompt before rendering. Scores compliance (0-100%) and guarantees the inclusion of mandatory educational disclaimers.
- **Dynamic Neural Speech & Audio Ducking**: Uses Microsoft Edge neural voice synthesis with studio-grade cadence, pitch inflection, and automatic background music ducking normalized to **-14 LUFS**.
- **Dynamic Subtitles**: High-contrast, 2-3 word rapid chunking subtitles in bold yellow with thick black borders, positioned perfectly for vertical Shorts.
- **Zero Computer Slowdown**: Rendering is strictly hard-capped to `threads=2` and lightweight memory buffers (<150MB RAM), keeping your Mac completely fast and responsive during production.

---

## 👥 The Autonomous Agent Squad

| Agent | Codename | Role & Responsibility | Cost |
|---|---|---|---|
| 🧠 **Guru Strategist** | `GuruStrategist` | Analyzes high-CPM niches ($9-$42 CPM), predicts CTR, and crafts curiosity-gap titles. | **$0** (Local) |
| 🛡️ **Policy Guardian** | `PolicyGuardian` | Enforces YouTube Community Guidelines, Fair Use, and Synthetic Media declarations. | **$0** (Local) |
| ✍️ **Retention Writer** | `RetentionWriter` | Generates 5-scene high-AVD scripts with visual prompts, on-screen text, and loop hooks. | **$0** (Local) |
| 🎙️ **Audio Director** | `AudioDirector` | Synthesizes neural voices (`edge-tts`), extracts word subtitles, and creates ambient audio beds + Foley SFX. | **$0** (Free Neural) |
| 📐 **Vector Motion Engine** | `VectorMotionEngine` | Renders crisp 2D vector motion graphics, stage trackers, formula cards, and animated characters (*The Curious Plot*). | **$0** (Pure Python/Pillow) |
| 🎨 **Visual Engine** | `VisualEngine` | Generates photorealistic scene visuals + 3D mannequin assets + High-CTR Thumbnails. | **$0** (Free API) |
| 🎬 **Video Compositor** | `VideoCompositor` | FFmpeg-powered engine that renders Ken Burns camera animations, burns captions, and exports MP4. | **$0** (FFmpeg) |
| 🚀 **Publisher & SEO** | `PublisherSEO` | Generates SEO descriptions, 30 tags, hashtags, and a 1-click YouTube Data API v3 upload script. | **$0** (Official API) |

---

## 💰 Top High-CPM / Viral Niches Built-In

1. **🍋 Business Leverage Metaphors (The Curious Plot Style)** (CPM: `$22.00 - $42.00`)
   - *Target Audience*: Entrepreneurs, wealth builders, ambitious professionals.
   - *Visual Style*: 2D vector motion graphics, radial spotlight, live wallet counter, 4-tier stage tracker, formula cards, lemonade stall duplicates.
   - *SFX*: Coin clink, level-up chime, cash register.
2. **🧬 3D Mannequin Simulation (Zack D. Style)** (CPM: `$12.00 - $25.00`)
   - *Target Audience*: Curious viewers worldwide (high viral replay loops).
   - *Visual Style*: 3D human mannequin simulation, anatomical cutaways, glowing bones.
   - *SFX*: Heartbeat, bone crack, whooshes.
3. **💎 Hidden Wealth & Financial Secrets (Magnates Media Style)** (CPM: `$18.00 - $38.00`)
   - *Target Audience*: Aspiring investors, entrepreneurs.
   - *Visual Style*: Dark cinematic stock footage, documentary overlays, kinetic zooms.
   - *SFX*: Deep 808 boom, risers, whoosh transitions.
4. **Dark Psychology & Human Behavior** (CPM: `$9.00 - $17.50`)
5. **Modern Stoicism & High Performance** (CPM: `$8.00 - $16.00`)

---

## ⚡ Quick Start Guide

### 1. Launch the Interactive Web Studio
```bash
source .venv/bin/activate
python run_studio.py
```
Open **`http://localhost:8000`** in your browser. You can:
- Explore niches and review real-time CPM forecasts.
- Click **"Optimize Topic"** or select curated viral topics.
- Check the **YPP Policy Meter** (ensures your channel stays safe).
- Preview and select from 6 studio neural voices.
- Click **"Produce High-Quality Video (1-Click)"** and watch the finished video directly in the web player.
- Copy your optimized YouTube SEO description and 30 tags.

---

### 2. Headless CLI Production (For Batch Automation)
You can also generate videos directly from the terminal:
```bash
# Produce The Curious Plot style 2D vector leverage short
source .venv/bin/activate
python cli.py --niche curious_leverage --format shorts

# Produce a Zack D. style 3D mannequin explainer
python cli.py --niche simulation_explainer --format shorts

# Produce a Magnates Media style financial deep-dive
python cli.py --niche wealth_secrets --format shorts
```

---

### 3. Automated Scheduling & Auto-Pilot
To run autonomous scheduled batches in the background:
```bash
python auto_pilot.py --batch 3
```
This produces 3 ready-to-publish videos, deposits them into `output/ready_to_publish/`, and triggers a native macOS notification when complete.

---

## 📡 1-Click YouTube Publishing Setup (Free)
Every video produced creates an automated upload script in `output/{session_id}_publish_to_youtube.py`.

To enable direct automated upload to your YouTube channel:
1. Go to the [Google Cloud Console](https://console.cloud.google.com/) (100% free).
2. Create a project and enable the **YouTube Data API v3**.
3. Go to **APIs & Services > Credentials > Create Credentials > OAuth client ID (Desktop app)**.
4. Download the JSON file and save it in this directory as **`client_secret.json`**.
5. Run:
   ```bash
   python output/<session_id>_publish_to_youtube.py
   ```
   *Your video, custom thumbnail, title, tags, and description will be published directly to your YouTube channel!*

---

## 🔒 YouTube Partner Program (YPP) Compliance Checklist

| Policy Requirement | How ApexTube Complies |
|---|---|
| **Original Commentary** | Scripts provide transformative analysis and philosophical synthesis rather than raw scraped text. |
| **No Repetitious Cadence** | Sentences vary between short impact punches and analytical explanations. |
| **Synthetic Media Transparency** | Metadata automatically flags `hasAlteredOrSyntheticContent: true` adhering to YouTube 2024 mandates. |
| **Monetization Disclaimers** | High-stakes niches (finance, psychology) include mandatory educational disclaimers to prevent deceptive practice strikes. |
