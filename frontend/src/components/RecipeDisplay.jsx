import React from 'react';
import { Clock, Users, ChefHat, Activity, ClipboardList, RefreshCw, ShoppingCart, Link } from 'lucide-react';
import './RecipeDisplay.css';

const RecipeDisplay = ({ recipe }) => {
  if (!recipe) return null;

  return (
    <div className="recipe-display">
      <div className="recipe-header">
        <h2 className="title">{recipe.title}</h2>
        <div className="tags">
          {recipe.cuisine && <span className="badge cuisine">{recipe.cuisine}</span>}
          {recipe.difficulty && <span className={`badge diff-${recipe.difficulty.toLowerCase()}`}>{recipe.difficulty}</span>}
        </div>
        <div className="meta">
          <div className="meta-item"><Clock size={18} /> Prep: {recipe.prep_time || 'N/A'}</div>
          <div className="meta-item"><Clock size={18} /> Cook: {recipe.cook_time || 'N/A'}</div>
          <div className="meta-item"><Activity size={18} /> Total: {recipe.total_time || 'N/A'}</div>
          <div className="meta-item"><Users size={18} /> Servings: {recipe.servings || 'N/A'}</div>
        </div>
      </div>

      <div className="grid-layout">
        <div className="left-col">
          <div className="card list-section">
            <h3 className="section-title"><ClipboardList size={20}/> Ingredients</h3>
            <ul className="ingredient-list">
              {recipe.ingredients?.map((ing, idx) => (
                <li key={idx}>
                  <span className="qty">{ing.quantity} {ing.unit}</span>
                  <span className="item">{ing.item}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="card list-section">
            <h3 className="section-title"><ChefHat size={20} /> Instructions</h3>
            <ol className="instruction-list">
              {recipe.instructions?.map((step, idx) => (
                <li key={idx}><span>{step}</span></li>
              ))}
            </ol>
          </div>
        </div>

        <div className="right-col">
          <div className="card nutrition-card">
            <h3 className="section-title"><Activity size={20}/> Nutrition facts</h3>
            <div className="nutrition-grid">
              <div className="nutr-item">
                <span className="nutr-val">{recipe.nutrition_estimate?.calories || 'N/A'}</span>
                <span className="nutr-label">Calories</span>
              </div>
              <div className="nutr-item">
                <span className="nutr-val">{recipe.nutrition_estimate?.protein || 'N/A'}</span>
                <span className="nutr-label">Protein</span>
              </div>
              <div className="nutr-item">
                <span className="nutr-val">{recipe.nutrition_estimate?.carbs || 'N/A'}</span>
                <span className="nutr-label">Carbs</span>
              </div>
              <div className="nutr-item">
                <span className="nutr-val">{recipe.nutrition_estimate?.fat || 'N/A'}</span>
                <span className="nutr-label">Fat</span>
              </div>
            </div>
          </div>

          <div className="card info-card">
            <h3 className="section-title"><RefreshCw size={20}/> Substitutions</h3>
            <ul className="subst-list">
              {recipe.substitutions?.map((sub, idx) => <li key={idx}>{sub}</li>)}
            </ul>
          </div>

          <div className="card info-card">
            <h3 className="section-title"><ShoppingCart size={20}/> Shopping List</h3>
            {recipe.shopping_list && Object.keys(recipe.shopping_list).map(category => (
              <div key={category} className="shopping-category">
                <h4 className="cat-title">{category}</h4>
                <ul>
                  {recipe.shopping_list[category].map((item, idx) => <li key={idx}>{item}</li>)}
                </ul>
              </div>
            ))}
          </div>

          <div className="card info-card">
            <h3 className="section-title"><Link size={20}/> Related Recipes</h3>
            <ul className="related-list">
              {recipe.related_recipes?.map((rel, idx) => <li key={idx}>{rel}</li>)}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RecipeDisplay;
