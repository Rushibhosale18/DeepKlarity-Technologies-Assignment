# FlavorSync - Recipe Extractor & Meal Planner

🚀 **Live Frontend:** [https://deep-klarity-technologies-assignmen.vercel.app/](https://deep-klarity-technologies-assignmen.vercel.app/)
⚙️ **Live Backend API:** [https://deepklarity-technologies-assignment.onrender.com](https://deepklarity-technologies-assignment.onrender.com)

A full-stack application built for the **DeepKlarity Technologies Assignment**. It extracts structured recipe arrays, calculates nutritional facts, generates substitutions and shopping lists from any blog link using LangChain and a Large Language Model.

## Tech Stack
* **Frontend:** React, Vite, Vanilla CSS
* **Backend:** FastAPI, Python, BeautifulSoup4, SQLAlchemy
* **Database:** PostgreSQL
* **AI/LLM Engine:** Google Gemini (1.5 Flash) via LangChain

## Setup Instructions

### 1. Database Setup
1. You must have **PostgreSQL** installed locally.
2. Create a new database called `recipe_planner` (e.g. using pgAdmin).

### 2. Backend Setup
1. Open a terminal and navigate to the `backend` directory.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Update `backend/.env` with your actual Postgres credentials and Gemini API Key.
   ```
   GEMINI_API_KEY=your_key_here
   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/recipe_planner
   ```
4. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### 3. Frontend Setup
1. Open a new terminal and navigate to the `frontend` directory.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the Vite React development server:
   ```bash
   npm run dev
   ```
4. Open the displayed `localhost` link in your browser!

---

## API Endpoints
* **POST `/api/extract`**
  * **Description:** Initiates recipe extraction.
  * **Payload:** `{ "url": "https://example-recipe-url.com" }`
  * **Operation:** Scrapes the provided URL, queries Gemini using LangChain for structured extraction, performs nutrition estimation and substitution generation, saves the result to the PostgreSQL database, and returns the strictly formatted JSON representation.
* **GET `/api/recipes`**
  * **Description:** Retrieves extraction history.
  * **Operation:** Returns a list of all previously stored recipes for displaying in the history tab.
* **GET `/api/recipes/{id}`**
  * **Description:** Fetches detailed data for a specific recipe.
  * **Operation:** Returns the complete stored JSON data for the requested recipe ID, used to populate the modal details interface.

---

## Testing Steps
Follow these steps to end-to-end test the application functionality:
1. **Prepare URLs:** Start with a standard recipe blog URL (e.g., from AllRecipes, Food Network, or any popular food blog). A sample list is provided in `sample_data/test_urls.json`.
2. **Start Both Servers:** Ensure PostgreSQL is running, then verify the backend FastAPI terminal (`uvicorn main:app --reload`) and the frontend React terminal (`npm run dev`) are both active.
3. **Test Extraction:** Navigate to `http://localhost:5173/`. On the **Extract Recipe** tab, paste your URL into the input bar and click "Extract".
4. **Read Output:** Wait roughly 5-15 seconds for the LLM to process. The parsed Title, Ingredients, Instructions, Shopping List, Nutrition Estimate, and Substitutions will render on the screen.
5. **View History:** Click the **History** tab (or navigate using the top bar). You should see your recent extraction listed as a card.
6. **Test Modal:** Click on the recipe card inside the History view. A modal will pop up showcasing the full, preserved breakdown of that recipe fetched natively from the database.

---

## Submission Checklist
This repository includes all required components from the project specifications:
* ✅ **Complete Working Code:** `backend/` and `frontend/` logic.
* ✅ **Screenshots:** Included images of Recipe Extraction, History view, and Details Modal directly in the code repository.
* ✅ **Sample Data:** Located in `sample_data/` (`api_outputs.json` & `test_urls.json`).
* ✅ **LangChain Prompt Templates:** Located in `prompts/` directory (includes specific prompts for extraction, nutrition, substitutions, and meal planning).
* ✅ **README Documentation:** Setup, Endpoints, and Testing included in this file.
