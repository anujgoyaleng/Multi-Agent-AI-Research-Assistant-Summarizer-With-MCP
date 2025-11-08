# 🚀 Quick Start Guide

Get up and running with the AI Research Assistant in 3 simple steps!

## ⚡ For Windows Users

### Step 1: Setup (First Time Only)
```bash
setup.bat
```
This will:
- Create a virtual environment
- Install all dependencies
- Set up the project structure

### Step 2: Configure API Key
1. Rename `.env.example` to `.env`
2. Get your API key from: https://makersuite.google.com/app/apikey
3. Add it to `.env`:
   ```
   api_key=YOUR_ACTUAL_API_KEY_HERE
   ```

### Step 3: Launch
```bash
run.bat
```
The app will open automatically in your browser! 🎉

---

## 💻 For Mac/Linux Users

### Step 1: Setup
```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure API Key
```bash
# Copy example file
cp .env.example .env

# Edit with your API key
nano .env
```

Add your API key:
```
api_key=YOUR_ACTUAL_API_KEY_HERE
```

### Step 3: Launch
```bash
streamlit run app.py
```

---

## 🎯 First Use Tutorial

### 1. Enter a Topic
Type any research topic in the input field:
- "Artificial Intelligence in Healthcare"
- "Climate Change Solutions"
- "Quantum Computing Basics"

### 2. Generate Content
Click the buttons to create different types of content:
- **📝 Generate Report** - Comprehensive research
- **📰 Fetch News** - Latest updates
- **📄 Create Summary** - Condensed version

### 3. Explore Features
Navigate through the tabs:
- **Research Report** - Full detailed report
- **Summary** - Quick overview
- **Latest News** - Recent developments
- **Q&A Chat** - Ask questions
- **Feedback** - Share your thoughts

### 4. Download & Save
- Reports are auto-saved in the `reports/` folder
- Click "Download Report" to get a Markdown file
- Files are timestamped for easy organization

---

## 🔑 Getting Your API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key
5. Paste it in your `.env` file

**Note:** Keep your API key private and never share it publicly!

---

## 💡 Pro Tips

### For Best Results
- ✅ Be specific with your research topics
- ✅ Generate a report before creating a summary
- ✅ Use the Q&A feature to explore deeper
- ✅ Check the `reports/` folder for saved files

### Common Use Cases
- **Students**: Research papers and study materials
- **Professionals**: Market research and analysis
- **Writers**: Content research and fact-checking
- **Educators**: Teaching materials and resources

---

## ❓ Need Help?

### Common Issues

**"API key not found" error?**
- Make sure `.env` file exists in the project root
- Check that `api_key=` has your actual key
- No spaces around the `=` sign

**App won't start?**
- Ensure Python 3.8+ is installed
- Check that all dependencies installed correctly
- Try running `pip install -r requirements.txt` again

**Slow responses?**
- This is normal for complex research topics
- Gemini AI processes take a few seconds
- Check your internet connection

### Get Support
- Check the main [README.md](README.md) for detailed docs
- Review [CHANGELOG.md](CHANGELOG.md) for recent updates
- Open an issue on GitHub for bugs

---

## 🎉 You're Ready!

Start researching and exploring with your AI assistant. Happy researching! 🚀

---

<div align="center">

**Made with 💜 and ☕**

[⬆ Back to Top](#-quick-start-guide)

</div>
