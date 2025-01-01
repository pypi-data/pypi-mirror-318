import os
import io
from pathlib import Path
import pathspec  # type: ignore

def atlaz_code(script_path: str,
               focus_directories: list,
               max_size_mb: int = 5,
               max_lines: int = 20000,
               max_depth: int = 20,
               manual_ignore_patterns=None,
               manual_ignore_files=None) -> tuple[list[dict], str]:
    """
    Gathers an overview of files in the specified focus directories,
    writes it to an overview file, and returns two things:
      1) directory_data: A list of dictionaries, one for each directory:
           [
               {
                   "directory_name": "<focus_dir>",
                   "files": [
                       {"name": "<relative_path>", "content": "<file_content>"},
                       ...
                   ]
               },
               ...
           ]
      2) directory_structure: A string containing just the directory tree listing
         (excluding the '## Directory Tree:' heading).
    """
    base_path = script_path.parent
    output_path = base_path / 'atlaz'
    output_path.mkdir(parents=True, exist_ok=True)

    max_size_bytes = convert_mb_to_bytes(max_size_mb)
    overview_file_path = prepare_overview_file(output_path, focus_directories)
    ignore_spec = compile_ignore_patterns(base_path, manual_ignore_patterns)

    # Append default ignores
    manual_ignore_files = append_default_ignores(manual_ignore_files, overview_file_path.name)
    
    # Write the overview and collect data
    directory_data, directory_structure = write_overview(
        overview_file_path,
        focus_directories,
        max_size_bytes,
        max_lines,
        max_depth,
        ignore_spec,
        manual_ignore_files
    )

    return directory_data, directory_structure

def convert_mb_to_bytes(mb: int) -> int:
    return mb * 1024 * 1024

def prepare_overview_file(output_path: Path, focus_directories: list) -> Path:
    if len(focus_directories) == 1:
        overview_file_name = f"{focus_directories[0]}_OVERVIEW.txt"
    else:
        overview_file_name = f"{'_'.join(focus_directories)}_OVERVIEW.txt"
    return output_path / overview_file_name

def append_default_ignores(manual_ignore_files: list, overview_file_name: str) -> list:
    common_ignore_dirs = [
        '.git', 'node_modules', 'build', 'dist', '__pycache__', 'venv', '*.log',
        'node_modules/', '*.tmp', '.env'
    ]
    return (manual_ignore_files or []) + common_ignore_dirs + [overview_file_name]

def write_overview(
    overview_file_path: Path,
    focus_directories: list,
    max_size_bytes: int,
    max_lines: int,
    max_depth: int,
    ignore_spec,
    manual_ignore_files
) -> tuple[list[dict], str]:
    """
    Writes the project overview to `overview_file_path`.
    Returns:
      - directory_data: a list of { "directory_name": <focus_dir>, "files": [...] }
      - directory_structure: just the directory tree listing lines 
        (excluding the '## Directory Tree:' heading).
    """
    collected_directories = []

    with open(overview_file_path, 'w', encoding='utf-8') as overview_file:
        # 1) Write the main header (but not the "## Directory Tree:" lines)
        write_header(overview_file, focus_directories)

        # 2) Write "## Directory Tree:" explicitly to the file
        overview_file.write("## Directory Tree:\n\n")

        # Capture the directory tree listing (minus the heading) in a buffer
        directory_tree_buffer = io.StringIO()
        write_directory_tree(directory_tree_buffer, focus_directories, ignore_spec, manual_ignore_files, max_depth)
        directory_tree_text = directory_tree_buffer.getvalue()

        # Write that text to the file
        overview_file.write(directory_tree_text)

        # 3) Separate section for file contents
        overview_file.write("\n---\n\n## File Contents:\n\n")

        # Traverse each focus directory, collecting files
        for focus_dir in focus_directories:
            files_for_this_dir = []

            traverse_directories(
                overview_file,
                Path(focus_dir),
                max_size_bytes,
                max_lines,
                max_depth,
                ignore_spec,
                manual_ignore_files,
                overview_file_path,
                files_for_this_dir
            )

            dir_info = {
                "directory_name": focus_dir,
                "files": files_for_this_dir
            }
            collected_directories.append(dir_info)

    # We do not re-read the entire file content now (removed).
    return collected_directories, directory_tree_text

def write_directory_tree(
    out_stream,
    focus_dirs: list,
    ignore_spec,
    manual_ignore_files: list,
    max_depth: int
):
    """
    Writes only the directory tree portion to out_stream
    (no '## Directory Tree:' heading here, so the returned text 
    won't include those lines).
    """
    for focus_dir in focus_dirs:
        focus_path = Path(focus_dir)
        for root, dirs, files in os.walk(focus_path):
            root_path = Path(root)
            if skip_depth(root_path, focus_path, max_depth):
                continue
            dirs[:] = filter_dirs(root_path, dirs, ignore_spec, manual_ignore_files)
            files = filter_files(root_path, files, ignore_spec, manual_ignore_files)
            write_tree_structure(out_stream, root_path, files)

def write_header(overview_file, focus_directories: list):
    """
    Writes the main project overview header to the text file.
    """
    if len(focus_directories) == 1:
        project_name = focus_directories[0]
    else:
        project_name = ', '.join(focus_directories)
    overview_file.write(f"# Project Overview: {project_name}\n\n")
    overview_file.write("This document provides an overview of the project's directory structure and content.\n")
    overview_file.write("The directory tree is listed first, followed by the contents of each file, up to specified limits.\n\n")

def traverse_directories(
    overview_file,
    base_path: Path,
    max_size_bytes: int,
    max_lines: int,
    max_depth: int,
    ignore_spec,
    manual_ignore_files,
    overview_file_path: Path,
    collected_files: list
):
    """
    Walk through a single focus directory, write file info to the overview file,
    and append file data to 'collected_files'.
    """
    current_line_count = 0
    for root, dirs, files in os.walk(base_path):
        root_path = Path(root)
        if skip_depth(root_path, base_path, max_depth):
            continue
        dirs[:] = filter_dirs(root_path, dirs, ignore_spec, manual_ignore_files)
        files = filter_files(root_path, files, ignore_spec, manual_ignore_files)

        current_line_count = process_files(
            overview_file,
            root_path,
            files,
            base_path,
            max_size_bytes,
            max_lines,
            current_line_count,
            overview_file_path,
            collected_files
        )

        if current_line_count >= max_lines:
            break

def skip_depth(root_path: Path, base_path: Path, max_depth: int) -> bool:
    """
    Checks if the directory depth is beyond the specified max_depth.
    """
    return len(root_path.relative_to(base_path).parts) > max_depth

def filter_dirs(root_path: Path, dirs: list, ignore_spec, manual_ignore_files: list) -> list:
    return [d for d in dirs if not is_ignored_file(root_path / d, ignore_spec, manual_ignore_files)]

def filter_files(root_path: Path, files: list, ignore_spec, manual_ignore_files: list) -> list:
    return [f for f in files if not is_ignored_file(root_path / f, ignore_spec, manual_ignore_files)]

def process_files(
    overview_file,
    root_path: Path,
    files: list,
    base_path: Path,
    max_size_bytes: int,
    max_lines: int,
    current_line_count: int,
    overview_file_path: Path,
    collected_files: list
) -> int:
    """
    Writes file headers and either indicates skipping or reads content, 
    appending results to 'collected_files'.
    """
    for file_name in files:
        file_path = root_path / file_name

        # Skip if it's the overview file itself
        if skip_overview_file(file_path, overview_file_path):
            continue

        # Write file header in the overview
        current_line_count += write_file_header(overview_file, file_path, base_path)

        # Check if the file is large or binary
        if is_large_or_binary(file_path):
            overview_file.write(
                f"```\n*** Skipping large or binary file (Size: {file_path.stat().st_size / 1024:.2f} KB) ***\n```\n"
            )
            current_line_count += 2
        else:
            # Write data to overview and collect it at the same time
            new_count, file_content = write_file_data_and_collect(
                overview_file,
                file_path,
                max_size_bytes,
                max_lines,
                current_line_count
            )
            current_line_count = new_count

            # Add to the list for this directory
            collected_files.append({
                "name": str(file_path.relative_to(base_path)),
                "content": file_content
            })

        if current_line_count >= max_lines:
            break

    return current_line_count

def skip_overview_file(file_path: Path, overview_file_path: Path) -> bool:
    return file_path == overview_file_path

def write_file_header(overview_file, file_path: Path, base_path: Path) -> int:
    """
    Writes a header line for the file in the overview.
    Returns how many lines were written (here, 2).
    """
    overview_file.write(f"\n#### File: `{file_path.relative_to(base_path)}`\n")
    return 2

def write_file_data_and_collect(
    overview_file,
    file_path: Path,
    max_size_bytes: int,
    max_lines: int,
    current_line_count: int
) -> tuple[int, str]:
    """
    Reads the file line by line, writes it to the overview file, 
    and collects the file content in a string. Returns:
      - The new line count after writing
      - The collected file content
    """
    overview_file.write("```\n")
    file_content_lines = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                overview_file.write(line)
                file_content_lines.append(line)
                current_line_count += 1

                # Stop if limits are reached
                if is_limit_reached(overview_file, current_line_count, max_size_bytes, max_lines):
                    break
    except Exception as e:
        err_msg = f"Could not read file: {e}\n"
        overview_file.write(err_msg)
        file_content_lines.append(err_msg)
        current_line_count += 1

    overview_file.write("\n```\n")

    # +1 for the trailing backticks line
    return current_line_count + 1, "".join(file_content_lines)

def is_large_or_binary(file_path: Path) -> bool:
    """
    Returns True if the file is likely binary or if it's larger than 1 MB.
    Adjust size logic as needed.
    """
    one_mb_in_bytes = 1024 * 1024

    if is_binary(file_path):
        return True
    if file_path.stat().st_size > one_mb_in_bytes:
        return True
    return False

def is_binary(file_path: Path) -> bool:
    """
    A simple check for binary content by scanning the first 1024 bytes for null bytes.
    """
    try:
        with open(file_path, 'rb') as file:
            return b'\0' in file.read(1024)
    except Exception:
        # If we can't read it, treat it as binary
        return True

def is_limit_reached(overview_file, current_line_count: int, max_size_bytes: int, max_lines: int) -> bool:
    """
    Checks if either the total bytes in the overview or the line count
    have exceeded their respective limits.
    """
    return (overview_file.tell() > max_size_bytes) or (current_line_count >= max_lines)

def compile_ignore_patterns(base_path: Path, manual_patterns: list):
    """
    Load .gitignore patterns plus any manual_patterns, compile them into a PathSpec.
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
        with open(gitignore_path, 'r') as f:
            return f.readlines()
    return []

def is_ignored_file(file_path: Path, ignore_spec, manual_ignore_files: list) -> bool:
    """
    Returns True if file_path is matched by ignore_spec or is explicitly
    in manual_ignore_files.
    """
    # For pathspec matching, convert path to a posix string relative 
    # to the drive root (file_path.anchor).
    if ignore_spec and ignore_spec.match_file(file_path.relative_to(file_path.anchor).as_posix()):
        return True
    if manual_ignore_files and file_path.name in manual_ignore_files:
        return True
    return False

def write_tree_structure(out_stream, root_path: Path, files: list):
    """
    Writes a simple tree structure for the given directory (root_path) and file list
    to the provided out_stream (could be a file or StringIO).
    """
    depth = len(root_path.parts) - 1
    indent = '    ' * depth
    out_stream.write(f"{indent}├── {root_path.name}\n")
    for file_name in files:
        file_indent = '    ' * (depth + 1) + '└── '
        out_stream.write(f"{file_indent}{file_name}\n")

if __name__ == "__main__":
    script_path = Path(__file__).resolve()
    focus_dirs = ['atlaz', 'dist']
    manual_ignore_patterns = ['*.log', 'node_modules/', '*.tmp']
    manual_ignore_files = []
    directory_data, directory_structure = atlaz_code(
        script_path,
        focus_dirs,
        manual_ignore_patterns=manual_ignore_patterns,
        manual_ignore_files=manual_ignore_files
    )
    print("=== Directory Tree Only (directory_structure) ===")
    print(directory_structure)
    print("\n=== Directory Data ===")
    for dir_entry in directory_data:
        print(f"Directory: {dir_entry['directory_name']}")
        for file_info in dir_entry['files']:
            print(f"  File name: {file_info['name']}")
            print(f"  Content:\n{file_info['content']}")
            print("-----")
        print("========")