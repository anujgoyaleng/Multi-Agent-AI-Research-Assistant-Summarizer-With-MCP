# 🤖 AI Research Assistant & Summarizer

A modern, intelligent research platform powered by Google Gemini AI. Generate comprehensive research reports, fetch latest news, create summaries, and interact with your research through an intuitive Q&A interface.

## ✨ Features

### 📝 Core Functionality
- **Comprehensive Research Reports** - Generate detailed reports with introduction, key findings, analysis, and conclusions
- **Smart AI Summaries** - Condense lengthy reports into concise, actionable summaries
- **Real-time News Aggregation** - Fetch and analyze the latest news on any topic
- **Interactive Q&A Chat** - Ask questions about your research and get intelligent answers
- **Auto-Save & Export** - Automatically save reports and download in Markdown format
- **Feedback System** - AI-powered sentiment analysis for user feedback

### 🎨 Modern UI/UX
- Stunning gradient theme with smooth animations
- Responsive design optimized for all screen sizes
- Intuitive tab-based navigation
- Professional, clean interface
- Custom scrollbars and hover effects
- Enhanced typography with Inter font

### 🚀 Technology Stack
- **Frontend**: Streamlit with custom CSS
- **Backend**: Python, LangChain
- **AI Model**: Google Gemini 2.0 Flash
- **Storage**: Local Markdown files

## 📁 Project Structure

```
├── app.py                  # Main application (enhanced UI)
├── llm.py                  # LLM initialization
├── feedback.py             # Feedback sentiment analysis
├── get_mcp.py             # MCP integration (optional)
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── .env.example           # Example environment file
├── setup.bat              # Windows setup script
├── run.bat                # Windows launch script
├── reports/               # Auto-saved reports directory
└── README.md              # Documentation
```

## 🛠️ Quick Start

> 📖 **New to the project?** Check out the [QUICK_START.md](QUICK_START.md) guide for a detailed walkthrough!

### Windows Users (Recommended)

1. **Run Setup** (First time only)
   ```bash
   setup.bat
   ```

2. **Configure API Key**
   - Rename `.env.example` to `.env`
   - Add your Google Gemini API key:
     ```env
     api_key=YOUR_GOOGLE_GENAI_API_KEY
     ```
   - Get your API key from: https://makersuite.google.com/app/apikey

3. **Launch Application**
   ```bash
   run.bat
   ```

### Mac/Linux Users

1. **Setup Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure API Key**
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   ```

3. **Launch Application**
   ```bash
   streamlit run app.py
   ```

The app will open automatically at `http://localhost:8501` 🚀

## 📖 How to Use

### Basic Workflow

1. **Enter Research Topic**
   - Type your topic in the input field (e.g., "Artificial Intelligence", "Climate Change")

2. **Generate Content**
   - Click **"Generate Report"** for comprehensive research
   - Click **"Fetch News"** for latest updates
   - Click **"Create Summary"** to condense your report

3. **Explore Results**
   - Navigate through tabs to view different content types
   - Download reports in Markdown format
   - Ask questions in the Q&A tab

4. **Provide Feedback**
   - Share your experience in the Feedback tab
   - Rate the tool and get AI-powered responses

### Tips for Best Results

- Be specific with your research topics
- Generate a report before creating a summary
- Use the Q&A feature to dive deeper into findings
- Check the `reports/` folder for auto-saved files

## 🎯 Use Cases

- 📚 **Academic Research** - Literature reviews and research papers
- 💼 **Business Intelligence** - Market research and competitive analysis
- 📰 **News Monitoring** - Track trends and developments
- 🎓 **Education** - Quick topic overviews and study materials
- 📊 **Content Creation** - Research for articles and presentations

## 🔒 Privacy & Security

- ✅ All processing via Google Gemini API
- ✅ Reports saved locally on your machine
- ✅ No external data storage
- ✅ API key secured in `.env` file
- ✅ No tracking or analytics

## 🐛 Troubleshooting

**App won't start?**
- Ensure Python 3.8+ is installed
- Check that all dependencies are installed
- Verify your API key in `.env` file

**API errors?**
- Confirm your Gemini API key is valid
- Check your internet connection
- Ensure you haven't exceeded API rate limits

**Reports not saving?**
- Check write permissions in the project folder
- Ensure the `reports/` directory exists

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs via GitHub Issues
- 💡 Suggest new features
- 🔧 Submit pull requests
- 📖 Improve documentation

## 📝 License

MIT License - Free to use, modify, and distribute.

## 👨‍💻 Author

Built with ❤️ by [Ayush Ghosh](https://github.com/ai-codesmith-solver/)

## 🙏 Acknowledgments

- **Google Gemini AI** - Powerful language models
- **Streamlit** - Amazing web framework
- **LangChain** - AI orchestration tools

---

<div align="center">

⭐ **If you find this project helpful, please give it a star!** ⭐

Made with 💜 and ☕

</div>
