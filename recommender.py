import os
from dotenv import load_dotenv
from google import genai
from utils import clean_json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_recommendations(data):
    prompt = f"""
You are Head of Growth at KeenFox.

Previous insights:
{data.get("previous")}

New insights:
{data.get("current")}

Update recommendations based on changes.

Return JSON:

{{
  "messaging": {{
      "weaknesses_in_market": "...",
      "new_positioning": "...",
      "sample_copy": {{
          "tagline": "...",
          "body": "..."
      }}
  }},
  "channels": {{
      "underutilized": [...],
      "overcrowded": [...],
      "recommendations": [...]
  }},
  "gtm_strategy": [
      {{
        "strategy": "...",
        "rationale": "...",
        "impact": "..."
      }}
  ]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return clean_json(response.text)