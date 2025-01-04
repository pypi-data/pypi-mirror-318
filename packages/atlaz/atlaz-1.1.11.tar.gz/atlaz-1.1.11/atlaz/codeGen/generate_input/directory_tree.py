from pathlib import Path
from typing import Any, Dict, List


from pathlib import Path
from typing import List, Dict, Any

def build_directory_tree_string(selected_files: List[str]) -> str:
    """
    Builds a directory tree string from a list of file and directory paths.

    Args:
        selected_files (List[str]): List of file and directory paths.

    Returns:
        str: Formatted string representing the directory tree.

    Raises:
        ValueError: If a conflict is detected where a file is treated as a directory or vice versa.
    """
    tree = {}
    directories = set()
    files = set()

    # Step 1: Separate directories and files
    for file_path in selected_files:
        path = Path(file_path)
        if file_path.endswith('/'):
            # It's a directory; remove trailing '/'
            directories.add(path.as_posix().rstrip('/'))
        else:
            # It's a file; add to files set
            files.add(path.as_posix())

    # Step 2: Add parent directories of files to directories set
    for file_path in files:
        path = Path(file_path)
        for parent in path.parents:
            if parent == Path('/'):
                continue  # Skip the root
            directories.add(parent.as_posix())

    # Step 3: Detect conflicts where a path is both a file and a directory
    conflicting_paths = directories.intersection(files)
    if conflicting_paths:
        conflict_path = conflicting_paths.pop()
        conflicting_part = Path(conflict_path).name
        raise ValueError(f"Conflict at '{conflicting_part}': Path is both a file and a directory.")

    # Step 4: Build the tree structure by processing directories first
    sorted_directories = sorted(directories, key=lambda x: x.count('/'))
    for dir_path in sorted_directories:
        path = Path(dir_path)
        parts = path.parts
        current_level = tree
        for part in parts:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]

    # Step 5: Add files to the tree
    for file_path in sorted(files):
        path = Path(file_path)
        parts = path.parts
        current_level = tree
        for part in parts[:-1]:
            current_level = current_level[part]
        file_name = parts[-1]
        current_level[file_name] = None  # Represent files as None

    lines = []
    def traverse(current_dict: Dict[str, Any], prefix: str = ""):
        # Sort directories first, then files, both alphabetically
        dirs = sorted([k for k, v in current_dict.items() if isinstance(v, dict)], key=lambda x: x.lower())
        files_sorted = sorted([k for k, v in current_dict.items() if v is None], key=lambda x: x.lower())
        sorted_keys = dirs + files_sorted
        total_items = len(sorted_keys)
        for idx, key in enumerate(sorted_keys):
            is_last = idx == total_items - 1
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{key}")
            if isinstance(current_dict[key], dict):
                extension = "    " if is_last else "│   "
                traverse(current_dict[key], prefix + extension)
    traverse(tree)
    return "\n".join(lines)