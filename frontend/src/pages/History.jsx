import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Eye, Clock, X } from 'lucide-react';
import RecipeDisplay from '../components/RecipeDisplay';
import './History.css';

const History = () => {
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedRecipe, setSelectedRecipe] = useState(null);

  useEffect(() => {
    fetchRecipes();
  }, []);

  const fetchRecipes = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/recipes');
      setRecipes(response.data);
    } catch (error) {
      console.error("Failed to fetch history", error);
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (isoString) => {
    if (!isoString) return 'Unknown';
    return new Date(isoString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  };

  return (
    <div className="history-container">
      <div className="card">
        <h2 className="history-title">Extraction History</h2>
        <p className="subtitle">View and revisit your past AI-extracted recipes</p>
        
        {loading ? (
          <div className="loading-state">Loading history...</div>
        ) : recipes.length === 0 ? (
          <div className="empty-state">No recipes extracted yet.</div>
        ) : (
          <div className="table-container mt-4">
            <table>
              <thead>
                <tr>
                  <th>Title</th>
                  <th>Cuisine</th>
                  <th>Difficulty</th>
                  <th>Date Extracted</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                {recipes.map(recipe => (
                  <tr key={recipe.id}>
                    <td className="font-medium text-white">{recipe.title}</td>
                    <td>{recipe.cuisine || '-'}</td>
                    <td>
                      {recipe.difficulty && (
                        <span className={`badge diff-${recipe.difficulty.toLowerCase()}`}>
                          {recipe.difficulty}
                        </span>
                      )}
                    </td>
                    <td>{formatDate(recipe.created_at)}</td>
                    <td>
                      <button 
                        className="btn-details"
                        onClick={() => setSelectedRecipe(recipe)}
                      >
                        <Eye size={16} /> Details
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* Details Modal */}
      {selectedRecipe && (
        <div className="modal-overlay" onClick={() => setSelectedRecipe(null)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <h3>Recipe Details</h3>
              <button className="close-btn" onClick={() => setSelectedRecipe(null)}>
                <X size={24} />
              </button>
            </div>
            <div className="modal-body">
              <RecipeDisplay recipe={selectedRecipe} />
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default History;
