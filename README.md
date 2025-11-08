# 🤖 AI Research Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production-success.svg)

**A modern, intelligent research platform powered by Google Gemini AI**

Generate comprehensive research reports • Fetch latest news • Create summaries • Interactive Q&A

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API Key Setup](#-api-key-setup) • [Deployment](#-deployment)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
  - [Windows](#windows)
  - [Mac/Linux](#maclinux)
- [API Key Setup](#-api-key-setup)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

The **AI Research Assistant** is a cutting-edge web application that leverages Google's Gemini AI to provide comprehensive research capabilities. Built with Streamlit and featuring a modern, minimalist UI, it offers an intuitive interface for conducting research, analyzing news, and generating insights.

### Why Use This Tool?

- **🚀 Fast Research**: Generate comprehensive reports in seconds
- **📰 Real-time News**: Stay updated with the latest developments
- **🤖 AI-Powered**: Leverages Google Gemini 2.0 Flash for intelligent responses
- **🔒 Privacy-First**: Your API key stays in your browser, never sent to servers
- **💎 Modern UI**: Clean, minimalist design for distraction-free research
- **📱 Responsive**: Works seamlessly on desktop, tablet, and mobile

---

## ✨ Features

### Core Functionality

#### 📝 Comprehensive Research Reports
Generate detailed, well-structured research reports with:
- **Introduction**: Clear overview of the topic
- **Key Findings**: Important facts, statistics, and insights
- **Recent Developments**: Latest news, trends, and breakthroughs
- **Analysis**: Deep dive into the findings
- **Conclusion**: Summary and future implications

#### 📰 Real-time News Aggregation
Fetch and analyze the latest news with:
- **Latest Headlines**: 5-7 recent, relevant news items
- **Key Updates**: Important recent developments
- **Trending Topics**: What's currently being discussed
- **Industry Impact**: How developments affect the field

#### 📄 AI Summaries
Create concise, actionable summaries that:
- Highlight main points and key takeaways
- Present information clearly and concisely
- Use bullet points for easy scanning
- Maintain approximately 200-300 words

#### 💬 Interactive Q&A Chat
Ask questions about your research and get:
- Accurate, context-aware answers
- Clear, informative responses
- Chat history for reference
- Ability to dive deeper into topics

#### 💾 Export & Save
Automatically save and download:
- Reports in Markdown format
- Auto-save to local `reports/` folder
- Timestamped filenames
- Easy sharing and archiving

#### ⭐ Feedback System
Provide feedback with:
- AI-powered sentiment analysis
- Rating system (1-5 stars)
- Intelligent responses
- Continuous improvement

### User Interface

#### 🎨 Modern Minimalist Design
- **Clean Layout**: Distraction-free interface
- **Dark Theme**: Easy on the eyes
- **Smooth Animations**: Polished interactions
- **Responsive Design**: Works on all devices
- **Color-Coded Content**: Visual organization

#### 🔑 Secure API Key Management
- **Browser Storage**: Keys stored locally using localStorage
- **Never Transmitted**: Keys never sent to servers
- **Easy Management**: Simple UI to add, update, or remove keys
- **Format Validation**: Ensures correct API key format
- **Status Indicators**: Clear visual feedback

---

## 📸 Screenshots

### Main Interface
![Main Interface](screenshot_demo/main_interface.png)

### Research Report
![Research Report](screenshot_demo/report.png)

### API Key Settings
![API Key Settings](screenshot_demo/api_settings.png)

---

## 🚀 Installation

### Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package manager)
- **Google Gemini API Key** ([Get one here](https://makersuite.google.com/app/apikey))

### Windows

#### Quick Setup (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-research-assistant.git
   cd ai-research-assistant
   ```

2. **Run the setup script**
   ```bash
   setup.bat
   ```
   This will:
   - Create a virtual environment
   - Install all dependencies
   - Set up the project structure

3. **Launch the application**
   ```bash
   run.bat
   ```

The app will automatically open in your default browser at `http://localhost:8501`

#### Manual Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-research-assistant.git
   cd ai-research-assistant
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

### Mac/Linux

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-research-assistant.git
   cd ai-research-assistant
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

---

## 🔑 API Key Setup

The application requires a Google Gemini API key to function. You have two options:

### Option 1: In-App Setup (Recommended)

1. **Launch the application**
   ```bash
   streamlit run app.py
   ```

2. **Enter your API key**
   - On first launch, you'll see an API key entry screen
   - Paste your Google Gemini API key
   - Click "🚀 Start Using the App"

3. **Your key is saved**
   - Stored securely in your browser's localStorage
   - Never transmitted to any server
   - Automatically loaded on future visits

### Option 2: Environment Variable

1. **Create a `.env` file**
   ```bash
   cp .env.example .env
   ```

2. **Add your API key**
   ```env
   api_key=YOUR_GOOGLE_GEMINI_API_KEY
   ```

3. **Launch the application**
   ```bash
   streamlit run app.py
   ```

### Getting Your API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key (starts with `AIza`)
5. Paste it into the application

### API Key Security

- ✅ **Stored Locally**: Keys are stored in your browser's localStorage
- ✅ **Never Transmitted**: Keys are never sent to our servers
- ✅ **Format Validation**: Ensures correct key format before saving
- ✅ **Easy Removal**: One-click key deletion
- ✅ **Full Control**: Add, update, or remove keys anytime

---

## 📖 Usage Guide

### Basic Workflow

1. **Enter Your API Key** (First time only)
   - Launch the app
   - Enter your Google Gemini API key
   - Click "Start Using the App"

2. **Enter a Research Topic**
   - Type your topic in the input field
   - Examples: "Artificial Intelligence", "Climate Change", "Quantum Computing"

3. **Generate Content**
   - **📝 Generate Report**: Create a comprehensive research report
   - **📰 Fetch News**: Get the latest news and updates
   - **📄 Create Summary**: Generate a concise summary (requires report first)

4. **Explore Results**
   - Navigate through tabs to view different content types
   - Download reports in Markdown format
   - Ask questions in the Q&A tab

5. **Provide Feedback**
   - Share your experience in the Feedback tab
   - Rate the tool (1-5 stars)
   - Get AI-powered responses

### Tips for Best Results

#### Research Topics
- **Be Specific**: "Machine Learning in Healthcare" vs "AI"
- **Use Clear Language**: Avoid jargon or abbreviations
- **Focus on One Topic**: Better results than multiple topics

#### Report Generation
- **Wait for Completion**: Reports take 10-30 seconds to generate
- **Review Carefully**: AI-generated content should be verified
- **Save Important Reports**: Use the download button

#### Q&A Feature
- **Ask Specific Questions**: "What are the main benefits?" vs "Tell me more"
- **Reference the Report**: Questions are answered based on the generated report
- **Follow Up**: Ask clarifying questions for deeper insights

#### News Fetching
- **Current Topics**: Works best with recent, trending topics
- **Broad Topics**: May return more diverse news items
- **Verify Sources**: AI summarizes news, always verify important information

---

## 📁 Project Structure

```
ai-research-assistant/
├── app.py                      # Main application file
├── api_key_manager.py          # API key management module
├── feedback.py                 # Feedback system
├── llm.py                      # LLM initialization
├── get_mcp.py                  # MCP integration (optional)
├── test_api_key.py             # API key validation tests
├── requirements.txt            # Python dependencies
├── .env.example                # Example environment file
├── .gitignore                  # Git ignore rules
├── setup.bat                   # Windows setup script
├── run.bat                     # Windows launch script
├── README.md                   # This file
├── .streamlit/
│   └── config.toml             # Streamlit configuration
├── reports/                    # Auto-saved reports directory
└── screenshot_demo/            # Screenshots for documentation
```

### Key Files

#### `app.py`
Main application file containing:
- UI components and layout
- Core research functions
- Tab navigation
- Session state management
- CSS styling

#### `api_key_manager.py`
Handles API key operations:
- Key validation
- localStorage integration
- UI components for key management
- Security features

#### `feedback.py`
Feedback system with:
- Sentiment analysis
- AI-powered responses
- Rating system

#### `llm.py`
LLM configuration:
- Google Gemini initialization
- API key handling
- Model configuration

---

## ⚙️ Configuration

### Streamlit Configuration

Edit `.streamlit/config.toml` to customize:

```toml
[theme]
primaryColor = "#ffffff"
backgroundColor = "#000000"
secondaryBackgroundColor = "#0a0a0a"
textColor = "#ffffff"
font = "sans serif"

[server]
port = 8501
headless = false
```

### Environment Variables

Create a `.env` file with:

```env
# Google Gemini API Key (optional if using in-app setup)
api_key=YOUR_API_KEY_HERE

# Bright Data API Token (optional, for advanced features)
BRIGHT_DATA_API_TOKEN=your_token_here

# Web Unlocker Zone (optional)
WEB_UNLOCKER_ZONE=your_zone_here

# Browser Zone (optional)
BROWSER_ZONE=your_zone_here
```

### Python Dependencies

The application requires:

```txt
streamlit>=1.28.0
langchain>=0.1.0
langchain-core>=0.1.0
langchain-google-genai>=1.0.0
python-dotenv>=1.0.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Deploy AI Research Assistant"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository and branch
   - Set main file path: `app.py`

3. **Add Secrets** (Optional)
   - In your app settings, go to "Secrets"
   - Add your API key (if using environment variable):
     ```toml
     api_key = "your_google_gemini_api_key_here"
     ```

4. **Deploy**
   - Click "Deploy"
   - Your app will be live at `https://your-app-name.streamlit.app`

### Deploy to Heroku

1. **Create `Procfile`**
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Create `setup.sh`**
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n\
   " > ~/.streamlit/config.toml
   ```

3. **Deploy**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Deploy to Docker

1. **Create `Dockerfile`**
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "app.py"]
   ```

2. **Build and run**
   ```bash
   docker build -t ai-research-assistant .
   docker run -p 8501:8501 ai-research-assistant
   ```

---

## 🔧 Troubleshooting

### Common Issues

#### App Won't Start

**Problem**: Application fails to launch

**Solutions**:
- Ensure Python 3.8+ is installed: `python --version`
- Check all dependencies are installed: `pip install -r requirements.txt`
- Verify virtual environment is activated
- Check for port conflicts (default: 8501)

#### API Key Errors

**Problem**: "No API key configured" or "Invalid API key"

**Solutions**:
- Verify your API key starts with "AIza"
- Check key is at least 30 characters long
- Ensure key is active at [Google AI Studio](https://makersuite.google.com/app/apikey)
- Try removing and re-entering the key
- Clear browser localStorage and re-enter key

#### API Rate Limits

**Problem**: "Rate limit exceeded" errors

**Solutions**:
- Wait a few minutes before trying again
- Check your quota at Google Cloud Console
- Consider upgrading your API plan
- Reduce frequency of requests

#### Reports Not Generating

**Problem**: Reports fail to generate or take too long

**Solutions**:
- Check your internet connection
- Verify API key is valid and active
- Try a simpler, more specific topic
- Check Google Gemini API status
- Review browser console for errors

#### localStorage Issues

**Problem**: API key not persisting across sessions

**Solutions**:
- Ensure browser allows localStorage
- Disable private/incognito mode
- Check browser settings for site data permissions
- Try a different browser (Chrome, Firefox, Edge)
- Clear browser cache and re-enter key

#### Deployment Errors

**Problem**: App fails to deploy to Streamlit Cloud

**Solutions**:
- Ensure all dependencies are in `requirements.txt`
- Verify main file path is set to `app.py`
- Check that secrets are properly configured
- Review deployment logs for specific errors
- Ensure repository is public or properly connected

### Getting Help

If you encounter issues not covered here:

1. **Check the Console**: Look for error messages in the browser console (F12)
2. **Review Logs**: Check Streamlit logs for detailed error information
3. **Test API Key**: Run `python test_api_key.py` to verify key validation
4. **Search Issues**: Check GitHub issues for similar problems
5. **Create an Issue**: Open a new issue with:
   - Detailed description of the problem
   - Steps to reproduce
   - Error messages
   - System information (OS, Python version, etc.)

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Report Bugs**: Open an issue describing the bug
- 💡 **Suggest Features**: Share your ideas for improvements
- 📖 **Improve Documentation**: Help make the docs clearer
- 🔧 **Submit Pull Requests**: Fix bugs or add features
- ⭐ **Star the Project**: Show your support

### Development Setup

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/ai-research-assistant.git
   cd ai-research-assistant
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Test your changes thoroughly

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Describe your changes

### Code Style

- Use **4 spaces** for indentation
- Follow **PEP 8** guidelines
- Add **docstrings** to functions
- Keep functions **focused and small**
- Use **meaningful variable names**

### Testing

Before submitting a PR:

1. **Test locally**
   ```bash
   streamlit run app.py
   ```

2. **Test API key validation**
   ```bash
   python test_api_key.py
   ```

3. **Check for errors**
   - Test all features
   - Verify UI responsiveness
   - Check console for errors

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 AI Research Assistant

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

### Technologies

- **[Streamlit](https://streamlit.io)** - Web framework for data apps
- **[Google Gemini AI](https://ai.google.dev)** - Powerful language models
- **[LangChain](https://langchain.com)** - AI orchestration framework
- **[Python](https://python.org)** - Programming language

### Inspiration

This project was inspired by the need for a simple, powerful research tool that respects user privacy while leveraging cutting-edge AI technology.

### Contributors

Thank you to all contributors who have helped improve this project!

---

## 📞 Support

### Get Help

- 📧 **Email**: support@example.com
- 💬 **Discord**: [Join our community](https://discord.gg/example)
- 🐦 **Twitter**: [@AIResearchApp](https://twitter.com/example)
- 📝 **Issues**: [GitHub Issues](https://github.com/yourusername/ai-research-assistant/issues)

### Stay Updated

- ⭐ **Star** the repository to stay updated
- 👀 **Watch** for new releases
- 🔔 **Follow** for announcements

---

## 🗺️ Roadmap

### Upcoming Features

- [ ] **Multi-language Support**: Research in multiple languages
- [ ] **Export to PDF**: Download reports as PDF files
- [ ] **Citation Management**: Automatic citation generation
- [ ] **Collaborative Research**: Share and collaborate on reports
- [ ] **Advanced Analytics**: Visualize research data
- [ ] **Voice Input**: Speak your research queries
- [ ] **Browser Extension**: Quick research from any webpage
- [ ] **Mobile App**: Native iOS and Android apps

### Version History

- **v2.1.0** (Current) - User API key management, minimalist UI
- **v2.0.0** - Enhanced UI, modern design system
- **v1.0.0** - Initial release with core features

---

<div align="center">

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/ai-research-assistant&type=Date)](https://star-history.com/#yourusername/ai-research-assistant&Date)

---

**Made with ❤️ by the AI Research Assistant Team**

[⬆ Back to Top](#-ai-research-assistant)

</div>
