import logging
import json
from typing import List
import requests  # type: ignore
from pathlib import Path
import getpass

from atlaz.codeGen.code_gen import code_gen_handler
from atlaz.graph.graph import build_graph_handler
from atlaz.old_overview.main_overview import gather_repository
from atlaz.frontend.main_frontend import frontend_main
from atlaz.frontend.livereload_server import start_dev_server
from atlaz.codeGen.schema import Files

class AtlazClient:
    def __init__(self, api_key: str = 'No API key yet', base_url: str = "https://atlaz-api.com"):
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
        instruction: str,
        focus_directories: list = [],
        manual_ignore_patterns: list = [],
        manual_ignore_files: list = [],
        model_choice: str = 'gpt-4o',
        provider: str = "openai"
        ):
        file_contents, directory_structure = gather_repository(
            script_path,
            focus_directories=focus_directories,
            manual_ignore_patterns=manual_ignore_patterns,
            manual_ignore_files=manual_ignore_files)
        if not self.auth_token:
            print("Re-authenticating...")
            self.authenticate()
            if not self.auth_token:
                print("Authentication failed.")
                return
        code_gen_handler(self, script_path=script_path, instruction=instruction, directory_structure=directory_structure, file_contents = file_contents, model_choice=model_choice, provider=provider)

    def build_graph(self, source_text: str, customization: str = '', graph: dict= None):
        return build_graph_handler(self, source_text, customization, graph)
    
    def start_frontend(self):
        if not self.auth_token:
            print("Re-authenticating...")
            self.authenticate()
            if not self.auth_token:
                print("Authentication failed.")
                return
        frontend_main()
        try:
            while True:
                pass  # spin forever
        except KeyboardInterrupt:
            print("Shutting down.")

    """  def generate_code_new(
        self,
        script_path: Path,
        instruction: str,
        structured_input: List[Files],
        model_choice: str = 'gpt-4o',
        provider: str = "openai"
        ):

        if not self.auth_token:
            print("Re-authenticating...")
            self.authenticate()
            if not self.auth_token:
                print("Authentication failed.")
                return
        #code_gen_handler(self, script_path=script_path, instruction=instruction, directory_structure=directory_structure, file_contents = file_contents, model_choice=model_choice, provider=provider)
"""