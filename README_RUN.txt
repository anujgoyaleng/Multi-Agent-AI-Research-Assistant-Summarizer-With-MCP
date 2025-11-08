========================================
HOW TO RUN THE PROJECT
========================================

STEP 1: Start the MCP Server
-----------------------------
Open a terminal/command prompt and run:
    python start_server.py

Wait until you see:
    "Server URL: http://127.0.0.1:8000/mcp"

Keep this terminal open!


STEP 2: Start the Streamlit App
--------------------------------
Open a NEW terminal/command prompt and run:
    python -m streamlit run research_client_ui.py

The app will open in your browser at:
    http://localhost:8501


TROUBLESHOOTING
---------------
If you get connection errors:
1. Make sure the MCP server (Step 1) is running
2. Wait 5-10 seconds after starting the server
3. Then start the Streamlit app (Step 2)

To stop:
- Press Ctrl+C in both terminals
