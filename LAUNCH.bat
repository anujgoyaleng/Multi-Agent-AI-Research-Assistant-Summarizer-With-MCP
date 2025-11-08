@echo off
title Multi-Agent AI Research Assistant
color 0B

echo ============================================================
echo    Multi-Agent AI Research Assistant with MCP
echo ============================================================
echo.
echo [STEP 1/2] Starting MCP Server...
start /MIN "MCP Server" cmd /c python research_server.py
echo    Server starting at http://127.0.0.1:8000/mcp
echo    Waiting 10 seconds for server initialization...
ping 127.0.0.1 -n 11 > nul

echo.
echo [STEP 2/2] Launching Streamlit Application...
echo    App will open at http://localhost:8501
echo.
echo ============================================================
echo.
python -m streamlit run research_client_ui.py
