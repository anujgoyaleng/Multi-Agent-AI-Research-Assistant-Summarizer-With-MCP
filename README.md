# 🤖 AI Research Assistant

A fast, lightweight research tool powered by **Google Gemini AI**, built with **Streamlit**. It generates structured research reports, fetches real-time news, summarizes content, and provides an interactive Q&A interface — all within a clean, modern UI.

---

## 🚀 Features

* **AI-Generated Research Reports**
  Structured insights including introduction, key findings, recent updates, analysis, and conclusion.

* **Real-time News Fetching**
  Pulls and summarizes the latest relevant headlines.

* **Smart Summaries**
  Clear, concise 200–300 word summaries from generated reports.

* **Interactive Q&A Chat**
  Context-aware answers with chat history.

* **Secure API Key Handling**
  API key stored only in **localStorage** — never sent to any server.

* **Modern Minimal UI**
  Responsive design, dark mode, smooth interactions.

* **Markdown Export**
  Auto-saves generated reports in `/reports` with timestamps.

---

## 📦 Installation

### Requirements

* Python **3.8+**
* Google Gemini API key

### Setup

```bash
git clone https://github.com/yourusername/ai-research-assistant.git
cd ai-research-assistant
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔑 API Key Setup

You can add your Google Gemini API key in two ways:

### 1. In-App (Recommended)

* Launch the app
* Enter your API key on the welcome screen
* Key is stored securely in your browser only

### 2. Environment Variable

Create a `.env`:

```env
api_key=YOUR_GEMINI_API_KEY
```

---

## 📁 Project Structure

```
ai-research-assistant/
├── app.py
├── api_key_manager.py
├── llm.py
├── feedback.py
├── requirements.txt
├── reports/
└── screenshot_demo/
```

---

## 🌐 Deployment

### Streamlit Cloud

* Push repo to GitHub
* Deploy via [https://share.streamlit.io](https://share.streamlit.io)
* Set `api_key` in app secrets (optional)

### Docker

```bash
docker build -t ai-research-assistant .
docker run -p 8501:8501 ai-research-assistant
```

---

## 🛠 Troubleshooting

* Ensure Python 3.8+
* Check all dependencies installed
* Validate API key (must start with `AIza`)
* Clear browser localStorage if key not loading

---

## 🤝 Contributing

Pull requests are welcome!
Please open an issue for feature requests or bug reports.


✅ Rewrite it in a corporate/enterprise tone
Just tell me!
