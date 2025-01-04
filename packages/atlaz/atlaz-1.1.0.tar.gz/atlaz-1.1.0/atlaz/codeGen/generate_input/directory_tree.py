from pathlib import Path
from typing import Any, Dict, List

def build_directory_tree(selected_files: List[str]) -> Dict[str, Any]:
    """
    Builds a nested directory tree from a list of file paths.

    Args:
        selected_files (List[str]): List of file paths.

    Returns:
        Dict[str, Any]: Nested dictionary representing the directory tree.
    """
    tree = {}
    for file_path in selected_files:
        parts = Path(file_path).parts
        current_level = tree
        for part in parts[:-1]:
            if part not in current_level:
                current_level[part] = {}
            elif not isinstance(current_level[part], dict):
                raise ValueError(f"Conflict at {part}: Expected a directory.")
            current_level = current_level[part]
        file_name = parts[-1]
        if file_name in current_level:
            if isinstance(current_level[file_name], dict):
                raise ValueError(f"Conflict at {file_name}: Expected a file.")
            continue
        current_level[file_name] = {}
    return tree