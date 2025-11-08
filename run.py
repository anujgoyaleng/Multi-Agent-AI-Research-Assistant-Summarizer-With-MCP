import subprocess
import time
import sys
import os

print("Starting Multi-Agent AI Research Assistant...")
print("=" * 60)

# Start MCP Server
print("\n[1/2] Starting MCP Server on http://127.0.0.1:8000/mcp")
server_process = subprocess.Popen(
    [sys.executable, "research_server.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    cwd=os.path.dirname(os.path.abspath(__file__))
)

# Wait for server to start
print("Waiting for MCP server to initialize...")
time.sleep(5)

# Start Streamlit App
print("\n[2/2] Starting Streamlit Application...")
print("=" * 60)
print("\nThe app will open in your browser automatically.")
print("If not, navigate to: http://localhost:8501")
print("\nPress Ctrl+C to stop both servers.\n")

try:
    subprocess.run([sys.executable, "-m", "streamlit", "run", "research_client_ui.py"])
except KeyboardInterrupt:
    print("\n\nShutting down...")
    server_process.terminate()
    server_process.wait()
    print("All services stopped.")
