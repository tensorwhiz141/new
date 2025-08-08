#!/usr/bin/env python3
"""
Wellness API Startup Script
Starts the unified orchestration system with wellness capabilities
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def check_requirements():
    """Check if required packages are installed"""
    try:
        import fastapi
        import uvicorn
        import google.generativeai
        print("✓ Required packages found")
        return True
    except ImportError as e:
        print(f"✗ Missing required package: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def check_env_file():
    """Check if .env file exists and has required keys"""
    env_path = Path(".env")
    if not env_path.exists():
        print("✗ .env file not found")
        print("Creating sample .env file...")
        with open(".env", "w") as f:
            f.write("# Gemini API Keys\n")
            f.write("GEMINI_API_KEY=your_primary_key_here\n")
            f.write("GEMINI_API_KEY_BACKUP=your_backup_key_here\n")
            f.write("\n# Sub-agent URLs (optional)\n")
            f.write("EMOTIONAL_WELLNESS_BOT_URL=http://localhost:8002\n")
            f.write("FINANCIAL_WELLNESS_BOT_URL=http://localhost:8003\n")
            f.write("TUTORBOT_URL=http://localhost:8001\n")
            f.write("QUIZBOT_URL=http://localhost:8004\n")
        print("✓ Created .env file. Please add your Gemini API keys.")
        return False
    
    # Check if API keys are set
    from dotenv import load_dotenv
    load_dotenv()
    
    primary_key = os.getenv("GEMINI_API_KEY")
    backup_key = os.getenv("GEMINI_API_KEY_BACKUP")
    
    if not primary_key or primary_key == "your_primary_key_here":
        print("✗ GEMINI_API_KEY not set in .env file")
        return False
    
    print("✓ Environment configuration found")
    return True

def start_api_server():
    """Start the API server with production configuration"""
    # Get port from environment (Render sets this)
    port = int(os.getenv("PORT", 8000))
    host = "0.0.0.0"  # Required for Render

    print("\n" + "="*60)
    print("  STARTING WELLNESS API SERVER")
    print("="*60)
    print(f"Server will be available at: http://{host}:{port}")
    print(f"API Documentation: http://{host}:{port}/docs")
    print("\nEndpoints:")
    print("  POST /ask-wellness - Wellness advice with emotional support")
    print("  POST /wellness - Simple wellness advice")
    print("  POST /ask-vedas - Spiritual wisdom")
    print("  POST /edumentor - Educational content")
    print("  GET /health - Health check")
    print("="*60)

    try:
        # Import uvicorn for production server
        import uvicorn

        # Try to start the full orchestration API first
        if Path("orchestration_api.py").exists():
            print("Starting full orchestration system...")
            # Import the FastAPI app
            from orchestration_api import app
            uvicorn.run(app, host=host, port=port, log_level="info")
        else:
            print("Starting simple API...")
            # Import the simple API app
            from simple_api import app
            uvicorn.run(app, host=host, port=port, log_level="info")

    except KeyboardInterrupt:
        print("\n\nServer stopped by user")
    except Exception as e:
        print(f"\n✗ Error starting server: {e}")
        print("Trying simple API as fallback...")
        try:
            from simple_api import app
            uvicorn.run(app, host=host, port=port, log_level="info")
        except Exception as fallback_error:
            print(f"✗ Fallback also failed: {fallback_error}")
            raise

def main():
    """Main startup function"""
    print("Wellness API Startup Script")
    print("=" * 30)

    # Change to the script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    # Check requirements
    if not check_requirements():
        return

    # For production (Render), skip .env file check as env vars are set directly
    environment = os.getenv("ENVIRONMENT", "development")
    if environment == "production":
        print("✓ Running in production mode")
        # Check for required environment variables
        required_vars = ["GEMINI_API_KEY"]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            print(f"✗ Missing required environment variables: {missing_vars}")
            return
    else:
        # Check environment file for development
        if not check_env_file():
            print("\nPlease configure your .env file with valid API keys and run again.")
            return

    # Start the API
    start_api_server()

if __name__ == "__main__":
    main()
