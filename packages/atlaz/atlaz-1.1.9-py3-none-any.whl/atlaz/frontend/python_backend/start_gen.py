from pathlib import Path
from atlaz.headquarter.client import AtlazClient

def start_gen(data):
    api_key = data.get('api_key', '')
    llm_model = data.get('llm_model', '')
    llm_provider = data.get('llm_provider', '')
    instruction = data.get('message', '')
    selected_files = data.get('selected_files', [])
    client = AtlazClient(api_key = api_key)

    # Now update the client’s credentials with the new values from the user
    client.set_credentials(api_key, llm_provider, llm_model)
    
    print(f'{instruction=}')
    client.generate_code_new(
        selected_files=selected_files,
        instruction=instruction,
        model_choice=llm_model,
        provider=llm_provider
    )