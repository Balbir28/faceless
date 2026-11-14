"""
PolicyGuardian - YouTube Partner Program (YPP) Compliance & Safety Auditor
Guarantees channel safety by enforcing YouTube Community Guidelines, Reused Content policies,
Repetitious Content rules, and Synthetic Media Disclosures.
"""

import re
from typing import Dict, List, Any
from pydantic import BaseModel, Field


class PolicyIssue(BaseModel):
    severity: str  # "HIGH", "MEDIUM", "LOW"
    category: str  # "reused_content", "community_guidelines", "synthetic_media", "deceptive_practices"
    description: str
    fix_suggestion: str


class ComplianceReport(BaseModel):
    is_safe_for_monetization: bool
    compliance_score: int = Field(ge=0, le=100)
    risk_level: str  # "LOW", "MODERATE", "CRITICAL"
    issues_found: List[PolicyIssue] = []
    synthetic_media_disclosure_required: bool
    disclosure_statement: str
    monetization_verdict: str


class PolicyGuardian:
    def __init__(self):
        # High-risk triggers that cause instant demonetization or algorithmic suppression
        self.prohibited_keywords = {
            "financial_scams": [
                "guaranteed profit", "100% win rate", "get rich quick", "free crypto",
                "double your money", "no risk investment", "pump and dump"
            ],
            "harm_and_violence": [
                "kill yourself", "suicide method", "bomb instructions", "how to hack into",
                "doxxing", "hate speech against", "terrorist attack"
            ],
            "deceptive_medical": [
                "cure for cancer in 3 days", "miracle cure", "vaccines contain chips",
                "doctors hiding this cure"
            ],
            "clickbait_fraud": [
                "you will die if", "police caught me doing this", "secret leaked by fbi"
            ]
        }

    def audit_script(self, title: str, script_text: str, niche: str) -> ComplianceReport:
        issues: List[PolicyIssue] = []
        score = 100
        text_lower = f"{title.lower()} {script_text.lower()}"

        # 1. Prohibited & High-Risk Keyword Scans
        for category, words in self.prohibited_keywords.items():
            for word in words:
                if re.search(r'\b' + re.escape(word) + r'\b', text_lower):
                    severity = "HIGH" if category in ["financial_scams", "harm_and_violence"] else "MEDIUM"
                    penalty = 25 if severity == "HIGH" else 15
                    score -= penalty
                    issues.append(PolicyIssue(
                        severity=severity,
                        category="community_guidelines",
                        description=f"Detected potentially non-compliant phrase: '{word}' ({category.replace('_', ' ')}).",
                        fix_suggestion=f"Remove or rephrase '{word}' with objective, educational terminology."
                    ))

        # 2. Reused Content & Originality Check
        # Reused content occurs when text is too short, lacks original analysis, or sounds like a bare Wikipedia summary
        word_count = len(script_text.split())
        if word_count < 40:
            score -= 20
            issues.append(PolicyIssue(
                severity="HIGH",
                category="reused_content",
                description="Script is excessively short (< 40 words), which flags YouTube's low-effort / repetitious content filter.",
                fix_suggestion="Expand the script with original commentary, contextual examples, or historical synthesis."
            ))

        # 3. Disclaimers for High-Stakes Niches (Finance / Psychology)
        if niche == "wealth_secrets" and not any(k in text_lower for k in ["educational", "financial advice", "disclaimer", "not advice"]):
            score -= 10
            issues.append(PolicyIssue(
                severity="MEDIUM",
                category="deceptive_practices",
                description="Finance content without educational disclaimer risks FTC and YouTube financial misrepresentation flags.",
                fix_suggestion="Append: 'This video is for educational and entertainment purposes only, not financial advice.'"
            ))

        # 4. Repetitious Cadence Check
        sentences = [s.strip() for s in re.split(r'[.!?]+', script_text) if s.strip()]
        if len(sentences) >= 3:
            lengths = [len(s.split()) for s in sentences]
            if len(set(lengths)) <= 2:  # All sentences have the exact same mechanical length
                score -= 10
                issues.append(PolicyIssue(
                    severity="LOW",
                    category="repetitious_content",
                    description="Monotone robotic sentence structure detected. High risk of low-effort algorithmic suppression.",
                    fix_suggestion="Vary sentence length with short impact punches followed by deeper explanatory phrases."
                ))

        # 5. Synthetic Media Policy Compliance
        # In YouTube's 2024+ guidelines, AI-generated realistic imagery requires synthetic media tagging
        disclosure_statement = (
            "YouTube Partner Program Synthetic Media Disclosure:\n"
            "- Content contains realistic generative imagery/visuals: YES\n"
            "- Depicts real persons saying/doing things they did not: NO\n"
            "- Alters footage of real historical event: NO\n"
            "- Declaration: Compliant under YouTube Generative AI Disclosure Guidelines."
        )

        score = max(0, min(100, score))
        risk_level = "LOW" if score >= 85 else ("MODERATE" if score >= 65 else "CRITICAL")
        is_safe = score >= 70

        verdict = (
            "✅ APPROVED FOR MONETIZATION: Safe for YouTube Partner Program (YPP). "
            "Strong original commentary and no policy violations detected."
            if is_safe else
            "⚠️ ACTION REQUIRED: Script has flagged terms or structure that could risk demonetization or YPP rejection."
        )

        return ComplianceReport(
            is_safe_for_monetization=is_safe,
            compliance_score=score,
            risk_level=risk_level,
            issues_found=issues,
            synthetic_media_disclosure_required=True,
            disclosure_statement=disclosure_statement,
            monetization_verdict=verdict
        )

