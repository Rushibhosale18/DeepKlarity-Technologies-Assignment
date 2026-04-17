from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class Ingredient(BaseModel):
    quantity: str
    unit: str
    item: str

class NutritionEstimate(BaseModel):
    calories: Optional[int]
    protein: Optional[str]
    carbs: Optional[str]
    fat: Optional[str]

class RecipeResponse(BaseModel):
    id: int
    url: str
    title: str
    cuisine: Optional[str]
    prep_time: Optional[str]
    cook_time: Optional[str]
    total_time: Optional[str]
    servings: Optional[int]
    difficulty: Optional[str]
    ingredients: List[Ingredient]
    instructions: List[str]
    nutrition_estimate: NutritionEstimate
    substitutions: List[str]
    shopping_list: Dict[str, List[str]]
    related_recipes: List[str]

    class Config:
        from_attributes = True

class ExtractRequest(BaseModel):
    url: str
