import subprocess
from sallmon.frontend.server import app
import threading

SALLMON_SERVER_CMD = ""

def start_fastapi_server():
    """Start the FastAPI server."""
    try:
        subprocess.run(SALLMON_SERVER_CMD.split(), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting FastAPI server: {e}")

def start_flask_app():
    """Start the Flask app."""
    app.run(host="0.0.0.0", port=1338, debug=True)

def main():
    """Main function to start all services."""
    # Start FastAPI server in a separate thread
    threading.Thread(target=start_fastapi_server, daemon=True).start()

    # Start Flask app
    start_flask_app()
