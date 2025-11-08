# 🧹 Cleanup Instructions

## Files to DELETE (Unnecessary/Duplicate Files)

### Duplicate App Files
- `app_final.py` (replaced by `app.py`)
- `app_optimized.py` (replaced by `app.py`)
- `simple_app.py` (replaced by `app.py`)
- `research_client_ui.py` (not needed for basic version)
- `research_server.py` (not needed for basic version)
- `start_server.py` (not needed for basic version)

### Test/Utility Files
- `test_brightdata.py` (test file)
- `feedback.py` (not integrated)
- `get_mcp.py` (not needed for basic version)
- `llm.py` (integrated into app.py)

### Old Batch Files
- `LAUNCH.bat` (replaced by `run.bat`)
- `start_app.bat` (replaced by `run.bat`)
- `START.bat` (replaced by `run.bat`)

### Documentation
- `README_RUN.txt` (replaced by README.md)

### Folders to DELETE
- `screenshot_demo/` (not needed in production)
- `reports/` (will be auto-created, delete old reports)

## Files to KEEP

### Core Files
- ✅ `app.py` - Main application (NEW)
- ✅ `requirements.txt` - Dependencies (UPDATED)
- ✅ `README.md` - Documentation (UPDATED)
- ✅ `.env` - Your environment variables (KEEP YOUR API KEY)
- ✅ `.env.example` - Example env file (UPDATED)
- ✅ `.gitignore` - Git ignore file (NEW)
- ✅ `run.bat` - Run script (NEW)

## How to Clean Up

### Option 1: Manual Deletion
Delete the files and folders listed above manually.

### Option 2: Using Command Prompt (Windows)
```batch
cd Multi-Agent-AI-Research-Assistant-Summarizer-With-MCP-main

# Delete duplicate app files
del app_final.py app_optimized.py simple_app.py research_client_ui.py research_server.py start_server.py

# Delete test/utility files
del test_brightdata.py feedback.py get_mcp.py llm.py

# Delete old batch files
del LAUNCH.bat start_app.bat START.bat

# Delete old documentation
del README_RUN.txt

# Delete folders
rmdir /s /q screenshot_demo
rmdir /s /q reports
```

### Option 3: Keep Everything
If you want to keep the old files for reference, just use the new `app.py` file and ignore the others.

## After Cleanup

Your clean project structure will look like:

```
Multi-Agent-AI-Research-Assistant-Summarizer-With-MCP-main/
├── app.py                 # Main application
├── requirements.txt       # Dependencies
├── README.md             # Documentation
├── .env                  # Your API keys
├── .env.example          # Example env file
├── .gitignore           # Git ignore
├── run.bat              # Run script
└── reports/             # Auto-created when you generate reports
```

## Running the Clean Version

1. Make sure you have your `.env` file with your API key
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py` or double-click `run.bat`

---

**Note**: Before deleting anything, make sure you've backed up your `.env` file with your API keys!
