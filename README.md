# 🧘‍♀️ Wellness Agent - AI-Powered Holistic Health Assistant

[![Deploy to Render](https://img.shields.io/badge/Deploy%20to-Render-46E3B7.svg)](https://render.com)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive AI-powered wellness agent that provides personalized health advice, emotional support, and wellness predictions using advanced machine learning and natural language processing.

## 🌟 Features

### 🧠 **AI-Powered Wellness Advice**
- Personalized health recommendations
- Emotional support and mindfulness guidance
- Stress management techniques
- Holistic wellness approach

### 📊 **ML-Based Predictions**
- Burnout risk assessment
- Financial wellness scoring
- Work-life balance analysis
- Emotional wellness indexing

### 💭 **Mood & Stress Tracking**
- 1-10 mood scale monitoring
- 0-6 stress level tracking
- Trigger-based interventions
- Personalized coping strategies

### 🎯 **Smart Interventions**
- Automatic concern detection
- Proactive wellness nudges
- Emergency support protocols
- Adaptive response system

### 📚 **Multi-Domain Knowledge**
- Wellness and health guidance
- Educational content delivery
- Ancient spiritual wisdom (Vedas)
- Evidence-based recommendations

## 🚀 Quick Start

### Option 1: Deploy to Render (Recommended)

1. **Fork this repository**
2. **Get API Keys**:
   - [Google Gemini API Key](https://makersuite.google.com/app/apikey) (Required)
   - [OpenAI API Key](https://platform.openai.com/api-keys) (Optional)

3. **Deploy to Render**:
   [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

4. **Set Environment Variables** in Render:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ENVIRONMENT=production
   PORT=8000
   ```

### Option 2: Local Development

```bash
# Clone the repository
git clone https://github.com/tensorwhiz141/new.git
cd new

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Run the application
python app/start_wellness_api.py
```

## 📡 API Endpoints

### 🏥 **Wellness Endpoints**
```http
POST /ask-wellness
Content-Type: application/json

{
  "query": "How can I manage stress better?",
  "user_id": "user123",
  "mood_score": 6,
  "stress_level": 4
}
```

### 🎓 **Educational Endpoints**
```http
POST /ask-edumentor
Content-Type: application/json

{
  "query": "Explain mindfulness meditation",
  "user_id": "user123"
}
```

### 🕉️ **Spiritual Wisdom**
```http
POST /ask-vedas
Content-Type: application/json

{
  "query": "What do the Vedas say about inner peace?",
  "user_id": "user123"
}
```

### 🔍 **Monitoring**
```http
GET /health          # Health check
GET /docs            # Interactive API documentation
GET /system-status   # Comprehensive system status
```

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Wellness API   │    │   ML Prediction │
│   (Any Client)  │◄──►│   (FastAPI)      │◄──►│   Engine        │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   Vector Stores  │
                       │   (Knowledge)    │
                       └──────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   LLM Services   │
                       │ (Gemini/OpenAI)  │
                       └──────────────────┘
```

## 🛠️ Technology Stack

- **Backend**: FastAPI, Python 3.11+
- **AI/ML**: LangChain, Transformers, Prophet, Scikit-learn
- **Vector DB**: FAISS
- **LLM APIs**: Google Gemini, OpenAI, Groq
- **Deployment**: Render, Docker
- **Monitoring**: Structured logging, Health checks

## 📊 Wellness Metrics Tracked

| Metric | Range | Description |
|--------|-------|-------------|
| **Mood Score** | 1-10 | Overall emotional state |
| **Stress Level** | 0-6 | Current stress intensity |
| **Burnout Risk** | 0-1 | Probability of burnout |
| **Financial Health** | 0-100 | Financial wellness score |
| **Work-Life Balance** | 0-100 | Balance assessment |
| **Emotional Wellness** | 0-100 | Emotional health index |

## 🔧 Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GEMINI_API_KEY` | ✅ | Primary Google Gemini API key |
| `GEMINI_API_KEY_BACKUP` | ❌ | Backup Gemini API key |
| `OPENAI_API_KEY` | ❌ | OpenAI API key for enhanced features |
| `GROQ_API_KEY` | ❌ | Groq API key for alternative LLM |
| `ENVIRONMENT` | ✅ | Set to `production` for deployment |
| `PORT` | ✅ | Server port (auto-set by Render) |

### Wellness Trigger Thresholds

```python
TRIGGER_THRESHOLDS = {
    'wellness_concern': 0.7,      # Stress level threshold
    'educational_struggle': 0.6,   # Learning difficulty threshold
    'mood_low': 3.0,              # Low mood threshold
    'burnout_risk': 0.8           # High burnout risk threshold
}
```

## 🧪 Testing

```bash
# Run health check
curl https://your-app.onrender.com/health

# Test wellness endpoint
curl -X POST https://your-app.onrender.com/wellness \
  -H "Content-Type: application/json" \
  -d '{"query": "I feel stressed", "mood_score": 4, "stress_level": 5}'

# View API documentation
open https://your-app.onrender.com/docs
```

## 📈 Monitoring & Analytics

- **Health Monitoring**: `/health` endpoint for uptime checks
- **Performance Metrics**: Response time and success rate tracking
- **User Analytics**: Anonymized usage patterns and wellness trends
- **Error Tracking**: Comprehensive logging and error reporting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [API Docs](https://your-app.onrender.com/docs)
- **Issues**: [GitHub Issues](https://github.com/tensorwhiz141/new/issues)
- **Discussions**: [GitHub Discussions](https://github.com/tensorwhiz141/new/discussions)

## 🙏 Acknowledgments

- **Ancient Wisdom**: Vedic texts and spiritual teachings
- **Modern Science**: Evidence-based wellness research
- **Open Source**: LangChain, FastAPI, and the Python community
- **AI Providers**: Google Gemini, OpenAI for powering the intelligence

---

**🌟 Star this repository if you find it helpful!**

**💬 Have questions? Open an issue or start a discussion!**

**🚀 Ready to deploy? Click the Render button above!**
