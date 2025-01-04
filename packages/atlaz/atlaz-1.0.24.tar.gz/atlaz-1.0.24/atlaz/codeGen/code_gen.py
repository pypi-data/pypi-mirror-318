import logging
import json
import os
import requests  # type: ignore
from pathlib import Path

from atlaz.codeGen.schema import CodeGenRequest, CodeGenResponse
from atlaz.frontend.livereload_server import start_dev_server
from atlaz.frontend.main_frontend import frontend_main

def code_gen_handler(client,
    script_path: Path,
    instruction: str,
    directory_structure: str,
    file_contents: list = [],
    model_choice: str = 'gpt-4o',
    provider: str = "openai"
    ):
    url = f"{client.base_url}/api/raspberry"
    payload = {
        "file_contents": file_contents,
        "directory_structure": directory_structure,
        "instruction": instruction,
        "api_key": client.api_key,
        "provider": provider,
        "model_choice": model_choice,
    }
    CodeGenRequest(**payload)
    headers = {"Authorization": f"Bearer {client.auth_token}", "Content-Type": "application/json"}
    replacing_dir, created_dir, original_dir, files_json_path = frontend_main(script_path)
    """atlaz_helper_dir = script_path.parent / ".atlaz_helper"
    original_dir = atlaz_helper_dir / "original"
    replacing_dir = atlaz_helper_dir / "replacing"
    created_dir = atlaz_helper_dir / "created"
    original_dir.mkdir(parents=True, exist_ok=True)
    replacing_dir.mkdir(parents=True, exist_ok=True)
    created_dir.mkdir(parents=True, exist_ok=True)
    frontend_dir = Path(__file__).parent.parent / 'frontend'
    files_json_path = frontend_dir / 'files.json'
    if files_json_path.exists():
        files_json_path.unlink()
    start_dev_server(port=8000)"""
    try:
        with requests.post(url, json=payload, headers=headers, stream=True) as response:
            response.raise_for_status()
            final_response = None
            for line in response.iter_lines():
                if line:
                    try:
                        decoded_line = line.decode("utf-8").strip()
                        if not decoded_line:
                            continue
                        data = json.loads(decoded_line)
                        CodeGenResponse(**data)
                        status = data.get("status")
                        if status == "completed":
                            final_response = data
                            break
                    except json.JSONDecodeError as e:
                        logging.error("Failed to parse JSON line: %s", e)
                        logging.debug("Line content: %s", decoded_line)
            if final_response and final_response.get("response"):
                files_to_serve = []
                for file_item in final_response["response"]:
                    new_file_name = Path(file_item["name"]).name + ".txt"
                    new_file_content = file_item["content"]
                    file_info = {"name": new_file_name, "content": new_file_content}
                    full_file_path = file_item["name"]
                    if file_item["name"].startswith('replacing-'):
                        target_file = replacing_dir / new_file_name
                        file_info['type'] = 'replacing'
                    elif file_item["name"].startswith('created-'):
                        target_file = created_dir / new_file_name
                        file_info['type'] = 'created'
                    elif file_item["name"].startswith('original-'):
                        target_file = original_dir / new_file_name
                        file_info['type'] = 'original'
                    file_info['full_name'] = full_file_path
                    with target_file.open("w", encoding="utf-8") as f_out:
                        f_out.write(new_file_content)
                    files_to_serve.append(file_info)
                with files_json_path.open("w", encoding="utf-8") as f_json:
                    json.dump(files_to_serve, f_json)
                print("Files generated. Press Ctrl+C to stop the server.")
                try:
                    while True:
                        pass  # spin forever
                except KeyboardInterrupt:
                    print("Shutting down.")
                return final_response
            else:
                raise ValueError("Server Error: Did not receive a 'completed' response.")
    except requests.RequestException as e:
        raise e