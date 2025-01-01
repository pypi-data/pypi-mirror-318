import os
from pathlib import Path
import pathspec # type: ignore

def atlaz_code(script_path: str, focus_directories: list, max_size_mb: int = 5, max_lines: int = 20000, max_depth: int = 20, manual_ignore_patterns=None, manual_ignore_files=None):
    base_path = script_path.parent
    output_path = base_path / 'atlaz'
    output_path.mkdir(parents=True, exist_ok=True)
    max_size_bytes = convert_mb_to_bytes(max_size_mb)
    overview_file_path = prepare_overview_file(output_path, focus_directories)
    ignore_spec = compile_ignore_patterns(base_path, manual_ignore_patterns)
    manual_ignore_files = append_default_ignores(manual_ignore_files, overview_file_path.name)
    write_overview(overview_file_path, focus_directories, max_size_bytes, max_lines, max_depth, ignore_spec, manual_ignore_files)

def convert_mb_to_bytes(mb: int) -> int:
    return mb * 1024 * 1024

def prepare_overview_file(output_path: Path, focus_directories: list) -> Path:
    if len(focus_directories) == 1:
        overview_file_name = f"{focus_directories[0]}_OVERVIEW.txt"
    else:
        overview_file_name = f"{'_'.join(focus_directories)}_OVERVIEW.txt"
    return output_path / overview_file_name

def append_default_ignores(manual_ignore_files: list, overview_file_name: str) -> list:
    common_ignore_dirs = ['.git', 'node_modules', 'build', 'dist', '__pycache__', 'venv', '*.log', 'node_modules/', '*.tmp']
    return (manual_ignore_files or []) + common_ignore_dirs + [overview_file_name]

def write_overview(overview_file_path: Path, focus_directories: list, max_size_bytes: int, max_lines: int, max_depth: int, ignore_spec, manual_ignore_files):
    with open(overview_file_path, 'w', encoding='utf-8') as overview_file:
        write_header(overview_file, focus_directories)
        write_directory_tree(overview_file, focus_directories, ignore_spec, manual_ignore_files, max_depth)
        overview_file.write("\n---\n\n## File Contents:\n\n")
        for focus_dir in focus_directories:
            traverse_directories(overview_file, Path(focus_dir), max_size_bytes, max_lines, max_depth, ignore_spec, manual_ignore_files, overview_file_path)

def write_directory_tree(overview_file, focus_dirs: list, ignore_spec, manual_ignore_files: list, max_depth: int):
    for focus_dir in focus_dirs:
        focus_path = Path(focus_dir)
        for root, dirs, files in os.walk(focus_path):
            root_path = Path(root)
            if skip_depth(root_path, focus_path, max_depth): 
                continue
            dirs[:] = filter_dirs(root_path, dirs, ignore_spec, manual_ignore_files)
            files = filter_files(root_path, files, ignore_spec, manual_ignore_files)
            write_tree_structure(overview_file, root_path, files)

def write_header(overview_file, focus_directories: list):
    if len(focus_directories) == 1:
        project_name = focus_directories[0]
    else:
        project_name = ', '.join(focus_directories)
    overview_file.write(f"# Project Overview: {project_name}\n\n")
    overview_file.write("This document provides an overview of the project's directory structure and content.\n")
    overview_file.write("The directory tree is listed first, followed by the contents of each file, up to specified limits.\n\n")
    overview_file.write("---\n\n## Directory Tree:\n\n")

def traverse_directories(overview_file, base_path: Path, max_size_bytes: int, max_lines: int, max_depth: int, ignore_spec, manual_ignore_files, overview_file_path: Path):
    current_line_count = 0
    for root, dirs, files in os.walk(base_path):
        root_path = Path(root)
        if skip_depth(root_path, base_path, max_depth): continue
        dirs[:] = filter_dirs(root_path, dirs, ignore_spec, manual_ignore_files)
        files = filter_files(root_path, files, ignore_spec, manual_ignore_files)
        current_line_count = process_files(overview_file, root_path, files, base_path, max_size_bytes, max_lines, current_line_count, overview_file_path)
        if current_line_count >= max_lines: break

def skip_depth(root_path: Path, base_path: Path, max_depth: int) -> bool:
    return len(root_path.relative_to(base_path).parts) > max_depth

def filter_dirs(root_path: Path, dirs: list, ignore_spec, manual_ignore_files: list) -> list:
    return [d for d in dirs if not is_ignored_file(root_path / d, ignore_spec, manual_ignore_files)]

def filter_files(root_path: Path, files: list, ignore_spec, manual_ignore_files: list) -> list:
    return [f for f in files if not is_ignored_file(root_path / f, ignore_spec, manual_ignore_files)]

def process_files(overview_file, root_path: Path, files: list, base_path: Path, max_size_bytes: int, max_lines: int, current_line_count: int, overview_file_path: Path) -> int:
    for file_name in files:
        file_path = root_path / file_name
        if skip_overview_file(file_path, overview_file_path): continue
        current_line_count += write_file_header(overview_file, file_path, base_path)
        current_line_count = write_file_data(overview_file, file_path, max_size_bytes, max_lines, current_line_count)
        if current_line_count >= max_lines: break
    return current_line_count

def skip_overview_file(file_path: Path, overview_file_path: Path) -> bool:
    return file_path == overview_file_path

def write_file_header(overview_file, file_path: Path, base_path: Path) -> int:
    overview_file.write(f"\n#### File: `{file_path.relative_to(base_path)}`\n")
    return 2

def write_file_data(overview_file, file_path: Path, max_size_bytes: int, max_lines: int, current_line_count: int) -> int:
    if is_large_or_binary(file_path):
        overview_file.write(f"```\n*** Skipping large or binary file (Size: {file_path.stat().st_size / 1024:.2f} KB) ***\n```\n")
        return current_line_count + 2
    return write_file_content(overview_file, file_path, current_line_count, max_size_bytes, max_lines)

def is_large_or_binary(file_path: Path) -> bool:
    return is_binary(file_path) or file_path.stat().st_size > 1024 * 1024

def write_file_content(overview_file, file_path: Path, current_line_count: int, max_size_bytes: int, max_lines: int) -> int:
    overview_file.write("```\n")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                overview_file.write(line)
                current_line_count += 1
                if is_limit_reached(overview_file, current_line_count, max_size_bytes, max_lines): break
    except Exception as e:
        overview_file.write(f"Could not read file: {e}\n")
        current_line_count += 1
    overview_file.write("```\n")
    return current_line_count + 1

def is_limit_reached(overview_file, current_line_count: int, max_size_bytes: int, max_lines: int) -> bool:
    return overview_file.tell() > max_size_bytes or current_line_count >= max_lines

def compile_ignore_patterns(base_path: Path, manual_patterns: list):
    gitignore_patterns = load_gitignore_patterns(base_path)
    return pathspec.PathSpec.from_lines('gitwildmatch', gitignore_patterns + (manual_patterns or [])) if gitignore_patterns else None

def load_gitignore_patterns(base_path: Path) -> list:
    gitignore_path = base_path / '.gitignore'
    if gitignore_path.exists():
        with open(gitignore_path, 'r') as f:
            return f.readlines()
    return []

def is_ignored_file(file_path: Path, ignore_spec, manual_ignore_files: list) -> bool:
    return (ignore_spec and ignore_spec.match_file(file_path.relative_to(file_path.anchor).as_posix())) or (manual_ignore_files and file_path.name in manual_ignore_files)

def is_binary(file_path: Path) -> bool:
    try:
        with open(file_path, 'rb') as file:
            return b'\0' in file.read(1024)
    except Exception:
        return True

def write_tree_structure(overview_file, root_path: Path, files: list):
    depth = len(root_path.parts) - 1
    indent = '    ' * depth
    overview_file.write(f"{indent}├── {root_path.name}\n")
    for file_name in files:
        file_indent = '    ' * (depth + 1) + '└── '
        overview_file.write(f"{file_indent}{file_name}\n")

if __name__ == "__main__":
    script_path = Path(__file__).resolve()
    focus_dirs = ['atlaz', 'dist']
    manual_ignore_patterns = ['*.log', 'node_modules/', '*.tmp']
    manual_ignore_files = []
    atlaz_code(focus_dirs, manual_ignore_patterns=manual_ignore_patterns, manual_ignore_files=manual_ignore_files)