import React, { useState } from 'react';
import axios from 'axios';
import { Search, Loader2 } from 'lucide-react';
import RecipeDisplay from '../components/RecipeDisplay';
import './ExtractRecipe.css';

const ExtractRecipe = () => {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleExtract = async (e) => {
    e.preventDefault();
    if (!url) return;
    
    setLoading(true);
    setError('');
    
    try {
      // In production, update this to your backend url
      const response = await axios.post('https://deepklarity-technologies-assignment.onrender.com/api/extract', { url });
      setResult(response.data);
    } catch (err) {
      const detail = err.response?.data?.detail;
      const errorMsg = typeof detail === 'string' ? detail : err.response?.data?.error || 'Failed to extract recipe connecting to backend. Did you start it?';
      setError(errorMsg);
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="extract-container">
      <div className="card input-card">
        <h2>Enter Recipe URL</h2>
        <p className="subtitle">Paste the link to any recipe blog or website</p>
        <form onSubmit={handleExtract} className="input-form">
          <div className="input-group">
            <Search className="search-icon" size={20} />
            <input 
              type="url" 
              placeholder="https://www.allrecipes.com/..." 
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="btn-primary" disabled={loading}>
            {loading ? (
              <span className="flex-center"><Loader2 className="spinner" size={20}/> Extracting AI Data...</span>
            ) : 'Extract Recipe'}
          </button>
        </form>
        {error && <div className="error-message">{error}</div>}
      </div>

      {result && (
        <div className="result-container">
          <RecipeDisplay recipe={result} />
        </div>
      )}
    </div>
  );
};

export default ExtractRecipe;
