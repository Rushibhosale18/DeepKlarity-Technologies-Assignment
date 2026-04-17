from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from scraper import scrape_recipe
from llm import extract_recipe_llm
import models
import json

router = APIRouter()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from schemas import ExtractRequest

# 🔹 Extract Recipe
@router.post("/extract")
def extract(request: ExtractRequest, db: Session = Depends(get_db)):
    text = scrape_recipe(request.url)

    if not text:
        return {"error": "Failed to scrape URL"}

    data = extract_recipe_llm(text)

    if "error" in data:
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail=data["error"])

    # Save to DB
    recipe = models.Recipe(
        url=request.url,
        title=data.get("title"),
        cuisine=data.get("cuisine"),
        difficulty=data.get("difficulty"),
        data=json.dumps(data)
    )

    db.add(recipe)
    db.commit()

    return data


# 🔹 Get All Recipes (History)
@router.get("/recipes")
def get_recipes(db: Session = Depends(get_db)):
    recipes = db.query(models.Recipe).all()
    results = []
    for r in recipes:
        parsed_data = json.loads(r.data) if r.data else {}
        results.append({
            "id": r.id,
            "url": r.url,
            **parsed_data
        })
    return results


# 🔹 Get Single Recipe
@router.get("/recipes/{id}")
def get_recipe(id: int, db: Session = Depends(get_db)):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == id).first()
    if recipe:
        parsed_data = json.loads(recipe.data) if recipe.data else {}
        return {"id": recipe.id, "url": recipe.url, **parsed_data}
    return {"error": "Not found"}