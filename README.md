# FlavorSync - Recipe Extractor & Meal Planner

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
  * **Payload:** `{ "url": "https://..." }`
  * **Operation:** Scrapes URL, queries Gemini LLM for structured format, saves to Database, returns JSON.
* **GET `/api/recipes`**
  * **Operation:** Returns a list of all stored recipes in history.
* **GET `/api/recipes/{id}`**
  * **Operation:** Returns specific complete recipe data for modal viewing.

## Evaluation Criteria Highlights
* **LLM Prompt Design:** Prompt safely bypasses markdown block hallucinations using strict templating. Included in `prompts/recipe_extraction.txt`.
* **Database:** Clean SQLAlchemy models store natively structured JSONB elements gracefully representing Shopping Categories and Sub-Ingredients.
* **Extraction Quality:** Extracted logic avoids non-content text by using `BeautifulSoup` stripping `<style>` and `<script>`.
