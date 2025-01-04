import os
import subprocess
import sys
import time
import threading

from atlaz.headquarter.client import AtlazClient

def start_app_server():
    """Starts the Flask app server."""
    subprocess.run(["python", "-c", "from atlaz.frontend.python_backend.flask_server import app; app.run(debug=True, port=5050)"])

def start_frontend_client():
    """Starts the AtlazClient."""
    client = AtlazClient()
    client.start_frontend()

def start_full_chain():
    app_thread = threading.Thread(target=start_app_server)
    app_thread.daemon = True
    app_thread.start()
    time.sleep(1)
    start_frontend_client()

def main():
    """Entry point for the atlaz-code command."""
    project_root = os.getcwd()
    sys.path.append(project_root)  # Ensure PYTHONPATH is set
    subprocess.run(["python", "atlaz/headquarter/entry_point.py"])

if __name__ == "__main__":
    main() 