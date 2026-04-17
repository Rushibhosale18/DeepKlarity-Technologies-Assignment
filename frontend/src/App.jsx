import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom';
import ExtractRecipe from './pages/ExtractRecipe';
import History from './pages/History';
import { ChefHat, History as HistoryIcon } from 'lucide-react';
import './App.css';

function App() {
  return (
    <Router>
      <div className="layout">
        <nav className="sidebar">
          <div className="logo">
            <ChefHat size={32} color="var(--primary)" />
            <h2>FlavorSync</h2>
          </div>
          <div className="nav-links">
            <NavLink to="/" className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}>
              <ChefHat size={20} />
              <span>Extract Recipe</span>
            </NavLink>
            <NavLink to="/history" className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}>
              <HistoryIcon size={20} />
              <span>History</span>
            </NavLink>
          </div>
        </nav>
        <main className="main-content">
          <header className="topbar">
            <h1>Recipe Extraction & Meal Planner</h1>
            <p>Powered by AI</p>
          </header>
          <div className="page-container">
            <Routes>
              <Route path="/" element={<ExtractRecipe />} />
              <Route path="/history" element={<History />} />
            </Routes>
          </div>
        </main>
      </div>
    </Router>
  );
}

export default App;
