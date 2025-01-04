from pathlib import Path
from flask import Flask, jsonify, request
from flask_cors import CORS
from atlaz.utility import build_directory_tree_json, write_txt
import logging

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
logging.basicConfig(level=logging.INFO)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json or {}
    msg = data.get('message', '')
    print(f"Received message: {msg}")
    write_txt(msg, 'message.txt')
    logging.error(f"Received message: {msg}")
    return jsonify({"status": "ok", "echo": msg})

@app.route('/api/directory_tree', methods=['GET'])
def get_directory_tree():
    """
    Dynamically build and return a JSON representation of the directory
    where this server is launched.
    """
    root_path = Path.cwd()  # The folder you're in when you start the server
    ignore_items = {'__pycache__', 'node_modules', '.git', '.venv', 'venv'}

    # This list will define which items to leave *unchecked* by default
    default_unmarked = ['.gitignore', 'docker-compose.yml', '__pycache__', 'x_deploy.md']

    tree_json = build_directory_tree_json(root_path, ignore=ignore_items, max_depth=20)

    # Return both the directory structure and the default_unmarked items
    return jsonify({
        "tree": tree_json,
        "default_unmarked": default_unmarked
    })