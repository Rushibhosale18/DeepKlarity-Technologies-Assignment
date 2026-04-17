import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from schemas import RecipeResponse
import json
from dotenv import load_dotenv

load_dotenv()

def process_recipe_text(text: str) -> dict:
    """Passes the scraped text to Gemini to extract structured recipe data."""
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    
    prompt = PromptTemplate.from_template(
        """You are an expert culinary assistant and data extractor.
        Extract the recipe details from the following scraped web text.
        Return the result EXACTLY as a JSON object matching this schema. Do not include markdown formatting like ```json, just return the raw JSON object.
        
        {{
            "title": "Recipe Title",
            "cuisine": "Cuisine type (e.g., American, Italian)",
            "prep_time": "Prep time (e.g., '10 mins')",
            "cook_time": "Cook time",
            "total_time": "Total time",
            "servings": 4,
            "difficulty": "easy, medium, or hard",
            "ingredients": [
                {{ "quantity": "amount (e.g. 4)", "unit": "unit (e.g. slices, cups)", "item": "item name" }}
            ],
            "instructions": [
                "Step 1...",
                "Step 2..."
            ],
            "nutrition_estimate": {{
                "calories": 300,
                "protein": "10g",
                "carbs": "20g",
                "fat": "5g"
            }},
            "substitutions": [
                "Substitute 1...",
                "Substitute 2...",
                "Substitute 3..."
            ],
            "shopping_list": {{
                "category1 (e.g. dairy)": ["item1", "item2"],
                "category2 (e.g. produce)": ["item3"]
            }},
            "related_recipes": [
                "Related Recipe 1",
                "Related Recipe 2",
                "Related Recipe 3"
            ]
        }}
        
        Scraped Text:
        {text}
        """
    )
    
    chain = prompt | llm
    
    response = chain.invoke({"text": text})
    raw_content = response.content.strip()
    
    if raw_content.startswith("```json"):
        raw_content = raw_content[7:]
    if raw_content.startswith("```"):
        raw_content = raw_content[3:]
    if raw_content.endswith("```"):
        raw_content = raw_content[:-3]
        
    return json.loads(raw_content.strip())
