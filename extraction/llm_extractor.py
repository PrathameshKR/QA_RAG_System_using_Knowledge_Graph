import google.generativeai as genai
from utils.helpers import extract_json
from config import GEMINI_API_KEY, MODEL

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL)

def extract_triples(text, year):
    prompt = f"""
    Extract engineering knowledge as triples with time.

    Return STRICT JSON:
    [
      {{"subject": "...", "relation": "...", "object": "...", "time": "{year}"}}
    ]

    Text:
    {text}
    """

    response = model.generate_content(prompt)

    output = response.text

    return extract_json(output)