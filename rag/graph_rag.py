import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL)

def generate_answer(query, context):
    prompt = f"""
    You are an engineering expert.

    Use ONLY this knowledge graph:

    {context}

    Question:
    {query}

    Give a clear explanation.
    """

    response = model.generate_content(prompt)

    return response.text