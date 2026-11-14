"""
GuruStrategist - YouTube Monetization Guru & Content Strategist Agent
Analyzes high-CPM niches, optimizes viral velocity, crafts irresistible hook formulas,
and engineers thumbnail concepts designed for 10%+ CTR.
"""

from typing import Dict, List, Any, Optional
from pydantic import BaseModel, Field
from app.config import NICHES, VOICES


class TitleConcept(BaseModel):
    title: str
    archetype: str  # "Curiosity Gap", "Contrarian Take", "Urgency/High-Stakes"
    predicted_ctr: str
    target_emotion: str


class ThumbnailConcept(BaseModel):
    focal_subject: str
    background_elements: str
    lighting_style: str
    overlay_text: str  # 2-4 punchy words max
    color_palette: str


class VideoStrategy(BaseModel):
    niche_key: str
    niche_name: str
    topic: str
    estimated_cpm: str
    viral_velocity_score: int = Field(ge=1, le=100)
    hook_angle: str
    titles: List[TitleConcept]
    primary_title: str
    thumbnail_concept: ThumbnailConcept
    target_audience: str
    recommended_voice: str
    monetization_playbook: str


class GuruStrategist:
    def __init__(self):
        self.niches = NICHES

    def get_supported_niches(self) -> Dict[str, Any]:
        return self.niches

    def formulate_strategy(self, niche_key: str, custom_topic: Optional[str] = None) -> VideoStrategy:
        if niche_key not in self.niches:
            niche_key = "dark_psychology"

        niche_info = self.niches[niche_key]

        # Curated viral topic banks if user doesn't pass a specific custom topic
        topic_vault = {
            "curious_leverage": [
                {
                    "topic": "$20 → $120,000 With a Lemonade Stand 🍋 (4 Levels of Leverage)",
                    "hook": "$20 to $120,000 using nothing but a lemonade stand. Here are the 4 levels of leverage most people never find.",
                    "titles": [
                        TitleConcept(
                            title="$20 → $120,000 With a Lemonade Stand 🍋 (4 Levels of Leverage)",
                            archetype="Curiosity Gap",
                            predicted_ctr="15.8%",
                            target_emotion="Business Curiosity & Epiphany"
                        ),
                        TitleConcept(
                            title="How $20 Becomes $120,000 (The 4 Levels of Leverage)",
                            archetype="High-Stakes Metaphor",
                            predicted_ctr="14.6%",
                            target_emotion="Wealth Building"
                        ),
                        TitleConcept(
                            title="Why Working Harder Never Makes You Rich (The Lemonade Secret)",
                            archetype="Contrarian Take",
                            predicted_ctr="13.9%",
                            target_emotion="Mindset Shift"
                        ),
                    ],
                    "thumbnail": ThumbnailConcept(
                        focal_subject="2D vector motion graphic, cute lemonade stand with glass pitcher and gold coins, hero text $20 -> $120,000 with 3D shadow",
                        background_elements="Radial indigo spotlight, 4-tier leverage stage tracker, glowing gold coins",
                        lighting_style="Vibrant clean vector lighting, high-contrast yellow and indigo",
                        overlay_text="$20 TO $120,000?",
                        color_palette="Lemon Yellow, Deep Indigo, Crisp White, Emerald Green"
                    ),
                    "viral_score": 98,
                }
            ],
            "simulation_explainer": [
                {
                    "topic": "How To Survive A Marathon Doing The Worm",
                    "hook": "If you tried to finish an entire twenty-six mile marathon exclusively doing the worm, here is the brutal toll on your body.",
                    "titles": [
                        TitleConcept(
                            title="How To Survive A Marathon Doing The Worm 😳",
                            archetype="Curiosity Gap",
                            predicted_ctr="14.8%",
                            target_emotion="Shock & Curiosity"
                        ),
                        TitleConcept(
                            title="What Happens To Your Body If You Do The Worm For 26 Miles",
                            archetype="High-Stakes",
                            predicted_ctr="13.5%",
                            target_emotion="Anatomical Fascination"
                        ),
                        TitleConcept(
                            title="Why You Cannot Finish A Marathon Doing The Worm",
                            archetype="Contrarian Take",
                            predicted_ctr="12.2%",
                            target_emotion="Scientific Skepticism"
                        ),
                    ],
                    "thumbnail": ThumbnailConcept(
                        focal_subject="3D human mannequin doing the worm motion on a paved road, glowing red friction points on ribs and chin, anatomical skeletal cross-section",
                        background_elements="Marathon finish line banner in distance, clinical HUD telemetry gauges",
                        lighting_style="High-contrast clinical 3D lighting, Unreal Engine 5 render, glowing warning indicators",
                        overlay_text="DO THE WORM?",
                        color_palette="Asphalt Grey, Warning Crimson, Neon Cyan"
                    ),
                    "viral_score": 99,
                },
                {
                    "topic": "What Happens If You Swallow A Magnet And A Coin",
                    "hook": "If you swallow a single coin, your body passes it harmlessly. But if you swallow a magnet with it, a medical nightmare begins.",
                    "titles": [
                        TitleConcept(
                            title="What Happens If You Swallow A Magnet And A Coin 🧲",
                            archetype="Curiosity Gap",
                            predicted_ctr="15.2%",
                            target_emotion="Morbid Curiosity"
                        ),
                        TitleConcept(
                            title="Why Swallowing A Magnet Is 100x More Dangerous Than A Coin",
                            archetype="High-Stakes",
                            predicted_ctr="14.1%",
                            target_emotion="Urgent Warning"
                        ),
                        TitleConcept(
                            title="Doctors Warn: Never Let Children Play With These Two Objects",
                            archetype="Urgency/High-Stakes",
                            predicted_ctr="13.0%",
                            target_emotion="Protective Suspense"
                        ),
                    ],
                    "thumbnail": ThumbnailConcept(
                        focal_subject="3D anatomical transparent human abdomen showing glowing neodymium magnet clamping to a metal coin through intestinal wall, red tear warning",
                        background_elements="Dark medical radiology scan background, clinical depth of field",
                        lighting_style="High-contrast neon cyan and emergency crimson backlight",
                        overlay_text="MAGNET TRAP",
                        color_palette="Radiology Blue, Emergency Red, Chrome"
                    ),
                    "viral_score": 98,
                },
                {
                    "topic": "Why You Should Never Pop A Pimple In The Danger Triangle",
                    "hook": "There is a triangular zone on your face where popping a single pimple can send a fatal infection directly to your brain.",
                    "titles": [
                        TitleConcept(
                            title="Why You Should NEVER Pop A Pimple In This Zone ⚠️",
                            archetype="Urgency/High-Stakes",
                            predicted_ctr="15.5%",
                            target_emotion="Fear & Fascination"
                        ),
                        TitleConcept(
                            title="The 'Danger Triangle' On Your Face That Can Kill You",
                            archetype="Curiosity Gap",
                            predicted_ctr="14.4%",
                            target_emotion="Intense Curiosity"
                        ),
                        TitleConcept(
                            title="What Doctors Secretly Fear When Patients Pop Facial Blemishes",
                            archetype="Contrarian Take",
                            predicted_ctr="13.2%",
                            target_emotion="Medical Revelation"
                        ),
                    ],
                    "thumbnail": ThumbnailConcept(
                        focal_subject="3D stylized human mannequin face with glowing red geometric triangle over nose and mouth, veins pulsing upward toward brain socket",
                        background_elements="Medical laboratory monitor with skull X-ray",
                        lighting_style="Chiaroscuro studio rim light with glowing anatomical vein highlights",
                        overlay_text="DANGER ZONE",
                        color_palette="Obsidian Black, Bio-Hazard Yellow, Vein Crimson"
                    ),
                    "viral_score": 99,
                }
            ],
            "dark_psychology": [
                {
                    "topic": "The 3-Second Eye Contact Trick That Exposes Liars",
                    "hook": "Psychologists discovered an involuntary micro-reaction the human eye does when telling a deception.",
                    "titles": [
                        TitleConcept(
                            title="The 3-Second Eye Trick That Exposes Any Liar",
                            archetype="Curiosity Gap",
                            predicted_ctr="11.4%",
                            target_emotion="Intense Curiosity"
                        ),
                        TitleConcept(
                            title="Psychologists Warn: Never Ignore This Eye Movement",
                            archetype="Urgency/High-Stakes",
                            predicted_ctr="10.8%",
                            target_emotion="Protective Suspense"
                        ),
                        TitleConcept(
                            title="Why Skilled Manipulators Never Look You in the Left Eye",
                            archetype="Contrarian Take",
                            predicted_ctr="9.7%",
                            target_emotion="Fascination"
                        ),
                    ],
                    "thumbnail": ThumbnailConcept(
                        focal_subject="Dramatic extreme close-up of a human eye with a dilated glowing pupil reflecting shadows",
                        background_elements="Dark cinematic background, forensic grid lines, moody neon rim light",
                        lighting_style="Chiaroscuro high contrast, deep shadows with vivid cyan/amber accents",
                        overlay_text="THEY'RE LYING",
                        color_palette="Obsidian Black, Neon Cyan, Warning Amber"
                    ),
                    "viral_score": 94,
                },
                {
                    "topic": "The Silent Treatment Defense: How To Turn It Against Them",
                    "hook": "When a narcissist gives you the silent treatment, they expect panic. Here is the move that destroys their leverage.",
                    "titles": [
                        TitleConcept(
                            title="How To Turn The Silent Treatment Against Them",
                            archetype="Curiosity Gap",
                            predicted_ctr="12.1%",
                            target_emotion="Empowerment"
                        ),
                        TitleConcept(
                            title="The 1 Word That Destroys A Manipulator's Silence",
                            archetype="Contrarian Take",
                            predicted_ctr="10.9%",
                            target_emotion="Revelation"
                        ),
                        TitleConcept(
                            title="Never Break Their Silence (Do This Instead)",
                            archetype="Urgency/High-Stakes",
                            predicted_ctr="11.8%",
                            target_emotion="Authority"
                        ),
                    ],
                    "thumbnail": ThumbnailConcept(
                        focal_subject="Silhouetted figure sitting with back turned while another figure walks away confidently into light",
                        background_elements="Smoky atmosphere, cold blue shadows",
                        lighting_style="Cold spotlight contrasting with warm silhouette",
                        overlay_text="LET THEM GO",
                        color_palette="Cold Navy, Electric White, Gold"
                    ),
                    "viral_score": 92,
                }
            ],
            "wealth_secrets": [
                {
                    "topic": "Why The Wealthy Borrow Against Assets Instead of Selling",
                    "hook": "Billionaires pay almost zero capital gains tax legally. They use a three-word strategy called Buy, Borrow, Die.",
                    "titles": [
                        TitleConcept(
                            title="The 3-Word Rule Billionaires Use To Pay 0% Tax",
                            archetype="Curiosity Gap",
                            predicted_ctr="13.2%",
                            target_emotion="Financial Ambition"
                        ),
                        TitleConcept(
                            title="Why Rich People Never Sell Their Assets (Legal Loophole)",
                            archetype="Contrarian Take",
                            predicted_ctr="11.5%",
                            target_emotion="Insider Knowledge"
                        ),
                        TitleConcept(
                            title="Stop Saving In Cash: The Wealth Trap Keeping You Broke",
                            archetype="Urgency/High-Stakes",
                            predicted_ctr="10.3%",
                            target_emotion="Urgency"
                        ),
                    ],
                    "thumbnail": ThumbnailConcept(
                        focal_subject="Sleek vault door cracked open with warm golden light spilling over stacks of money and blueprint documents",
                        background_elements="Architectural brutalist concrete wall, luxury corporate aesthetic",
                        lighting_style="High-end cinematic warm gold key lighting",
                        overlay_text="PAY ZERO",
                        color_palette="Charcoal Grey, Platinum, Rich Gold"
                    ),
                    "viral_score": 96,
                }
            ],
            "modern_stoicism": [
                {
                    "topic": "Marcus Aurelius: The Rule For Never Getting Angry",
                    "hook": "The Roman Emperor ruled the entire known world, yet wrote in his private journal: 'When you wake up, expect betrayal.'",
                    "titles": [
                        TitleConcept(
                            title="Marcus Aurelius: The Secret To Being Untouchable",
                            archetype="Curiosity Gap",
                            predicted_ctr="12.5%",
                            target_emotion="Inner Strength"
                        ),
                        TitleConcept(
                            title="The Stoic Rule That Makes Disrespect Completely Harmless",
                            archetype="Contrarian Take",
                            predicted_ctr="11.2%",
                            target_emotion="Discipline"
                        ),
                        TitleConcept(
                            title="Never React Instantly: The 10-Second Stoic Law",
                            archetype="Urgency/High-Stakes",
                            predicted_ctr="10.7%",
                            target_emotion="Self-Control"
                        ),
                    ],
                    "thumbnail": ThumbnailConcept(
                        focal_subject="Weathered marble bust of Marcus Aurelius with dramatic side lighting and rain droplets",
                        background_elements="Colosseum ruins in stormy background with lightning",
                        lighting_style="Dramatic moody film chiaroscuro",
                        overlay_text="BE SILENT",
                        color_palette="Stone Grey, Lightning Blue, Pure White"
                    ),
                    "viral_score": 91,
                }
            ],
            "future_tech": [
                {
                    "topic": "Autonomous AI Agents Running Entire Companies in 2026",
                    "hook": "A single engineer just built a software firm that reached 10 million in revenue with zero employees. Here is the exact stack.",
                    "titles": [
                        TitleConcept(
                            title="The 1-Person Billion Dollar Company Is Already Here",
                            archetype="Contrarian Take",
                            predicted_ctr="12.8%",
                            target_emotion="Awe & Disruption"
                        ),
                        TitleConcept(
                            title="AI Agents Just Replaced Entire Corporate Departments",
                            archetype="Urgency/High-Stakes",
                            predicted_ctr="11.6%",
                            target_emotion="Curiosity & Fear"
                        ),
                        TitleConcept(
                            title="The Autonomous Economy: Why 9-to-5 Is Quietly Dying",
                            archetype="Curiosity Gap",
                            predicted_ctr="10.9%",
                            target_emotion="Visionary"
                        ),
                    ],
                    "thumbnail": ThumbnailConcept(
                        focal_subject="Futuristic robotic android hand calmly operating an ultra-modern glowing glass control board",
                        background_elements="Glass skyscrapers at dusk with holographic data streams",
                        lighting_style="Cyberpunk dusk, magenta and cyan highlights",
                        overlay_text="0 EMPLOYEES",
                        color_palette="Deep Violet, Cyan Neon, Chrome"
                    ),
                    "viral_score": 95,
                }
            ],
            "unsolved_mysteries": [
                {
                    "topic": "The 1977 Wow Signal: What Deep Space Actually Sent Us",
                    "hook": "For 72 seconds, an Ohio telescope detected a narrowband radio transmission from 18,000 light years away. It was never heard again.",
                    "titles": [
                        TitleConcept(
                            title="The 72-Second Deep Space Signal That Terrified NASA",
                            archetype="Curiosity Gap",
                            predicted_ctr="13.5%",
                            target_emotion="Cosmic Dread"
                        ),
                        TitleConcept(
                            title="Scientists Finally Decoded The 1977 Space Transmission",
                            archetype="Contrarian Take",
                            predicted_ctr="11.9%",
                            target_emotion="Revelation"
                        ),
                        TitleConcept(
                            title="We Received A Signal In 1977. Then Space Went Completely Silent.",
                            archetype="Urgency/High-Stakes",
                            predicted_ctr="12.1%",
                            target_emotion="Suspense"
                        ),
                    ],
                    "thumbnail": ThumbnailConcept(
                        focal_subject="Massive observatory radio dish pointed at a pitch black star-filled cosmos with an enigmatic glowing frequency wave",
                        background_elements="Nebula dust, vintage computer terminal showing '6EQUJ5'",
                        lighting_style="Eerie cosmic glow, cold dark blue tones",
                        overlay_text="THE SIGNAL",
                        color_palette="Cosmic Navy, Crimson Red, Starlight White"
                    ),
                    "viral_score": 97,
                }
            ]
        }

        # Select preset or craft strategy for custom topic
        selected_data = topic_vault.get(niche_key, topic_vault["dark_psychology"])[0]
        final_topic = custom_topic if custom_topic and custom_topic.strip() else selected_data["topic"]

        if custom_topic and custom_topic.strip():
            # Build custom high-CTR title variations
            titles = [
                TitleConcept(
                    title=f"The Hidden Truth Behind {custom_topic}",
                    archetype="Curiosity Gap",
                    predicted_ctr="11.8%",
                    target_emotion="Curiosity"
                ),
                TitleConcept(
                    title=f"Why Everyone Is Wrong About {custom_topic}",
                    archetype="Contrarian Take",
                    predicted_ctr="10.5%",
                    target_emotion="Provocative"
                ),
                TitleConcept(
                    title=f"Before You Deal With {custom_topic}, Watch This",
                    archetype="Urgency/High-Stakes",
                    predicted_ctr="11.1%",
                    target_emotion="Urgency"
                ),
            ]
            thumbnail = ThumbnailConcept(
                focal_subject=f"Dramatic cinematic representation of {custom_topic}",
                background_elements="High contrast moody lighting with deep shadows and vibrant rim accents",
                lighting_style="Atmospheric cinematic chiaroscuro",
                overlay_text="THE TRUTH",
                color_palette="High-contrast darks with bold yellow/cyan focal glow"
            )
            hook_angle = f"Exposing the counter-intuitive reality of {custom_topic} in the first 3 seconds."
            viral_score = 90
        else:
            titles = selected_data["titles"]
            thumbnail = selected_data["thumbnail"]
            hook_angle = selected_data["hook"]
            viral_score = selected_data["viral_score"]

        playbook = (
            f"1. Hook: Deliver emotional disruption in 0-3s.\n"
            f"2. Retention: Introduce high-stakes curiosity gap by second 6.\n"
            f"3. Pattern Interrupt: Scene visual shifts every 3.5s with dynamic Ken Burns zoom.\n"
            f"4. Payoff: Deliver actionable insight at second 42.\n"
            f"5. Loop Hook: Connect concluding phrase seamlessly into the starting sentence for infinite replays."
        )

        return VideoStrategy(
            niche_key=niche_key,
            niche_name=niche_info["name"],
            topic=final_topic,
            estimated_cpm=niche_info["cpm_range"],
            viral_velocity_score=viral_score,
            hook_angle=hook_angle,
            titles=titles,
            primary_title=titles[0].title,
            thumbnail_concept=thumbnail,
            target_audience=niche_info["target_audience"],
            recommended_voice=niche_info["voice_recommendation"],
            monetization_playbook=playbook
        )

