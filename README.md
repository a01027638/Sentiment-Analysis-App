# 🎬 Movie Review Sentiment Analysis 🎭

A **Streamlit-based web application** that uses **Qwen2-0.5B-Instruct** to analyze the sentiment of movie reviews.  
The app provides two modes of inference:

- **Zero-shot sentiment analysis**: classifies sentiment without prior examples.  
- **Few-shot sentiment analysis**: classifies sentiment using several examples, including ambiguous phrases, for better accuracy.  

---

## 🚀 Features
- 🎯 **Zero-shot Sentiment Analysis**: quick classification with no examples.  
- 🔍 **Few-shot Sentiment Analysis**: classification guided by multiple examples (handles ambiguous phrases better).  
- 🌍 **Multilingual support (basic)**: works best in English, but can also handle Spanish and other languages if added to few-shot examples.  
- ⚡ **Streamlit UI**: simple, clean interface with real-time results.  
- 📂 **Local execution**   

---

## 📦 Requirements

Make sure you have **Python 3.9+** installed.  

# Instructions

# 📖 How to Run the Movie Review Sentiment Analysis App

## 1) Prerequisites
- **Python 3.9+** installed (check with `python --version` or `python3 --version`).
- **Git** installed (optional; you can also download the ZIP from GitHub).

> ℹ️ The first run will download the model from Hugging Face; this can take a minute.

---

## 2) Get the project

### Option A — Clone with Git
```bash
git clone https://github.com/<your-username>/sentiment-app.git
cd sentiment-
```
### Option B — Download ZIP
Go to your GitHub repo page.
Click Code → Download ZIP.
Unzip it and open the folder in a terminal.

## 3) Create a virtual environemnt 
Windows (PowerShell)
```bash
python -m venv .venv
.\.venv\Scripts\Activate
```
MacOS / Linux 
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Upgrade pip
```bash
python -m pip install --upgrade pip
```

## 4) Install dependencies
```bash
pip install -r requirements.txt
```

## 5) Run the app
```bash
streamlit run sentiment_app.py
```

## 6) Use the app
Paste a movie review into the text area.
Click Analyze Sentiment.
You’ll see two outputs:

🎯 Zero-shot Result
🔍 Few-shot Result (uses examples for better handling of ambiguous phrases).


