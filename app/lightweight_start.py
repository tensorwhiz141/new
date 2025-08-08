#!/usr/bin/env python3
"""
Lightweight Startup Script for Wellness Agent
Optimized for Render's 512MB memory limit
"""

import os
import sys
from pathlib import Path

def create_minimal_api():
    """Create a minimal wellness API that works within memory constraints"""
    
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    from typing import Optional
    import uuid
    from datetime import datetime
    
    app = FastAPI(
        title="Wellness Agent API",
        description="AI-powered wellness advice and support",
        version="1.0.0"
    )
    
    # Request models
    class WellnessRequest(BaseModel):
        query: str
        user_id: Optional[str] = "anonymous"
        mood_score: Optional[float] = None
        stress_level: Optional[float] = None
    
    class SimpleResponse(BaseModel):
        query_id: str
        query: str
        response: str
        timestamp: str
        endpoint: str
    
    # Simple wellness responses (no heavy AI models)
    def get_wellness_response(query: str, mood_score: Optional[float] = None, stress_level: Optional[float] = None) -> str:
        """Generate wellness response using simple rules"""
        
        query_lower = query.lower()
        
        # Stress-related queries
        if any(word in query_lower for word in ['stress', 'anxious', 'worried', 'overwhelmed']):
            return """Here are some effective stress management techniques:
            
🧘 **Immediate Relief:**
- Take 5 deep breaths (4 seconds in, 6 seconds out)
- Try the 5-4-3-2-1 grounding technique
- Do a quick 2-minute meditation

💪 **Daily Practices:**
- Regular exercise (even 10 minutes helps)
- Maintain a consistent sleep schedule
- Practice mindfulness or meditation
- Connect with supportive friends/family

🌱 **Long-term Wellness:**
- Set realistic goals and boundaries
- Learn to say "no" when overwhelmed
- Consider talking to a counselor
- Focus on what you can control

Remember: It's okay to ask for help when you need it."""
        
        # Sleep-related queries
        elif any(word in query_lower for word in ['sleep', 'tired', 'insomnia', 'rest']):
            return """Here's how to improve your sleep quality:
            
🌙 **Sleep Hygiene:**
- Keep a consistent sleep schedule
- Create a relaxing bedtime routine
- Keep your bedroom cool, dark, and quiet
- Avoid screens 1 hour before bed

☕ **What to Avoid:**
- Caffeine after 2 PM
- Large meals close to bedtime
- Alcohol (disrupts sleep quality)
- Intense exercise 3 hours before sleep

✨ **Natural Sleep Aids:**
- Try chamomile tea or magnesium
- Practice progressive muscle relaxation
- Use white noise or earplugs
- Consider meditation apps

Quality sleep is essential for mental and physical health!"""
        
        # Exercise/fitness queries
        elif any(word in query_lower for word in ['exercise', 'fitness', 'workout', 'active']):
            return """Here's how to build a sustainable fitness routine:
            
🏃 **Getting Started:**
- Start with 10-15 minutes daily
- Choose activities you enjoy
- Set realistic, achievable goals
- Focus on consistency over intensity

💪 **Simple Exercises:**
- Walking (easiest to start)
- Bodyweight exercises (push-ups, squats)
- Yoga or stretching
- Dancing or swimming

🎯 **Staying Motivated:**
- Track your progress
- Find a workout buddy
- Celebrate small wins
- Mix up your routine to avoid boredom

Remember: Any movement is better than none!"""
        
        # Mental health queries
        elif any(word in query_lower for word in ['depression', 'sad', 'lonely', 'mental health']):
            return """Supporting your mental health is crucial:
            
🧠 **Daily Mental Health:**
- Practice gratitude (write 3 things daily)
- Stay connected with loved ones
- Engage in activities you enjoy
- Maintain a routine

🌟 **Professional Support:**
- Consider therapy or counseling
- Talk to your doctor about mental health
- Join support groups
- Use mental health apps

🚨 **When to Seek Help:**
- Persistent sadness or hopelessness
- Loss of interest in activities
- Significant changes in sleep/appetite
- Thoughts of self-harm

You're not alone - help is available and recovery is possible."""
        
        # Nutrition queries
        elif any(word in query_lower for word in ['nutrition', 'diet', 'eating', 'food', 'healthy']):
            return """Here's guidance for healthy nutrition:
            
🥗 **Balanced Eating:**
- Include fruits and vegetables in every meal
- Choose whole grains over processed foods
- Include lean proteins (fish, chicken, beans)
- Stay hydrated (8 glasses of water daily)

🍎 **Simple Healthy Swaps:**
- Water instead of sugary drinks
- Nuts instead of chips
- Whole grain bread instead of white
- Baked instead of fried foods

⚖️ **Mindful Eating:**
- Eat slowly and without distractions
- Listen to hunger and fullness cues
- Plan meals ahead when possible
- Allow yourself occasional treats

Remember: Small, consistent changes lead to lasting results!"""
        
        # Default wellness response
        else:
            return f"""Thank you for your wellness question: "{query}"
            
🌟 **General Wellness Tips:**
- Prioritize sleep (7-9 hours nightly)
- Stay physically active daily
- Eat nutritious, balanced meals
- Practice stress management
- Maintain social connections
- Take time for activities you enjoy

💡 **Remember:**
- Small daily habits create big changes
- Progress isn't always linear
- Self-care isn't selfish
- You're worth investing in

For specific concerns, consider consulting with healthcare professionals. Your wellness journey is unique to you!"""
    
    @app.get("/health")
    async def health_check():
        """Health check endpoint"""
        return {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0",
            "service": "wellness-agent-lightweight"
        }
    
    @app.get("/")
    async def root():
        """Root endpoint"""
        return {
            "message": "Wellness Agent API - Lightweight Version",
            "description": "AI-powered wellness advice and support",
            "version": "1.0.0",
            "endpoints": {
                "health": "GET /health",
                "wellness": "POST /wellness",
                "docs": "GET /docs"
            }
        }
    
    @app.post("/wellness")
    async def wellness_advice(request: WellnessRequest):
        """Get wellness advice"""
        try:
            response_text = get_wellness_response(
                request.query, 
                request.mood_score, 
                request.stress_level
            )
            
            return SimpleResponse(
                query_id=str(uuid.uuid4()),
                query=request.query,
                response=response_text,
                timestamp=datetime.now().isoformat(),
                endpoint="wellness"
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    @app.post("/ask-wellness")
    async def comprehensive_wellness(request: WellnessRequest):
        """Comprehensive wellness advice (same as /wellness for lightweight version)"""
        return await wellness_advice(request)
    
    return app

def start_lightweight_api():
    """Start the lightweight wellness API"""
    
    # Get port from environment
    port = int(os.getenv("PORT", 8000))
    host = "0.0.0.0"
    
    print("=" * 60)
    print("  WELLNESS AGENT - LIGHTWEIGHT VERSION")
    print("=" * 60)
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Environment: {os.getenv('ENVIRONMENT', 'production')}")
    print("Memory optimized for Render's 512MB limit")
    print("=" * 60)
    
    try:
        import uvicorn
        
        # Create the lightweight app
        app = create_minimal_api()
        
        print("[INFO] Starting lightweight wellness API...")
        print("[INFO] No heavy AI models - using rule-based responses")
        print(f"[INFO] Server starting on {host}:{port}")
        
        # Start the server
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
    start_lightweight_api()
