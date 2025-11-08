import subprocess
import sys
import time

print("=" * 60)
print("Starting MCP Server...")
print("=" * 60)
print("\nServer will run on: http://127.0.0.1:8000/mcp")
print("\nPress Ctrl+C to stop the server\n")

try:
    subprocess.run([sys.executable, "research_server.py"])
except KeyboardInterrupt:
    print("\n\nServer stopped.")
