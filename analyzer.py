import os
from dotenv import load_dotenv
from google import genai
from utils import clean_json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_competitor(name, data):
    prompt = f"""
You are a senior competitive intelligence analyst.

Analyze competitor: {name}

Data:
{data}

Return STRICT JSON:

{{
  "features": [...],
  "messaging": "...",
  "target_audience": "...",
  "strengths": [...],
  "weaknesses": [...],
  "customer_sentiment": {{
      "likes": [...],
      "complaints": [...]
  }},
  "pricing_insights": [...],
  "product_updates": [...],
  "messaging_trends": "...",
  "strategic_positioning": "...",
  "opportunities_for_keenfox": [...]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return clean_json(response.text)