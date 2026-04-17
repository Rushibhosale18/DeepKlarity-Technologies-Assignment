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
    Return ONLY JSON. STRICTLY follow this format:
    {{
        "title": "String",
        "cuisine": "String",
        "prep_time": "String",
        "cook_time": "String",
        "total_time": "String",
        "servings": Number,
        "difficulty": "easy/medium/hard",
        "ingredients": [
            {{ "quantity": "String", "unit": "String", "item": "String" }}
        ],
        "instructions": ["String (Step 1)", "String (Step 2)"],
        "nutrition_estimate": {{
            "calories": "String or Number",
            "protein": "String",
            "carbs": "String",
            "fat": "String"
        }},
        "substitutions": ["String 1", "String 2", "String 3"],
        "shopping_list": {{
            "Category Name": ["Item 1", "Item 2"]
        }},
        "related_recipes": ["String 1", "String 2", "String 3"]
    }}

    TEXT:
    {text}
    """

    try:
        # Switching to 2.0-flash as my check showed 1.5-flash is unavailable for this key
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[prompt],
        )
    except Exception as e:
        # Last ditch effort with 'flash-latest' if 2.0 fails
        try:
           response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=[prompt],
            )
        except Exception as inner_e:
            return {"error": f"LLM Error: {str(inner_e)}"}

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
