import os
import io
from pathlib import Path
import pathspec  # type: ignore

def atlaz_code(script_path: Path,
               focus_directories: list,
               max_size_mb: int = 5,
               max_lines: int = 20000,
               max_depth: int = 20,
               manual_ignore_patterns=None,
               manual_ignore_files=None) -> tuple[list[dict], str]:
    """
    Scans the specified focus directories (relative to script_path.parent), 
    and returns:

      1) directory_data: A single list of dictionaries, each with
         {"name": "...", "content": "..."} where "name" includes the focus
         directory in its path. Example:
             [
                 {"name": "atlaz/some_file.py", "content": "..."},
                 {"name": "dist/index.html",   "content": "..."},
                 ...
             ]

      2) directory_structure: A string of the directory tree lines (e.g. lines
         with '├── ...'), excluding any heading.

    No data is written to disk. Large/binary/ignored files are skipped.
    """
    base_path = script_path.parent

    # Convert MB to bytes for size-limiting
    max_size_bytes = max_size_mb * 1024 * 1024

    # Compile ignore patterns from .gitignore + manual patterns
    ignore_spec = compile_ignore_patterns(base_path, manual_ignore_patterns)

    # Combine default ignores with user-provided manual_ignore_files
    manual_ignore_files = append_default_ignores(manual_ignore_files)

    # 1) Build the directory tree (in-memory, no heading)
    directory_structure = gather_directory_tree(
        focus_directories, ignore_spec, manual_ignore_files, max_depth
    )

    # 2) Gather all files from all focus dirs into a single list
    directory_data = []
    current_line_count = 0

    for focus_dir in focus_directories:
        focus_path = Path(focus_dir)

        for root, dirs, files in os.walk(focus_path):
            root_path = Path(root)
            if skip_depth(root_path, focus_path, max_depth):
                continue

            dirs[:] = filter_dirs(root_path, dirs, ignore_spec, manual_ignore_files)
            files = filter_files(root_path, files, ignore_spec, manual_ignore_files)

            for file_name in files:
                file_path = root_path / file_name

                # If it's large or binary, skip
                if is_large_or_binary(file_path):
                    continue

                # Read file content within the specified line/size limits
                new_line_count, file_content = read_file_data(
                    file_path, max_size_bytes, max_lines, current_line_count
                )
                current_line_count = new_line_count

                # Construct a name that includes the focus directory
                # e.g. "atlaz/some_subdir/foo.py"
                relative_to_focus = file_path.relative_to(focus_path).as_posix()
                full_name = f"{focus_dir}/{relative_to_focus}"

                directory_data.append({
                    "name": full_name,
                    "content": file_content
                })

                # If we've hit the max line limit, stop collecting
                if current_line_count >= max_lines:
                    break

            if current_line_count >= max_lines:
                break

    return directory_data, directory_structure

# --------------------------------------------------------------------
# Supporting Functions
# --------------------------------------------------------------------

def append_default_ignores(manual_ignore_files: list) -> list:
    """
    Add common ignore directories and patterns if they're not already present.
    """
    common_ignores = [
        '.git', 'node_modules', 'build', 'dist', '__pycache__',
        'venv', '*.log', 'node_modules/', '*.tmp', '.env'
    ]
    if not manual_ignore_files:
        manual_ignore_files = []
    for pattern in common_ignores:
        if pattern not in manual_ignore_files:
            manual_ignore_files.append(pattern)
    return manual_ignore_files

def compile_ignore_patterns(base_path: Path, manual_patterns: list):
    """
    Load .gitignore patterns plus any manual_patterns, compile into a PathSpec.
    """
    gitignore_patterns = load_gitignore_patterns(base_path)
    all_patterns = gitignore_patterns + (manual_patterns or [])
    if all_patterns:
        return pathspec.PathSpec.from_lines('gitwildmatch', all_patterns)
    return None

def load_gitignore_patterns(base_path: Path) -> list:
    """
    Reads the .gitignore (if present) and returns the patterns.
    """
    gitignore_path = base_path / '.gitignore'
    if gitignore_path.exists():
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            return f.readlines()
    return []

def gather_directory_tree(
    focus_dirs: list,
    ignore_spec,
    manual_ignore_files: list,
    max_depth: int
) -> str:
    """
    Recursively walks the given focus directories, builds a textual
    tree (e.g. lines with '├── ...'), and returns the entire tree
    as a single string. Skips ignored directories and files, as well
    as directories beyond max_depth.
    """
    buffer = io.StringIO()
    for focus_dir in focus_dirs:
        focus_path = Path(focus_dir)
        for root, dirs, files in os.walk(focus_path):
            root_path = Path(root)
            if skip_depth(root_path, focus_path, max_depth):
                continue
            dirs[:] = filter_dirs(root_path, dirs, ignore_spec, manual_ignore_files)
            files = filter_files(root_path, files, ignore_spec, manual_ignore_files)
            write_tree_structure(buffer, root_path, files)
    return buffer.getvalue()

def skip_depth(root_path: Path, base_path: Path, max_depth: int) -> bool:
    """
    Returns True if root_path is deeper than max_depth relative to base_path.
    """
    return len(root_path.relative_to(base_path).parts) > max_depth

def filter_dirs(root_path: Path, dirs: list, ignore_spec, manual_ignore_files: list) -> list:
    """
    Removes directories from 'dirs' if they match ignore patterns or
    are in manual_ignore_files.
    """
    return [d for d in dirs if not is_ignored_file(root_path / d, ignore_spec, manual_ignore_files)]

def filter_files(root_path: Path, files: list, ignore_spec, manual_ignore_files: list) -> list:
    """
    Removes files from 'files' if they match ignore patterns or
    are in manual_ignore_files.
    """
    return [f for f in files if not is_ignored_file(root_path / f, ignore_spec, manual_ignore_files)]

def is_ignored_file(file_path: Path, ignore_spec, manual_ignore_files: list) -> bool:
    """
    Returns True if file_path is matched by ignore_spec or is explicitly
    in manual_ignore_files.
    """
    # Convert path to a posix string relative to the drive root (file_path.anchor).
    if ignore_spec and ignore_spec.match_file(file_path.relative_to(file_path.anchor).as_posix()):
        return True
    if manual_ignore_files and file_path.name in manual_ignore_files:
        return True
    return False

def is_large_or_binary(file_path: Path) -> bool:
    """
    Returns True if the file is likely binary or if it's larger than 1 MB.
    """
    one_mb_in_bytes = 1024 * 1024
    if file_path.exists():
        if file_path.stat().st_size > one_mb_in_bytes:
            return True
        if is_binary(file_path):
            return True
    return False

def is_binary(file_path: Path) -> bool:
    """
    A simple check for binary content by scanning the first 1024 bytes for null bytes.
    """
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            return b'\0' in chunk
    except Exception:
        # If we can't read it, treat it as binary/unreadable
        return True

def read_file_data(
    file_path: Path,
    max_size_bytes: int,
    max_lines: int,
    current_line_count: int
) -> tuple[int, str]:
    """
    Reads the file up to max_lines or until total read content
    would exceed max_size_bytes. Returns:
      - new_line_count after reading
      - the actual file text (which may be truncated if we hit a limit)
    """
    file_content_lines = []
    total_bytes = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                current_line_count += 1
                total_bytes += len(line.encode('utf-8'))

                if (total_bytes > max_size_bytes) or (current_line_count >= max_lines):
                    break
                file_content_lines.append(line)

    except Exception as e:
        file_content_lines.append(f"Could not read file: {e}\n")
        current_line_count += 1

    file_text = "".join(file_content_lines)
    return current_line_count, file_text

def write_tree_structure(out_stream, root_path: Path, files: list):
    """
    Writes a simple tree structure (lines with '├── ...') for the given
    directory (root_path) and file list to out_stream (a StringIO).
    """
    depth = len(root_path.parts) - 1
    indent = '    ' * depth
    out_stream.write(f"{indent}├── {root_path.name}\n")
    for file_name in files:
        file_indent = '    ' * (depth + 1) + '└── '
        out_stream.write(f"{file_indent}{file_name}\n")