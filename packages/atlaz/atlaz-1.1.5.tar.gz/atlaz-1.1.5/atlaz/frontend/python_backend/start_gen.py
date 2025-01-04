from pathlib import Path
from atlaz.client import AtlazClient

def start_gen(data):
    api_key = data.get('api_key', '')
    api_key = 'AIzaSyCF0sTZ6iSBg3wJ9mePLTa3GP7tEwkCkPE'
    llm_model = data.get('llm_model', '')
    llm_provider = data.get('llm_provider', '')
    instruction = data.get('message', '')
    selected_files = data.get('selected_files', [])
    client = AtlazClient(api_key=api_key)
    script_path = Path(__file__).resolve()
    focus_directories = ['atlaz']
    manual_ignore_files = ['graph','files.json', 'directory_structure.json']
    print(f'{instruction=}')
    client.generate_code(script_path,focus_directories = focus_directories, manual_ignore_files=manual_ignore_files, instruction=instruction, model_choice = llm_model, provider = llm_provider)


