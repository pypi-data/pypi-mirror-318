import logging
import json
import requests  # type: ignore
from pathlib import Path
import getpass

from atlaz.overview import atlaz_code
from atlaz.codeGen.schema import CodeGenRequest, CodeGenResponse

class Atlaz:
    def __init__(self, api_key: str, base_url: str = "https://atlaz-api.com"):
        self.api_key = api_key
        self.models = ["raspberry"]
        self.auth_token = None
        self.token_file = Path.home() / ".atlaz"
        self.base_url = base_url
        if self.token_file.exists():
            with self.token_file.open("r") as f:
                data = json.load(f)
                self.auth_token = data.get("auth_token")
        if not self.auth_token:
            self.authenticate()

    def _save_token(self, token: str):
        with self.token_file.open("w") as f:
            json.dump({"auth_token": token}, f)
        self.auth_token = token

    def authenticate(self):
        print("=== Welcome to Atlaz! ===")
        while True:
            choice = input("Do you want to (1) Login or (2) Create an account? Enter 1 or 2: ").strip()
            if choice == '1':
                login_flag = True
                print("=== Login ===")
                break
            elif choice == '2':
                login_flag = False
                print("=== Create an Account ===")
                break
            else:
                print("Invalid choice. Please enter 1 to Login or 2 to Create an account.")
        email = input("Enter your email: ")
        while True:
            password = getpass.getpass("Enter your password: ")
            if not login_flag:
                password_confirm = getpass.getpass("Confirm your password: ")
                if password != password_confirm:
                    print("Passwords do not match. Please try again.")
                    continue
            break
        login_url = f"{self.base_url}/models/login"
        payload = {"email": email, "password": password, "login": login_flag}
        try:
            response = requests.post(login_url, json=payload)
            if response.status_code == 200:
                data = response.json()
                persistent_token = data.get("persistent_token")
                if persistent_token:
                    self._save_token(persistent_token)
                if not login_flag:
                    print("Account created successfully. You are now logged in.")
                else:
                    print("Logged in successfully.")
            else:
                action = "login" if login_flag else "create an account"
                print(f"Failed to {action}. Status Code: {response.status_code}")
                try:
                    error_message = response.json().get("error", response.text)
                    print(f"Error: {error_message}")
                except json.JSONDecodeError:
                    print(f"Response: {response.text}")
        except requests.RequestException as e:
            logging.error(f"Request failed: {e}")
            print("An error occurred while trying to authenticate.")

    def list_models(self):
        return {"data": [{"id": model} for model in self.models]}

    def generate_code(
        self,
        script_path: Path,
        focus_dirs: list,
        instruction: str,
        manual_ignore_patterns: list = [],
        manual_ignore_files: list = [],
        model_choice: str = 'gpt-4o',
        provider: str = "openai"
    ):
        file_contents, directory_structure = atlaz_code(
            script_path,
            focus_dirs,
            manual_ignore_patterns=manual_ignore_patterns,
            manual_ignore_files=manual_ignore_files
        )
        if "raspberry" not in self.models:
            raise ValueError("Model 'raspberry' is not available.")
        if not self.auth_token:
            print("Re-authenticating...")
            self.authenticate()
            if not self.auth_token:
                print("Authentication failed.")
                return
        url = f"{self.base_url}/api/raspberry"
        payload = {
            "file_contents": file_contents,
            "directory_structure": directory_structure,
            "instruction": instruction,
            "api_key": self.api_key,
            "provider": provider,
            "model_choice": model_choice,
        }
        CodeGenRequest(**payload)
        headers = {"Authorization": f"Bearer {self.auth_token}", "Content-Type": "application/json"}
        atlaz_helper_dir = script_path.parent / ".atlaz_helper"
        original_dir = atlaz_helper_dir / "original"
        replacing_dir = atlaz_helper_dir / "replacing"
        created_dir = atlaz_helper_dir / "created"
        original_dir.mkdir(parents=True, exist_ok=True)
        replacing_dir.mkdir(parents=True, exist_ok=True)
        created_dir.mkdir(parents=True, exist_ok=True)
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
                    for file_item in final_response["response"]:
                        new_file_name = Path(file_item["name"]).name + ".txt"
                        new_file_content = file_item["content"]
                        if 'replacing' in file_item["name"]:
                            target_file = replacing_dir / new_file_name
                        elif 'created' in file_item["name"]:
                            target_file = created_dir / new_file_name
                        elif 'original' in file_item["name"]:
                            target_file = original_dir / new_file_name
                        with target_file.open("w", encoding="utf-8") as f_out:
                            f_out.write(new_file_content)
                    return final_response
                else:
                    raise ValueError("Server Error: Did not receive a 'completed' response.")
        except requests.RequestException as e:
            raise e