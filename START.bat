@echo off
title Multi-Agent AI Research Assistant
color 0A

echo ========================================
echo  Multi-Agent AI Research Assistant
echo ========================================
echo.
echo Starting MCP Server...
start /B python research_server.py
timeout /t 5 /nobreak >nul

echo Starting Streamlit App...
echo.
echo The app will open at: http://localhost:8501
echo.
python -m streamlit run research_client_ui.py
