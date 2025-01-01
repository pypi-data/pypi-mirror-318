# atlaz/frontend/__init__.py

import http.server
import socketserver
import os

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

def frontend(port=8000):
    # Change the current working directory to the directory of this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    handler = CustomHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving at port {port}")
        print("Open http://localhost:8000 in your browser to view the app.")
        print("Press Ctrl+C to stop the server.")
        httpd.serve_forever()