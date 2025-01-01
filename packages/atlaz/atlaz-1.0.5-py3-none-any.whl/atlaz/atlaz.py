from pathlib import Path
from atlaz.overview import atlaz_code # type: ignore

def main():
    script_path = Path(__file__).resolve().parent
    focus_dirs = ['atlaz', 'dist']
    manual_ignore_patterns = ['*.log', 'node_modules/', '*.tmp']
    manual_ignore_files = []
    atlaz_code(script_path, focus_dirs, manual_ignore_patterns=manual_ignore_patterns, manual_ignore_files=manual_ignore_files)

if __name__ == "__main__":
    main()