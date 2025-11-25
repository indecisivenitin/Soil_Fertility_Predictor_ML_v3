# Soil Fertility Predictor ML  
**Real-time Soil Health Analysis & Smart Fertilizer Recommendation System**  

**Live App** → https://soil-fertility-predictor.onrender.com  



---

### Features
- Predicts soil fertility percentage (0–100%) using Machine Learning  
- Classifies soil: **Ultra-Fertile → Very Good → Average → Needs Improvement → Poor**  
- Gives **personalized fertilizer & amendment recommendations** (Urea, DAP, MOP, FYM, Lime, Gypsum)  
- Beautiful responsive UI with real-time gauge  
- One-click **PDF Report Download** (with score, status & recommendations)  
- Sample **Test Cases** page with auto-fill feature  
- Fully deployed on **Render.com** (free & always live)  

---

### Tech Stack
- **Backend**: Flask (Python)  
- **ML Model**: Random Forest Regressor (trained on 2000+ soil samples)  
- **Frontend**: HTML, Tailwind CSS, JavaScript  
- **PDF Generation**: ReportLab  
- **Deployment**: Render.com + Gunicorn  
- **Model Persistence**: joblib  

---

### Live Demo
**Website**: https://soil-fertility-predictor.onrender.com  
**Test Cases**: https://soil-fertility-predictor.onrender.com/test-cases  

Try the **"Ultra-Fertile Soil"** test case → Should give **98–100%**

---

### How to Run Locally (1 Minute Setup)

```bash
# 1. Clone repo
git clone https://github.com/indecisivenitin/Soil_Fertility_Predictor_ML_v3.git
cd Soil_Fertility_Predictor_ML_v3

# 2. Create virtual environment
python -m venv venv

# 3. Activate venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r backend/requirements.txt

# 5. Run the app
python backend/app.py
