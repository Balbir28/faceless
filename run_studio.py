#!/usr/bin/env python3
"""
ApexTube Studio Runner
Starts the local web server and launches the interactive YouTube Monetization Studio UI.
"""

import sys
import socket
import uvicorn
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent))


def find_available_port(start_port: int = 8000) -> int:
    port = start_port
    while port < 8100:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
            port += 1
    return 8000


if __name__ == "__main__":
    port = find_available_port(8000)
    print("\n" + "="*60)
    print("🚀 ApexTube Studio - Autonomous YouTube Monetization Guru")
    print(f"🌐 Dashboard URL: http://localhost:{port}")
    print("="*60 + "\n")
    uvicorn.run("app.server:app", host="0.0.0.0", port=port, reload=False)

