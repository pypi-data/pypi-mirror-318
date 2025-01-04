import json
import os
from pathlib import Path
import tiktoken # type: ignore

def count_tokens(string_inp):
    encc = tiktoken.encoding_for_model("gpt-4")
    encoded_str = encc.encode(string_inp)
    return len(encoded_str)

def read_txt(file_input):
    with open(file_input, 'r') as file:
        data = file.read()
    return data

def write_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_json(json_name):
    with open(json_name, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def write_txt(string, filename):
    with open(filename, 'w') as f:
        f.write(string)


def build_directory_tree_json(root_path: Path, ignore=None, max_depth=20, level=0):
    """
    Recursively build a nested JSON representation of the directory tree.
    Each node will have:
      {
          "name": <str>,
          "type": "directory" or "file",
          "path": <full_or_relative_path>,
          "children": [...]
      }
    """
    if ignore is None:
        ignore = set()

    # If we've exceeded max depth, stop here
    if level > max_depth:
        return []

    items = []
    try:
        for entry in sorted(os.scandir(root_path), key=lambda e: e.name.lower()):
            # Skip ignored files/directories
            if entry.name in ignore or entry.name.startswith('.'):
                continue
            # Build a dictionary node
            entry_path = Path(entry.path)
            if entry.is_dir():
                items.append({
                    "name": entry.name,
                    "type": "directory",
                    "path": str(entry_path),
                    "children": build_directory_tree_json(
                        entry_path,
                        ignore=ignore,
                        max_depth=max_depth,
                        level=level + 1
                    )
                })
            else:
                items.append({
                    "name": entry.name,
                    "type": "file",
                    "path": str(entry_path)
                })
    except PermissionError:
        # If you don't have permission to read a folder, skip it
        pass

    return items