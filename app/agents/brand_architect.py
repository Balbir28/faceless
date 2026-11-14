"""
BrandArchitect - Channel Name, Identity & Authority Branding Agent
Generates authoritative, brandable YouTube channel names, handles, channel bios,
and profile avatar prompts engineered for high subscriber conversion and YPP trust.
"""

from typing import Dict, List, Any
from pydantic import BaseModel


class ChannelBrand(BaseModel):
    niche_key: str
    primary_name: str
    alternate_names: List[str]
    suggested_handles: List[str]
    channel_tagline: str
    channel_about_bio: str
    profile_avatar_prompt: str
    banner_prompt: str


class BrandArchitect:
    def __init__(self):
        self.brand_vault = {
            "simulation_explainer": ChannelBrand(
                niche_key="simulation_explainer",
                primary_name="BioSim Studio",
                alternate_names=["Anatomy Vault", "HypoPhysics", "Survival Simulations", "The Human Sim"],
                suggested_handles=["@BioSimStudio", "@AnatomyVault", "@HypoPhysics"],
                channel_tagline="The brutal physics, anatomy, and survival science behind impossible scenarios.",
                channel_about_bio=(
                    "Welcome to BioSim Studio.\n\n"
                    "We break down the biomechanics, human anatomy, and survival science behind impossible feats, "
                    "bizarre hypothetical scenarios, and extreme physical challenges.\n\n"
                    "⚡ Daily 3D anatomical simulations and medical physics breakdowns.\n"
                    "📌 Educational scientific simulations and hypothetical analysis.\n\n"
                    "Business inquiries: contact.biosimstudio@gmail.com"
                ),
                profile_avatar_prompt="Sleek 3D anatomical human mannequin bust with glowing cyan ribcage and neural spine, dark studio backdrop, 8k Blender icon logo",
                banner_prompt="3D laboratory environment with transparent holographic human anatomical cross-sections, glowing medical HUD data streams, Zack D Films aesthetic"
            ),
            "dark_psychology": ChannelBrand(
                niche_key="dark_psychology",
                primary_name="Cognitive Vault",
                alternate_names=["The Shadow Protocol", "Mind Unmasked", "Subconscious Ledger", "Neuro Sovereignty"],
                suggested_handles=["@CognitiveVault", "@ShadowProtocol", "@MindUnmasked"],
                channel_tagline="Deconstructing human behavior, micro-expressions, and psychological leverage.",
                channel_about_bio=(
                    "Welcome to Cognitive Vault.\n\n"
                    "We explore behavioral psychology, cognitive biases, micro-expressions, and conversational dynamics. "
                    "Our mission is to help you decode deception, protect your mental autonomy, and understand the subtle forces governing human nature.\n\n"
                    "⚡ New strategic breakdowns published daily.\n"
                    "📌 Content created for educational and analytical purposes.\n\n"
                    "Business inquiries: contact.cognitivevault@gmail.com"
                ),
                profile_avatar_prompt="Minimalist geometric glowing human silhouette profile with glowing neural pathways, dark obsidian and gold accents, 8k luxury logo icon",
                banner_prompt="Sleek dark cinematic backdrop with subtle glowing neural mesh and typography reading 'DECODE HUMAN BEHAVIOR', high contrast dark slate and cyan rim light"
            ),
            "wealth_secrets": ChannelBrand(
                niche_key="wealth_secrets",
                primary_name="Capital Protocol",
                alternate_names=["Asset Sovereignty", "The 1% Playbook", "Wealth Architects", "Billionaire Leverage"],
                suggested_handles=["@CapitalProtocol", "@AssetSovereignty", "@TheOnePercentPlaybook"],
                channel_tagline="The unwritten financial rules of the ultra-wealthy.",
                channel_about_bio=(
                    "Welcome to Capital Protocol.\n\n"
                    "We dissect how the ultra-wealthy structure assets, leverage legal debt, and build multi-generational compounding wealth. "
                    "From private family offices to macro-economic secrets, we break down what they never taught you in business school.\n\n"
                    "⚡ Daily breakdowns on wealth creation and asset strategy.\n"
                    "📌 Educational analysis only, not financial advice.\n\n"
                    "Business inquiries: partner.capitalprotocol@gmail.com"
                ),
                profile_avatar_prompt="Luxury gold geometric crest emblem resembling an architectural vault and ascending pillar, obsidian background, matte finish",
                banner_prompt="Modern architectural concrete penthouse overlooking a world financial capital skyline at dusk, golden geometric grid overlay"
            ),
            "modern_stoicism": ChannelBrand(
                niche_key="modern_stoicism",
                primary_name="The Stoic Sovereign",
                alternate_names=["Aurelius Mind", "Iron Sovereignty", "Timeless Discipline", "Marcus Legacy"],
                suggested_handles=["@StoicSovereign", "@AureliusMind", "@IronSovereignty"],
                channel_tagline="Ancient Roman discipline applied to modern mental sovereignty.",
                channel_about_bio=(
                    "Welcome to The Stoic Sovereign.\n\n"
                    "Command your thoughts. Master your reactions. Become untouchable.\n"
                    "We translate timeless Stoic principles from Marcus Aurelius, Seneca, and Epictetus into actionable mental models for modern resilience, focus, and high performance.\n\n"
                    "⚡ Daily philosophical wisdom and mental toughness drills.\n"
                    "📌 Philosophy synthesized for modern daily life.\n\n"
                    "Business inquiries: thestoicsovereign@gmail.com"
                ),
                profile_avatar_prompt="Classical white marble bust of Roman Emperor Marcus Aurelius with dramatic side lighting and dark moody background, high resolution museum sculpture",
                banner_prompt="Storm over ancient Roman colosseum with dramatic lightning and single ray of golden sunlight cutting through clouds, cinematic 35mm"
            ),
            "future_tech": ChannelBrand(
                niche_key="future_tech",
                primary_name="Neural Frontier",
                alternate_names=["Autonomous Pulse", "The Singularity Shift", "Agentic Nexus", "Cyber Genesis"],
                suggested_handles=["@NeuralFrontier", "@AutonomousPulse", "@SingularityShift"],
                channel_tagline="Mapping the exponential age of AI agents, robotics, and synthetic intelligence.",
                channel_about_bio=(
                    "Welcome to Neural Frontier.\n\n"
                    "Technology is moving at warp speed. We track autonomous AI agents, enterprise automation, robotics, and the economic disruption reshaping humanity. "
                    "Stay ahead of the curve before the world changes permanently.\n\n"
                    "⚡ Daily updates on breakthrough AI models and tech leverage.\n"
                    "📌 In-depth technological research and analysis.\n\n"
                    "Business inquiries: tech.neuralfrontier@gmail.com"
                ),
                profile_avatar_prompt="Cybernetic glowing sphere with quantum core and pulsing blue-violet fiber lines, hyper-futuristic tech studio emblem",
                banner_prompt="Futuristic holographic cityscape at dusk with floating data streams and glowing autonomous drone paths, cyberpunk cinematic"
            ),
            "unsolved_mysteries": ChannelBrand(
                niche_key="unsolved_mysteries",
                primary_name="Cosmic Paradox",
                alternate_names=["The Silent Frequency", "Chronos Vault", "Deep Anomaly", "Unseen Archive"],
                suggested_handles=["@CosmicParadox", "@SilentFrequency", "@ChronosVault"],
                channel_tagline="Uncovering the bizarre events, cosmic signals, and anomalies science cannot explain.",
                channel_about_bio=(
                    "Welcome to Cosmic Paradox.\n\n"
                    "There are occurrences in our universe that defy explanation. "
                    "From deep space radio transmissions and ocean anomalies to historical paradoxes, we investigate the unexplained events that keep astronomers and scientists awake at night.\n\n"
                    "⚡ Daily mystery deep dives and cosmic anomalies.\n"
                    "📌 Documented scientific history and verified anomalies.\n\n"
                    "Business inquiries: cosmicparadox.media@gmail.com"
                ),
                profile_avatar_prompt="Deep cosmic nebula in dark violet and crimson with an ominous radio signal telescope silhouette in foreground, mysterious badge",
                banner_prompt="Massive radio telescope array under the Milky Way galaxy in pitch black desert night with glowing frequency wave, eerie scientific atmosphere"
            ),
        }

    def get_brand(self, niche_key: str) -> ChannelBrand:
        if niche_key in self.brand_vault:
            return self.brand_vault[niche_key]
        # Default brand synthesis
        clean_name = niche_key.replace("_", " ").title()
        return ChannelBrand(
            niche_key=niche_key,
            primary_name=f"{clean_name} Insights",
            alternate_names=[f"{clean_name} Hub", f"The {clean_name} Vault", f"{clean_name} Daily"],
            suggested_handles=[f"@{clean_name.replace(' ', '')}Hub", f"@{clean_name.replace(' ', '')}Vault"],
            channel_tagline=f"Daily high-leverage strategic breakdowns on {clean_name}.",
            channel_about_bio=f"Welcome to the official channel for {clean_name}. We provide daily insights and transformative analysis.",
            profile_avatar_prompt=f"Minimalist luxury brand logo for {clean_name}, dark moody background with vibrant golden accent",
            banner_prompt=f"Cinematic wide banner for {clean_name} channel, sleek and authoritative"
        )

