#!/usr/bin/env python3
"""
Production Startup Script for Wellness Agent
Simplified startup for Render deployment - no .env file checks
"""

import os
import sys
from pathlib import Path

def start_wellness_api():
    """Start the wellness API in production mode"""
    
    # Get port from environment (Render sets this)
    port = int(os.getenv("PORT", 8000))
    host = "0.0.0.0"
    
    print("=" * 60)
    print("  WELLNESS AGENT PRODUCTION STARTUP")
    print("=" * 60)
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Environment: {os.getenv('ENVIRONMENT', 'production')}")
    
    # Check for API keys
    gemini_key = os.getenv("GEMINI_API_KEY")
    groq_key = os.getenv("GROQ_API_KEY")
    
    if gemini_key:
        print("[OK] Gemini API key configured")
    if groq_key:
        print("[OK] Groq API key configured")
    
    if not gemini_key and not groq_key:
        print("[WARNING] No API keys found - using fallback mode")
    
    print("=" * 60)
    
    try:
        # Import uvicorn
        import uvicorn
        
        # Try to import and start the main orchestration API
        try:
            print("[INFO] Starting full orchestration system...")
            from orchestration_api import app
            print("[OK] Full orchestration API loaded")
        except ImportError as e:
            print(f"[INFO] Full API not available ({e}), using simple API...")
            from simple_api import app
            print("[OK] Simple API loaded")
        
        # Start the server
        print(f"[INFO] Starting server on {host}:{port}")
        uvicorn.run(
            app, 
            host=host, 
            port=port, 
            log_level="info",
            access_log=True
        )
        
    except Exception as e:
        print(f"[ERROR] Failed to start server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_wellness_api()
