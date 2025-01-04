import os
import threading
from livereload import Server

def start_dev_server(port=8000, open_browser=True):
    """
    Start a Livereload server in a background thread so we don't block
    the rest of the code from continuing.
    """
    server = Server()
    frontend_dir = os.path.dirname(__file__)
    server.watch(os.path.join(frontend_dir, "*.html"))
    server.watch(os.path.join(frontend_dir, "*.css"))
    server.watch(os.path.join(frontend_dir, "scripts", "*.js"))
    server.watch(os.path.join(frontend_dir, "files.json"))
    def run_server():
        delay = 1 if open_browser else None
        server.serve(root=frontend_dir, port=port, open_url_delay=delay, default_filename='index.html')
    t = threading.Thread(target=run_server, daemon=True)
    t.start()