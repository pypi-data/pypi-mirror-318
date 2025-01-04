import datetime
import json
import logging
from pathlib import Path
from flask import Flask, jsonify, request
from flask_cors import CORS

from atlaz.utility import build_directory_tree_json, write_txt
from atlaz.frontend.python_backend.start_gen import start_gen

server_start_time = datetime.datetime.now().isoformat()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
logging.basicConfig(level=logging.INFO)

def make_paths_relative(tree_list, root_path):
    """
    Recursively convert each item's 'path' from absolute to relative
    relative to the given root_path.
    """
    new_list = []
    for item in tree_list:
        new_item = item.copy()
        abs_path = Path(new_item['path'])
        try:
            rel_path = abs_path.relative_to(root_path)
            new_item['path'] = str(rel_path)
        except ValueError:
            pass
        if 'children' in new_item:
            new_item['children'] = make_paths_relative(new_item['children'], root_path)
        new_list.append(new_item)
    return new_list

credentials = {}

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.json or {}
    api_key = data.get('api_key', '')
    llm_model = data.get('llm_model', '')
    llm_provider = data.get('llm_provider', '')
    message = data.get('message', '')
    selected_files = data.get('selected_files', [])
    
    if not api_key or not llm_model:
        return jsonify({"status": "error", "message": "API key and LLM model are required."}), 400
    if not message:
        return jsonify({"status": "error", "message": "Message is required."}), 400
    if not selected_files:
        return jsonify({"status": "error", "message": "At least one directory must be selected."}), 400
    logging.info(f"Received API Key: {api_key}")
    logging.info(f"Received LLM Model: {llm_model}")
    logging.info(f"Received LLM Provider: {llm_provider}")
    logging.info(f"Received Message: {message}")
    logging.info(f"Received Selected Directories: {selected_files}")
    try:
        start_gen(data)
        print(f'{data=}')
        response = {
            "status": "success",
            "message": "Code generation initiated.",
            "llm_model_used": llm_model
        }
        return jsonify(response)
    except Exception as e:
        logging.error(f"Error during code generation: {e}")
        return jsonify({"status": "error", "message": "An error occurred during code generation."}), 500

@app.route('/api/directory_tree', methods=['GET'])
def get_directory_tree():
    """
    Dynamically build and return a JSON representation of the directory
    where this server is launched, but store paths as relative to root_path.
    """
    root_path = Path.cwd()
    ignore_items = {'__pycache__', 'node_modules', '.git', '.venv', 'venv'}
    default_unmarked = ['.gitignore', 'docker-compose.yml', '__pycache__', 'x_deploy.md']
    tree_json = build_directory_tree_json(root_path, ignore=ignore_items, max_depth=20)
    tree_json_relative = make_paths_relative(tree_json, root_path)
    return jsonify({
        "tree": tree_json_relative,
        "default_unmarked": default_unmarked
    })

@app.route('/api/save_selection', methods=['POST'])
def save_selection():
    data = request.json or {}
    selected_paths = data.get('selectedPaths', [])
    print("Received selected file paths:", selected_paths)
    return jsonify({"status": "ok", "receivedCount": len(selected_paths)})

@app.route('/api/version', methods=['GET'])
def get_version():
    return jsonify({"version": server_start_time})

@app.route('/api/get_credentials', methods=['GET'])
def get_credentials():
    """
    Retrieve the saved credentials from ~/.atlaz
    """
    token_file = Path.home() / ".atlaz"
    if not token_file.exists():
        return jsonify({
            "api_key": "",
            "llm_provider": "openai",
            "model_choice": "gpt-4"
        }), 200  # Return defaults if file doesn't exist

    try:
        with token_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
        api_key = data.get("api_key", "")
        llm_provider = data.get("llm_provider", "openai")
        model_choice = data.get("model_choice", "gpt-4")
        return jsonify({
            "api_key": api_key,
            "llm_provider": llm_provider,
            "model_choice": model_choice
        }), 200
    except (json.JSONDecodeError, OSError) as e:
        logging.error(f"Error reading .atlaz file: {e}")
        return jsonify({
            "api_key": "",
            "llm_provider": "openai",
            "model_choice": "gpt-4"
        }), 500  # Return defaults on error