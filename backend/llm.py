import json
import os
from dotenv import load_dotenv
from google import genai

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set in the environment")

client = genai.Client(api_key=api_key)

def extract_recipe_llm(text):
    prompt = f"""
    Extract structured recipe data from this text.

    Return ONLY JSON with:
    title, cuisine, prep_time, cook_time, total_time,
    servings, difficulty,
    ingredients (quantity, unit, item),
    instructions (steps),
    nutrition_estimate (calories, protein, carbs, fat),
    substitutions (3),
    shopping_list (grouped),
    related_recipes (3)

    TEXT:
    {text}
    """

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[prompt],
        )
    except Exception as e:
        return {"error": f"LLM Error: {str(e)}"}

    output_text = ""
    if response and response.candidates:
        candidate = response.candidates[0]
        if candidate.content and candidate.content.parts:
            output_text = "".join(part.text or "" for part in candidate.content.parts)
    
    if not output_text:
        return {"error": "LLM returned empty content"}

    try:
        clean_text = output_text.strip()
        if clean_text.startswith("```json"):
            clean_text = clean_text[7:]
        elif clean_text.startswith("```"):
            clean_text = clean_text[3:]
            
        if clean_text.endswith("```"):
            clean_text = clean_text[:-3]
            
        clean_text = clean_text.strip()
        
        return json.loads(clean_text)
    except Exception as e:
        return {"error": "Invalid JSON from LLM", "raw": output_text, "exception": str(e)}
