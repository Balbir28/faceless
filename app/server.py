"""
FastAPI Server & REST Backend for ApexTube Guru Studio
Serves the web dashboard, real-time agent APIs, and media streaming endpoints.
"""

from pathlib import Path
from typing import Optional, List, Dict, Any
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.config import NICHES, VOICES, OUTPUT_DIR, TEMP_DIR, DEFAULT_VOICE
from app.agents.orchestrator import MasterOrchestrator
from app.agents.guru_strategist import GuruStrategist
from app.agents.retention_writer import RetentionWriter
from app.agents.policy_guardian import PolicyGuardian
from app.agents.brand_architect import BrandArchitect

app = FastAPI(title="ApexTube Studio - YouTube Monetization Guru Agent", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files if directory exists
static_path = Path(__file__).parent / "web" / "static"
if static_path.exists():
    app.mount("/static", StaticFiles(directory=str(static_path)), name="static")

orchestrator = MasterOrchestrator()
strategist = GuruStrategist()
writer = RetentionWriter()
guardian = PolicyGuardian()
brand_architect = BrandArchitect()


class StrategyRequest(BaseModel):
    niche: str
    custom_topic: Optional[str] = None


class ScriptRequest(BaseModel):
    niche: str
    topic: str
    title: str
    format: str = "shorts"


class AuditRequest(BaseModel):
    title: str
    script_text: str
    niche: str


class ProduceRequest(BaseModel):
    niche: str = "curious_leverage"
    topic: Optional[str] = None
    voice_id: str = DEFAULT_VOICE
    format: str = "shorts"
    music_mood: Optional[str] = None
    speed_adjustment: str = "+4%"


@app.get("/", response_class=HTMLResponse)
async def serve_dashboard():
    template_path = Path(__file__).parent / "web" / "templates" / "index.html"
    if template_path.exists():
        return template_path.read_text(encoding="utf-8")
    return "<h1>ApexTube Studio</h1><p>Dashboard template loading...</p>"


@app.get("/api/niches")
async def get_niches():
    return NICHES


@app.get("/api/voices")
async def get_voices():
    return VOICES


@app.get("/api/brand/{niche}")
async def get_brand(niche: str):
    brand = brand_architect.get_brand(niche)
    return brand.model_dump()


@app.post("/api/strategy")
async def generate_strategy(req: StrategyRequest):
    strat = strategist.formulate_strategy(niche_key=req.niche, custom_topic=req.custom_topic)
    return strat.model_dump()


@app.post("/api/script")
async def generate_script(req: ScriptRequest):
    scr = writer.generate_script(
        niche=req.niche,
        topic=req.topic,
        title=req.title,
        format_type=req.format
    )
    return scr.model_dump()


@app.post("/api/audit")
async def run_audit(req: AuditRequest):
    report = guardian.audit_script(
        title=req.title,
        script_text=req.script_text,
        niche=req.niche
    )
    return report.model_dump()


@app.post("/api/produce")
async def produce_video(req: ProduceRequest):
    try:
        package = orchestrator.run_pipeline(
            niche=req.niche,
            topic=req.topic,
            voice_id=req.voice_id,
            format_type=req.format,
            music_mood=req.music_mood,
            speed_adjustment=req.speed_adjustment
        )
        # Convert internal paths to web accessible URLs
        res = package.model_dump()
        res["video_url"] = f"/media/{Path(package.video_path).name}"
        res["thumbnail_url"] = f"/media/{Path(package.thumbnail_path).name}"
        return res
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


class PublishRequest(BaseModel):
    session_id: str


@app.post("/api/publish")
async def trigger_publish(req: PublishRequest):
    """
    Executes automated 100% free YouTube upload using Google's official free quota API.
    """
    import subprocess
    upload_script = OUTPUT_DIR / f"{req.session_id}_publish_to_youtube.py"
    if not upload_script.exists():
        raise HTTPException(status_code=404, detail="Publish script not found for this video")

    client_secret = Path(__file__).parent.parent / "client_secret.json"
    if not client_secret.exists():
        return {
            "success": False,
            "mode": "manual_or_credentials_needed",
            "message": (
                "client_secret.json not found. You have two 100% FREE publishing options:\n"
                "1. Manual Free Upload: Click 'Open YouTube Studio' and upload with 1-click copied metadata.\n"
                "2. Automated Free API: Download free client_secret.json from Google Cloud (free quota: 10,000 units/day)."
            ),
            "studio_url": "https://studio.youtube.com/channel/UC/videos/upload?d=pt"
        }

    try:
        proc = subprocess.run(
            ["python3", str(upload_script)],
            capture_output=True,
            text=True,
            timeout=120
        )
        if proc.returncode == 0:
            return {"success": True, "message": "Video successfully uploaded to YouTube for FREE!", "output": proc.stdout}
        else:
            return {"success": False, "error": proc.stderr}
    except Exception as e:
        return {"success": False, "error": str(e)}


@app.get("/api/gallery")
async def get_gallery():
    videos = []
    for f in sorted(OUTPUT_DIR.glob("*_video.mp4"), key=lambda x: x.stat().st_mtime, reverse=True):
        session_id = f.name.replace("_video.mp4", "")
        thumb = OUTPUT_DIR / f"{session_id}_thumbnail.jpg"
        seo = OUTPUT_DIR / f"{session_id}_seo.json"
        title = session_id
        if seo.exists():
            try:
                import json
                meta = json.loads(seo.read_text())
                title = meta.get("title", session_id)
            except Exception:
                pass

        videos.append({
            "session_id": session_id,
            "title": title,
            "video_url": f"/media/{f.name}",
            "thumbnail_url": f"/media/{thumb.name}" if thumb.exists() else None,
            "bundle_url": f"/api/package/{session_id}",
            "created_at": f.stat().st_mtime,
            "file_size_mb": round(f.stat().st_size / (1024 * 1024), 2)
        })
    return videos


@app.get("/api/package/{session_id}")
async def download_bundle(session_id: str):
    """
    Exports complete production bundle (MP4, Thumbnail, Posting Guide TXT, SEO JSON)
    in a single 1-click ZIP file.
    """
    import zipfile
    video = OUTPUT_DIR / f"{session_id}_video.mp4"
    if not video.exists():
        raise HTTPException(status_code=404, detail="Video not found")

    zip_path = TEMP_DIR / f"{session_id}_package.zip"
    thumb = OUTPUT_DIR / f"{session_id}_thumbnail.jpg"
    seo = OUTPUT_DIR / f"{session_id}_seo.json"
    cross = OUTPUT_DIR / f"{session_id}_cross_platform.json"

    # Human-readable posting guide
    guide_lines = [f"=== APEXTUBE PRODUCTION PACKAGE: {session_id} ===", ""]
    if seo.exists():
        try:
            import json
            meta = json.loads(seo.read_text())
            guide_lines.append(f"📌 YOUTUBE SHORTS TITLE:\n{meta.get('title')}\n")
            guide_lines.append(f"📝 YOUTUBE DESCRIPTION:\n{meta.get('description')}\n")
            guide_lines.append(f"🏷️ YOUTUBE TAGS:\n{', '.join(meta.get('tags', []))}\n")
        except Exception:
            pass

    if cross.exists():
        try:
            import json
            cmeta = json.loads(cross.read_text())
            guide_lines.append(f"📸 INSTAGRAM REELS CAPTION:\n{cmeta.get('instagram_reels', {}).get('caption')}\n")
            guide_lines.append(f"🎵 TIKTOK CAPTION:\n{cmeta.get('tiktok', {}).get('caption')}\n")
        except Exception:
            pass

    guide_path = TEMP_DIR / f"{session_id}_POSTING_GUIDE.txt"
    guide_path.write_text("\n".join(guide_lines), encoding="utf-8")

    with zipfile.ZipFile(zip_path, "w") as z:
        z.write(video, arcname="video_1080x1920.mp4")
        if thumb.exists():
            z.write(thumb, arcname="thumbnail.jpg")
        z.write(guide_path, arcname="POSTING_GUIDE.txt")
        if seo.exists():
            z.write(seo, arcname="youtube_seo.json")
        if cross.exists():
            z.write(cross, arcname="cross_platform.json")

    return FileResponse(
        path=str(zip_path),
        filename=f"{session_id}_complete_package.zip",
        media_type="application/zip"
    )


@app.get("/api/analytics")
async def get_analytics():
    videos = list(OUTPUT_DIR.glob("*_video.mp4"))
    total_count = len(videos)
    niches_seen = set()
    for v in videos:
        for k in NICHES.keys():
            if k in v.name:
                niches_seen.add(k)
    return {
        "total_videos": total_count,
        "niches_active": len(niches_seen),
        "target_avg_cpm": "$15.40",
        "human_hours_saved": round(total_count * 3.5, 1),
        "freelancer_cost_saved": f"${total_count * 85}",
        "projected_revenue": {
            "at_100k": "$1,200 - $2,200",
            "at_500k": "$6,000 - $11,000",
            "at_1m": "$12,000 - $22,000"
        }
    }


@app.get("/media/{filename}")
async def get_media(filename: str):
    # Check in OUTPUT_DIR first
    target = OUTPUT_DIR / filename
    if not target.exists():
        target = TEMP_DIR / filename
    if not target.exists():
        raise HTTPException(status_code=404, detail="Media file not found")

    mime = "video/mp4"
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        mime = "image/jpeg"
    elif filename.endswith(".png"):
        mime = "image/png"
    elif filename.endswith(".mp3"):
        mime = "audio/mpeg"
    elif filename.endswith(".json"):
        mime = "application/json"

    return FileResponse(path=str(target), media_type=mime)

