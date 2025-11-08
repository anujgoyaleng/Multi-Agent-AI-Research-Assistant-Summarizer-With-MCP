@echo off
echo ========================================
echo   AI Research Assistant Launcher
echo ========================================
echo.
echo Starting the application...
echo.

REM Activate virtual environment if it exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo Virtual environment activated.
) else (
    echo No virtual environment found. Using system Python.
)

echo.
echo Launching Streamlit app...
echo The app will open in your browser automatically.
echo.
echo Press Ctrl+C to stop the application.
echo ========================================
echo.

streamlit run app.py

pause
