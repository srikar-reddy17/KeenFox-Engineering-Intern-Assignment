# KeenFox Competitive Intelligence System

## SETUP & RUN INSTRUCTIONS

1. Clone or download the project folder.

2. Open terminal / PowerShell and navigate to the project directory:
   cd keenfox-ai-challenge

3. Install required dependencies:
   pip install -r requirements.txt

4. Create a .env file in the root directory and add your Gemini API key:
   GEMINI_API_KEY=your_api_key_here

5. Run the main pipeline:
   python main.py

   This will:

   * Scrape competitor data
   * Analyze it using Gemini
   * Generate insights and recommendations
   * Save output in: outputs/report.json

6. Launch the dashboard:
   python -m streamlit run app.py

7. Open the browser link shown in terminal (usually http://localhost:8501)

8. Use the dashboard to:

   * View competitor insights
   * View strategy recommendations
   * Check changes across runs
   * Ask questions using the Q&A feature
