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
    # Get the current working directory (where the command is run)
    cwd = os.getcwd()

    # Add the current working directory to sys.path
    if cwd not in sys.path:
        sys.path.insert(0, cwd)

    # Print the paths for debugging (optional)
    # print(f"sys.path: {sys.path}")

    # Dynamically find the path to this module within the package
    entry_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "entry_point.py"))

    # Execute the main logic of the script
    subprocess.run([sys.executable, entry_file_path])
if __name__ == "__main__":
    main() 