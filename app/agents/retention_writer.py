"""
RetentionWriter - High-AVD Scriptwriting & Narrative Pacing Agent
Follows retention-engineered frameworks (Hook, Curiosity Gap, Pattern Interrupts, Micro-Cliffhangers,
and Seamless Loop Engineering) to maximize YouTube Average Percentage Viewed (APV).
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from app.config import VIDEO_CONFIGS


class ScriptScene(BaseModel):
    scene_number: int
    narration: str
    visual_prompt: str
    on_screen_text: str
    camera_motion: str  # "zoom_in", "zoom_out", "pan_left", "pan_right"
    sound_effect: str   # "whoosh", "deep_boom", "impact", "glitch", "riser"
    estimated_duration: float  # seconds
    wallet_amount: Optional[str] = None
    hero_text: Optional[str] = None
    level_str: Optional[str] = None
    formula_text: Optional[str] = None
    active_level: Optional[int] = 1


class RetentionScript(BaseModel):
    niche: str
    topic: str
    title: str
    format: str  # "shorts" or "horizontal"
    scenes: List[ScriptScene]
    full_narration: str
    total_words: int
    estimated_duration_sec: float
    loop_engineered: bool
    policy_disclaimer: Optional[str] = None


class RetentionWriter:
    def __init__(self):
        # Master templates engineered with retention psychology
        self.preset_scripts = {
            "curious_leverage": [
                {
                    "title": "$20 → $120,000 With a Lemonade Stand 🍋 (4 Levels of Leverage)",
                    "scenes": [
                        {
                            "narration": "$20 to $120,000 using nothing but a lemonade stand. Here are the four levels of leverage most people never find.",
                            "visual_prompt": "2D vector motion graphic, dark indigo spotlight, hero text $20 -> $120,000 with 3D drop shadow, The Curious Plot style",
                            "on_screen_text": "LEMONADE METAPHOR",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 4.5,
                            "wallet_amount": "$20",
                            "hero_text": "$20 -> $120,000",
                            "level_str": "4 LEVELS OF LEVERAGE",
                            "formula_text": "$20 TO $120,000",
                            "active_level": 1
                        },
                        {
                            "narration": "Level one: Labor. Leo spends twenty dollars on lemons and cups. He works eight hours, pours eighty cups at one dollar each, and makes eighty dollars. If he stops pouring, the money stops.",
                            "visual_prompt": "Level 1 Labor, single lemonade stand with character Leo, $20 = 80 cups, 2D vector style",
                            "on_screen_text": "LEVEL 1: LABOR",
                            "camera_motion": "pan_left",
                            "sound_effect": "coin_clink",
                            "estimated_duration": 6.5,
                            "wallet_amount": "$80",
                            "hero_text": "$80",
                            "level_str": "LEVEL 1: LABOR",
                            "formula_text": "$20 = 80 CUPS",
                            "active_level": 1
                        },
                        {
                            "narration": "Level two: Capital. Leo uses his profits to buy two more stands and pays two helpers to run them. Now three stands sell eighty cups each. Even after paying his team, Leo keeps sixty dollars of pure profit without pouring a cup.",
                            "visual_prompt": "Level 2 Capital, 3 lemonade stands with 3 helpers, 20% of every sale, 2D vector style",
                            "on_screen_text": "LEVEL 2: CAPITAL",
                            "camera_motion": "zoom_in",
                            "sound_effect": "level_up",
                            "estimated_duration": 6.5,
                            "wallet_amount": "$140",
                            "hero_text": "$140",
                            "level_str": "LEVEL 2: CAPITAL",
                            "formula_text": "20% OF EVERY SALE",
                            "active_level": 2
                        },
                        {
                            "narration": "Level three: Systems. Leo packages his secret strawberry lemonade recipe into bottled six-packs for five local grocery stores, and sells a nine-dollar recipe guide online. Serving ten thousand customers takes the exact same effort as serving ten.",
                            "visual_prompt": "Level 3 Systems, 5 shops with bottled juice and digital recipe guide card, 2D vector style",
                            "on_screen_text": "LEVEL 3: SYSTEMS",
                            "camera_motion": "zoom_out",
                            "sound_effect": "coin_clink",
                            "estimated_duration": 7.0,
                            "wallet_amount": "$3,873",
                            "hero_text": "$3,873",
                            "level_str": "LEVEL 3: SYSTEMS",
                            "formula_text": "5 SHOPS x 200 BOTTLES",
                            "active_level": 3
                        },
                        {
                            "narration": "Level four: Deals. An organic beverage conglomerate notices Leo's brand, systems, and distribution. They offer him one hundred twenty thousand dollars for the business. Same lemons. Only the leverage changed. Which level are you on right now? Tell me in the comments.",
                            "visual_prompt": "Level 4 Deals, corporate headquarters Lemon Corp with team celebrating, franchise valuation, 2D vector style",
                            "on_screen_text": "LEVEL 4: DEALS",
                            "camera_motion": "zoom_in",
                            "sound_effect": "cash_register",
                            "estimated_duration": 7.5,
                            "wallet_amount": "$120,000",
                            "hero_text": "$120,000",
                            "level_str": "LEVEL 4: DEALS",
                            "formula_text": "FRANCHISE VALUATION",
                            "active_level": 4
                        }
                    ],
                    "loop_engineered": True,
                    "disclaimer": "Educational business leverage metaphor. Not guaranteed financial return claims."
                }
            ],
            "simulation_explainer": [
                {
                    "title": "How To Survive A Marathon Doing The Worm 😳",
                    "scenes": [
                        {
                            "narration": "If you ever tried to finish an entire twenty-six mile marathon exclusively doing the worm dance move, here is the brutal reality of what happens to your body.",
                            "visual_prompt": "3D stylized human mannequin starting the worm motion on a paved asphalt marathon track, Blender 3D render, Unreal Engine 5 simulation, dramatic clinical lighting, Zack D Films style",
                            "on_screen_text": "MARATHON BY WORM",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 4.5
                        },
                        {
                            "narration": "A single worm ripple moves you forward about three feet. To complete twenty-six miles, you would need to execute over forty-six thousand consecutive ripples.",
                            "visual_prompt": "3D human mannequin executing continuous worm ripples on asphalt road, floating telemetry HUD counter showing 46,000 REPS, motion trail arcs, 3D physical simulation",
                            "on_screen_text": "46,000 RIPPLES",
                            "camera_motion": "pan_left",
                            "sound_effect": "whoosh",
                            "estimated_duration": 5.5
                        },
                        {
                            "narration": "Within the first two miles, the abrasive asphalt would grind through your clothes, completely shredding the skin on your chin, knees, and toes down to the bare bone.",
                            "visual_prompt": "Extreme close-up 3D anatomical cutaway of human mannequin chin and knee joints grinding violently against rough asphalt, glowing red friction heat, skeletal cross-section",
                            "on_screen_text": "BONE EXPOSURE",
                            "camera_motion": "zoom_in",
                            "sound_effect": "impact",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "Your spine would endure thousands of violent hyper-extension flexes, causing severe lumbar disc compression and fracturing the cartilage across your ribcage.",
                            "visual_prompt": "3D transparent mannequin glowing anatomical spine flexing violently in mid-air, red stress points highlighting lumbar vertebrae and cracked rib cartilage, medical 3D simulation",
                            "on_screen_text": "SPINE DAMAGE",
                            "camera_motion": "zoom_out",
                            "sound_effect": "riser",
                            "estimated_duration": 5.5
                        },
                        {
                            "narration": "Since your hands are pinned to the asphalt, you cannot hold a bottle. You would need an assistant running beside you, pouring water directly onto the road so you could drink like a hamster.",
                            "visual_prompt": "3D stylized mannequin face down drinking water puddle on the road like a hamster, animated runner beside holding water jug, humorous medical 3D simulation",
                            "on_screen_text": "DRINK LIKE A HAMSTER",
                            "camera_motion": "zoom_in",
                            "sound_effect": "whoosh",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "By mile ten, massive muscle breakdown would flood your bloodstream with toxic myoglobin, causing total kidney failure before the finish line. So if you ever thought about trying this... don't.",
                            "visual_prompt": "3D anatomical cross-section of glowing human kidneys flashing red critical warning indicators, dramatic medical telemetry HUD, mannequin collapsing on track, Zack D Films aesthetic",
                            "on_screen_text": "KIDNEYS COLLAPSE",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 6.5
                        }
                    ],
                    "loop_engineered": True,
                    "disclaimer": "Hypothetical physics and biomechanical simulation for educational entertainment."
                },
                {
                    "title": "What Happens If You Swallow A Magnet And A Coin 🧲",
                    "scenes": [
                        {
                            "narration": "If you swallow a single metal coin, your digestive tract usually passes it without any serious issues. But if you swallow a neodymium magnet with it, a medical nightmare begins.",
                            "visual_prompt": "3D stylized human mannequin swallowing glowing magnet and shiny metal coin, transparent X-ray throat view, Blender 3D render, clinical studio lighting, Zack D Films style",
                            "on_screen_text": "MAGNET & COIN",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 5.5
                        },
                        {
                            "narration": "Inside your intestines, the magnet and coin travel through separate digestive loops at completely different speeds.",
                            "visual_prompt": "3D transparent anatomical abdomen showing glowing magnet and coin moving down separate intestinal folds, medical simulation",
                            "on_screen_text": "SEPARATE LOOPS",
                            "camera_motion": "pan_left",
                            "sound_effect": "whoosh",
                            "estimated_duration": 5.0
                        },
                        {
                            "narration": "As the intestinal folds brush together, the powerful magnetic field pulls the coin and magnet violently toward each other through the tissue wall.",
                            "visual_prompt": "Extreme macro 3D cutaway of magnetic attraction clamping two intestinal walls together, red pressure lines glowing, physical simulation",
                            "on_screen_text": "MAGNETIC CLAMP",
                            "camera_motion": "zoom_in",
                            "sound_effect": "impact",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "This pinches the blood vessels completely shut, causing the trapped tissue to die within hours and tearing a hole in your digestive tract.",
                            "visual_prompt": "3D medical cross section showing necrotic tissue tear between clamped bowel walls, red warning telemetry flashing, anatomical simulation",
                            "on_screen_text": "TISSUE NECROSIS",
                            "camera_motion": "zoom_out",
                            "sound_effect": "riser",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "Digestive enzymes and bacteria immediately flood your abdominal cavity, causing rapid sepsis unless surgeons cut you open to remove them. So if you ever swallow a magnet... seek an emergency room immediately.",
                            "visual_prompt": "3D mannequin on surgical operating table with holographic emergency HUD telemetry flashing EMERGENCY SURGERY, dramatic clinical lighting, Zack D Films style",
                            "on_screen_text": "EMERGENCY SURGERY",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 6.5
                        }
                    ],
                    "loop_engineered": True,
                    "disclaimer": "Medical physics breakdown for educational safety awareness."
                },
                {
                    "title": "Why You Should NEVER Pop A Pimple In This Zone ⚠️",
                    "scenes": [
                        {
                            "narration": "There is a specific zone on your face known as the Danger Triangle that stretches from the bridge of your nose down to the corners of your mouth.",
                            "visual_prompt": "3D human mannequin face with glowing red geometric triangle highlighted over nose and upper lips, medical diagnostic studio render, Zack D Films style",
                            "on_screen_text": "THE DANGER TRIANGLE",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 5.0
                        },
                        {
                            "narration": "Unlike almost all other veins in your body, the facial veins in this triangle do not have one-way valves, meaning blood can flow directly backward toward your brain.",
                            "visual_prompt": "3D anatomical skull cross-section showing facial veins with arrows illustrating backward blood flow toward the cranial vault, glowing cyan veins",
                            "on_screen_text": "NO VALVES = BACKFLOW",
                            "camera_motion": "pan_left",
                            "sound_effect": "whoosh",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "When you forcefully squeeze a deep blemish here, the mechanical pressure can push bacterial pus backward into the cavernous sinus—a major venous channel right behind your eyes.",
                            "visual_prompt": "Extreme macro 3D cutaway of fingernails squeezing a pore, bacteria forced downward into facial bloodstream, glowing red infection trail",
                            "on_screen_text": "PUS FORCED INWARD",
                            "camera_motion": "zoom_in",
                            "sound_effect": "impact",
                            "estimated_duration": 6.5
                        },
                        {
                            "narration": "This can cause a massive blood clot known as cavernous sinus thrombosis, leading to vision loss, paralysis of facial nerves, and severe brain infections.",
                            "visual_prompt": "3D transparent brain model highlighting cavernous sinus blood clot pulsing in warning amber and red, medical simulation telemetry",
                            "on_screen_text": "BRAIN CLOT RISK",
                            "camera_motion": "zoom_out",
                            "sound_effect": "riser",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "While rare, dermatologists warn that popping a pimple in the triangle is literally gambling with your nervous system. So leave that blemish alone.",
                            "visual_prompt": "3D stylized mannequin with hands raised away from face, clinical laboratory backdrop, bold warning telemetry HUD overlay",
                            "on_screen_text": "DO NOT POP",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 5.5
                        }
                    ],
                    "loop_engineered": True,
                    "disclaimer": "Dermatological and anatomical education for health awareness."
                }
            ],
            "dark_psychology": [
                {
                    "title": "The 3-Second Eye Trick That Exposes Any Liar",
                    "scenes": [
                        {
                            "narration": "If someone ever looks away to their upper right while answering you, pay very close attention.",
                            "visual_prompt": "Extreme macro close-up of human eyes darting to the upper right corner, moody chiaroscuro cinematic lighting, dark background, 8k hyperrealistic",
                            "on_screen_text": "WATCH THEIR EYES",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 4.5
                        },
                        {
                            "narration": "Neuroscientists discovered that the human brain accesses creative visualization when fabricating a falsehood, forcing an involuntary eye movement.",
                            "visual_prompt": "Glowing holographic neural network of the human brain firing synapses in high contrast neon blue and gold, dark scientific laboratory",
                            "on_screen_text": "THE BRAIN GLITCH",
                            "camera_motion": "pan_left",
                            "sound_effect": "whoosh",
                            "estimated_duration": 6.5
                        },
                        {
                            "narration": "When recalling an actual memory, their eyes naturally flick down and left to retrieve acoustic and emotional data.",
                            "visual_prompt": "Cinematic portrait of a thoughtful person in shadow, subtle warm light highlighting the face, serious forensic atmosphere",
                            "on_screen_text": "REAL MEMORY",
                            "camera_motion": "zoom_out",
                            "sound_effect": "impact",
                            "estimated_duration": 5.5
                        },
                        {
                            "narration": "To test this, ask a neutral question like what they ate yesterday, calibrate their baseline, then drop your real question.",
                            "visual_prompt": "Two silhouetted figures seated across an interrogation table, dramatic smoky atmosphere, cold overhead spotlight",
                            "on_screen_text": "CALIBRATE FIRST",
                            "camera_motion": "zoom_in",
                            "sound_effect": "riser",
                            "estimated_duration": 6.5
                        },
                        {
                            "narration": "Because the eyes are the only part of the central nervous system exposed directly to the outside world. And that is why...",
                            "visual_prompt": "Dramatic glowing iris reflecting a mysterious dark silhouette, cinematic depth of field, intense focus",
                            "on_screen_text": "THE TELL",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 5.0
                        }
                    ],
                    "loop_engineered": True,
                    "disclaimer": "Educational psychology breakdown. Not clinical diagnostics."
                }
            ],
            "wealth_secrets": [
                {
                    "title": "The 3-Word Rule Billionaires Use To Pay 0% Tax",
                    "scenes": [
                        {
                            "narration": "The richest one percent never sell their stocks to buy luxury assets. Instead, they use a strategy called Buy, Borrow, Die.",
                            "visual_prompt": "High-end cinematic private bank vault, gleaming gold bullion and financial ledger books illuminated by soft dramatic spotlights",
                            "on_screen_text": "BUY. BORROW. DIE.",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 5.0
                        },
                        {
                            "narration": "When you sell an investment, governments charge up to thirty-seven percent in capital gains tax.",
                            "visual_prompt": "Hand stamping a red tax document with bold typography, high-contrast corporate aesthetic, architectural concrete background",
                            "on_screen_text": "37% LOSS",
                            "camera_motion": "pan_right",
                            "sound_effect": "whoosh",
                            "estimated_duration": 5.0
                        },
                        {
                            "narration": "So the ultra-wealthy deposit their appreciating assets as collateral, borrowing millions at low interest rates.",
                            "visual_prompt": "Sleek modern penthouse overlooking a glowing metropolitan city skyline at night, financial charts glowing on a glass tablet",
                            "on_screen_text": "BORROW AGAINST IT",
                            "camera_motion": "zoom_out",
                            "sound_effect": "impact",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "Because borrowed money is classified as debt by the tax code, it is completely tax-free.",
                            "visual_prompt": "Close-up of a fountain pen signing an exclusive credit facility agreement, executive desk with luxury dark wood",
                            "on_screen_text": "DEBT = 0% TAX",
                            "camera_motion": "zoom_in",
                            "sound_effect": "riser",
                            "estimated_duration": 5.5
                        },
                        {
                            "narration": "Their assets grow faster than the interest, letting them live lavishly without ever losing ownership. Which explains why...",
                            "visual_prompt": "Magnificent high-rise corporate headquarters illuminated under golden hour sunlight, architectural mastery, cinematic composition",
                            "on_screen_text": "OWN NOTHING. CONTROL EVERYTHING.",
                            "camera_motion": "pan_left",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 6.0
                        }
                    ],
                    "loop_engineered": True,
                    "disclaimer": "This video is for educational and entertainment purposes only, not financial advice."
                }
            ],
            "modern_stoicism": [
                {
                    "title": "Marcus Aurelius: The Secret To Being Untouchable",
                    "scenes": [
                        {
                            "narration": "Marcus Aurelius commanded the greatest empire on Earth, yet woke up every morning and wrote one singular warning to himself.",
                            "visual_prompt": "Weathered classical marble statue bust of Marcus Aurelius in profile, dramatic moody chiaroscuro lighting, dark Roman temple backdrop",
                            "on_screen_text": "THE EMPEROR'S RULE",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 5.5
                        },
                        {
                            "narration": "He wrote: When you wake up, prepare to meet the arrogant, the ungrateful, the deceitful, and the jealous.",
                            "visual_prompt": "Ancient Roman forum in the rain, moody dark clouds, lone stoic figure wrapped in a woolen toga standing firm amid chaos",
                            "on_screen_text": "EXPECT BETRAYAL",
                            "camera_motion": "pan_left",
                            "sound_effect": "whoosh",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "He did not say this out of cynicism, but out of total emotional sovereignty.",
                            "visual_prompt": "Close up of an ancient papyrus scroll with Greek script, ink well, flickering candle light casting warm shadows",
                            "on_screen_text": "EMOTIONAL MASTERY",
                            "camera_motion": "zoom_out",
                            "sound_effect": "impact",
                            "estimated_duration": 4.5
                        },
                        {
                            "narration": "When you expect people to be flawed, their disrespect loses all power to wound you. You cannot be disappointed by what you foresaw.",
                            "visual_prompt": "A solitary warrior standing on a mountain cliff overlooking a storm over the sea, tranquil and unyielding",
                            "on_screen_text": "UNSHAKEABLE",
                            "camera_motion": "zoom_in",
                            "sound_effect": "riser",
                            "estimated_duration": 6.5
                        },
                        {
                            "narration": "The moment you stop seeking external validation, you become entirely invincible. And remember...",
                            "visual_prompt": "Dramatic sunrise breaking over ancient stone columns, golden rays cutting through fog, symbol of timeless strength",
                            "on_screen_text": "BE UNTOUCHABLE",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 5.0
                        }
                    ],
                    "loop_engineered": True,
                    "disclaimer": "Stoic philosophy applied to modern psychology and resilience."
                }
            ],
            "future_tech": [
                {
                    "title": "The 1-Person Billion Dollar Company Is Already Here",
                    "scenes": [
                        {
                            "narration": "Sam Altman recently predicted that the first billion-dollar company run by a single human will exist within twenty-four months.",
                            "visual_prompt": "A modern glass office with one solitary founder working on transparent holographic monitors showing hundreds of autonomous AI agents",
                            "on_screen_text": "1 PERSON. $1B.",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 5.5
                        },
                        {
                            "narration": "How? Because AI agents no longer just answer questions. They write full software stacks, conduct marketing, and execute customer support autonomously.",
                            "visual_prompt": "Futuristic server room with glowing blue fiber optic cables pulsing with immense data flows, hyper-detailed cyberpunk aesthetic",
                            "on_screen_text": "AUTONOMOUS SQUADS",
                            "camera_motion": "pan_right",
                            "sound_effect": "whoosh",
                            "estimated_duration": 6.5
                        },
                        {
                            "narration": "Instead of hiring eighty employees, a single creator orchestrates specialized AI agents working twenty-four hours a day with zero burn rate.",
                            "visual_prompt": "Cybernetic robotic hand holding a glowing orb of intricate circuits and microchips, hyperrealistic 8k render",
                            "on_screen_text": "ZERO PAYROLL",
                            "camera_motion": "zoom_out",
                            "sound_effect": "impact",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "The game is no longer about managing people. It is about prompt engineering, system design, and agentic workflows.",
                            "visual_prompt": "Abstract digital network connecting thousands of nodes across a spinning globe, neon cyan and violet lighting",
                            "on_screen_text": "THE NEW LEVERAGE",
                            "camera_motion": "zoom_in",
                            "sound_effect": "riser",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "Those who learn to orchestrate artificial intelligence will possess unimaginable leverage. Which is why...",
                            "visual_prompt": "Silhouette of a visionary looking out over a neon-lit futuristic city of tomorrow, golden glow on horizon",
                            "on_screen_text": "ADAPT OR FADE",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 5.0
                        }
                    ],
                    "loop_engineered": True,
                    "disclaimer": "Analysis of artificial intelligence trends and enterprise automation."
                }
            ],
            "unsolved_mysteries": [
                {
                    "title": "The 72-Second Deep Space Signal That Terrified NASA",
                    "scenes": [
                        {
                            "narration": "On August 15th, 1977, an astronomer sat in a radio observatory in Ohio and witnessed something that defied all laws of known astrophysics.",
                            "visual_prompt": "Giant radio telescope dish pointed into a pitch black star-filled cosmos under a starry night sky, subtle eerie red light",
                            "on_screen_text": "AUGUST 15, 1977",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "A signal spiked at thirty times above background radiation on the hydrogen line frequency of 1420 Megahertz.",
                            "visual_prompt": "Vintage computer printout from 1977 with green phosphor text and dot matrix characters showing '6EQUJ5' circled in red pen",
                            "on_screen_text": "6EQUJ5",
                            "camera_motion": "pan_left",
                            "sound_effect": "whoosh",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "Astronomer Jerry Ehman was so stunned that he grabbed a red pen and scribbled the word 'Wow!' directly onto the dot matrix paper.",
                            "visual_prompt": "Dramatic close up of vintage ink pen handwriting 'Wow!' with an exclamation point on old telemetry paper, dusty dark room",
                            "on_screen_text": "WOW!",
                            "camera_motion": "zoom_out",
                            "sound_effect": "impact",
                            "estimated_duration": 5.5
                        },
                        {
                            "narration": "The transmission lasted exactly seventy-two seconds, the maximum duration the telescope's stationary beam could track any stellar object.",
                            "visual_prompt": "A distant spiral galaxy illuminated against the dark void of deep space, cosmic dust clouds glowing in violet and blue",
                            "on_screen_text": "72 SECONDS",
                            "camera_motion": "zoom_in",
                            "sound_effect": "riser",
                            "estimated_duration": 6.0
                        },
                        {
                            "narration": "For fifty years, scientists have aimed hundreds of telescopes at the exact same coordinate. Only silence ever answered. Until...",
                            "visual_prompt": "Eerie dark cosmic void with a solitary pulsing radio wave radiating toward Earth, cinematic science fiction realism",
                            "on_screen_text": "TOTAL SILENCE",
                            "camera_motion": "zoom_in",
                            "sound_effect": "deep_boom",
                            "estimated_duration": 6.0
                        }
                    ],
                    "loop_engineered": True,
                    "disclaimer": "Historical astronomical documentary. Verified scientific archive."
                }
            ]
        }

    def generate_script(
        self,
        niche: str,
        topic: str,
        title: str,
        format_type: str = "shorts",
        custom_instructions: Optional[str] = None
    ) -> RetentionScript:
        # Check if we have pre-engineered script
        if niche in self.preset_scripts and (not topic or topic == self.preset_scripts[niche][0]["title"] or "eye trick" in topic.lower() or "billionaire" in topic.lower() or "marcus" in topic.lower() or "signal" in topic.lower() or "1-person" in topic.lower()):
            template = self.preset_scripts[niche][0]
            scenes = [ScriptScene(**s, scene_number=i+1) for i, s in enumerate(template["scenes"])]
            full_narration = " ".join(s.narration for s in scenes)
            total_words = len(full_narration.split())
            total_duration = sum(s.estimated_duration for s in scenes)

            return RetentionScript(
                niche=niche,
                topic=topic or template["title"],
                title=title or template["title"],
                format=format_type,
                scenes=scenes,
                full_narration=full_narration,
                total_words=total_words,
                estimated_duration_sec=total_duration,
                loop_engineered=template.get("loop_engineered", True),
                policy_disclaimer=template.get("disclaimer")
            )

        # Dynamic Script Synthesis for custom user topic
        clean_topic = topic if topic and topic.strip() else "The Hidden Rule of Success"
        target_title = title if title and title.strip() else f"The Truth About {clean_topic}"

        # Build 5 retention-engineered narrative scenes
        scenes = [
            ScriptScene(
                scene_number=1,
                narration=f"If you think you understand {clean_topic}, you're falling into the exact trap 99% of people never escape.",
                visual_prompt=f"Dramatic cinematic opening for {clean_topic}, high contrast chiaroscuro lighting, deep shadows with vibrant rim lighting, 8k hyperrealistic",
                on_screen_text="THE TRAP",
                camera_motion="zoom_in",
                sound_effect="deep_boom",
                estimated_duration=5.0
            ),
            ScriptScene(
                scene_number=2,
                narration=f"Most people approach this completely backwards, letting conventional wisdom cloud the underlying reality.",
                visual_prompt=f"Abstract cinematic visual illustrating deception and hidden truth regarding {clean_topic}, moody atmosphere, sleek composition",
                on_screen_text="CONVENTIONAL LIE",
                camera_motion="pan_left",
                sound_effect="whoosh",
                estimated_duration=5.0
            ),
            ScriptScene(
                scene_number=3,
                narration=f"The breakthrough happens when you realize the real leverage does not come from doing more, but from mastering this single counter-intuitive principle.",
                visual_prompt=f"High-detail cinematic visualization of insight, glowing energy or geometric structure representing {clean_topic}",
                on_screen_text="THE LEVERAGE",
                camera_motion="zoom_out",
                sound_effect="impact",
                estimated_duration=6.5
            ),
            ScriptScene(
                scene_number=4,
                narration=f"Once you align with this reality, the friction disappears and outcomes compound exponentially.",
                visual_prompt=f"Powerful triumphant cinematic visual representing mastery of {clean_topic}, golden hour rays, dramatic depth of field",
                on_screen_text="EXPONENTIAL GROWTH",
                camera_motion="zoom_in",
                sound_effect="riser",
                estimated_duration=5.5
            ),
            ScriptScene(
                scene_number=5,
                narration=f"Master this, and you will never see the world the same way again. Which is exactly why...",
                visual_prompt=f"Intense closing cinematic portrait or symbol for {clean_topic}, cinematic mist and focused spotlight",
                on_screen_text="REMEMBER THIS",
                camera_motion="zoom_in",
                sound_effect="deep_boom",
                estimated_duration=4.5
            ),
        ]

        full_narration = " ".join(s.narration for s in scenes)
        total_words = len(full_narration.split())
        total_duration = sum(s.estimated_duration for s in scenes)

        return RetentionScript(
            niche=niche,
            topic=clean_topic,
            title=target_title,
            format=format_type,
            scenes=scenes,
            full_narration=full_narration,
            total_words=total_words,
            estimated_duration_sec=total_duration,
            loop_engineered=True,
            policy_disclaimer="Educational and analytical content designed with original commentary."
        )

