from pathlib import Path

from atlaz.frontend.livereload_server import start_dev_server

def frontend_main(script_path):
    atlaz_helper_dir = script_path.parent / ".atlaz_helper"
    original_dir = atlaz_helper_dir / "original"
    replacing_dir = atlaz_helper_dir / "replacing"
    created_dir = atlaz_helper_dir / "created"
    original_dir.mkdir(parents=True, exist_ok=True)
    replacing_dir.mkdir(parents=True, exist_ok=True)
    created_dir.mkdir(parents=True, exist_ok=True)
    frontend_dir = Path(__file__).parent.parent / 'frontend'
    files_json_path = frontend_dir / 'files.json'
    if files_json_path.exists():
        files_json_path.unlink()
    start_dev_server(port=8000)
    return replacing_dir, created_dir, original_dir, files_json_path
