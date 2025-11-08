# 🤖 AI Research Assistant & Summarizer

A modern Streamlit-based AI platform that leverages Google Gemini AI to perform research, summarization, news aggregation, and interactive Q&A.

## ✨ Features

### 📝 Core Functionality
- **Generate Research Reports** - Create comprehensive reports with introduction, key findings, recent developments, and conclusions
- **Smart Summaries** - Condense reports into concise, easy-to-read summaries
- **Latest News** - Fetch and aggregate recent news on any topic
- **Interactive Q&A** - Ask questions about your research and get AI-powered answers
- **Auto-Save Reports** - Automatically saves generated reports as Markdown files

### 🎨 Modern UI
- Beautiful blue gradient theme
- Responsive design with smooth animations
- Intuitive tab-based navigation
- Clean, professional interface

### 🚀 Technology Stack
- **Frontend/UI**: Streamlit
- **Backend**: Python, LangChain
- **LLM**: Google Gemini AI (gemini-2.0-flash)
- **Data Storage**: Local Markdown files

## 📁 Project Structure

```
├── app.py                  # Main application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create from .env.example)
├── .env.example           # Example environment file
├── reports/               # Generated reports directory
└── README.md              # This file
```

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Multi-Agent-AI-Research-Assistant-Summarizer-With-MCP-main
```

### 2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```env
api_key=YOUR_GOOGLE_GENAI_API_KEY
```

Get your Google Gemini API key from: https://makersuite.google.com/app/apikey

### 5. Run the application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 How to Use

1. **Enter a Topic** - Type your research topic in the input field
2. **Generate Report** - Click to create a detailed research report
3. **Fetch News** - Get the latest news and updates on your topic
4. **Create Summary** - Generate a concise summary of your report
5. **Ask Questions** - Use the Q&A tab to ask questions about your research
6. **Download** - Save your reports as Markdown files

## 🎯 Use Cases

- Academic research and literature reviews
- Market research and competitive analysis
- News monitoring and trend analysis
- Quick topic overviews and summaries
- Educational content creation

## 🔒 Privacy & Security

- All processing happens through Google Gemini API
- Reports are saved locally on your machine
- No data is stored on external servers
- API key is stored securely in .env file

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is licensed under the MIT License - free to use, modify, and distribute.

## 👨‍💻 Author

Built with ❤️ by [Ayush Ghosh](https://github.com/ai-codesmith-solver/)

## 🙏 Acknowledgments

- Google Gemini AI for powerful language models
- Streamlit for the amazing web framework
- LangChain for AI orchestration tools

---

⭐ If you find this project helpful, please give it a star on GitHub!
