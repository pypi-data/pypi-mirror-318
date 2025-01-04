# File: codeGen/generate_input/file_loader.py
from typing import Any, Dict, List
from pathlib import Path
import logging
from pydantic import ValidationError

from atlaz.codeGen.schema import Files
from atlaz.codeGen.generate_input.bad_files import is_large_or_binary

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_files(selected_files: List[str]) -> List[Dict[str, Any]]:
    """
    Takes a list of file paths, reads their content, and returns a list of
    dictionaries conforming to the Pydantic `Files` schema.

    This function ensures that only non-binary files and files below a certain size
    are processed by utilizing the existing is_large_or_binary function.

    Args:
        selected_files (List[str]): List of file paths to load.

    Returns:
        List[Dict[str, Any]]: List of dictionaries, each adhering to the `Files` schema.
    """
    loaded_files = []
    for file_path_str in selected_files:
        file_path = Path(file_path_str)
        if not file_path.exists():
            logger.warning(f"File does not exist: {file_path}")
            continue
        if not file_path.is_file():
            logger.warning(f"Path is not a file: {file_path}")
            continue
        if is_large_or_binary(file_path):
            logger.warning(f"Skipping binary or large file: {file_path}")
            continue
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            logger.error(f"Failed to read file {file_path}: {e}")
            continue

        try:
            # Create the Pydantic model instance
            file_record = Files(name=file_path.name, content=content)
            # Convert to dict before appending to the list
            loaded_files.append(file_record.dict())
            logger.info(f"Loaded file: {file_path.name}")
        except ValidationError as ve:
            logger.error(f"Validation error for file {file_path}: {ve}")
            continue

    return loaded_files