import unittest
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
    for file_path in selected_files:
        path = Path(file_path).relative_to(Path(file_path).anchor)
        parts = path.parts
        current_level = tree
        for idx, part in enumerate(parts):
            is_file = idx == len(parts) - 1 and not file_path.endswith('/')
            if part not in current_level:
                current_level[part] = {} if not is_file else None
            else:
                if is_file:
                    if isinstance(current_level[part], dict):
                        raise ValueError(f"Conflict at '{part}': Expected a file but found a directory.")
                else:
                    if current_level[part] is None:
                        raise ValueError(f"Conflict at '{part}': Expected a directory but found a file.")
            current_level = current_level[part] if current_level[part] is not None else {}
    lines = []
    def traverse(current_dict: Dict[str, Any], prefix: str = ""):
        total_items = len(current_dict)
        sorted_items = sorted(current_dict.items(), key=lambda x: (x[0].lower()))
        for idx, (key, subtree) in enumerate(sorted_items):
            is_last = idx == total_items - 1
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{key}")
            if isinstance(subtree, dict):
                extension = "    " if is_last else "│   "
                traverse(subtree, prefix + extension)
    traverse(tree)
    return "\n".join(lines)


### **Unit Tests**

class TestBuildDirectoryTreeString(unittest.TestCase):
    def test_empty_list(self):
        selected_files = []
        expected = ""
        self.assertEqual(build_directory_tree_string(selected_files), expected)

    def test_single_file(self):
        selected_files = ["file.txt"]
        expected = "└── file.txt"
        self.assertEqual(build_directory_tree_string(selected_files), expected)

    def test_multiple_files_same_directory(self):
        selected_files = ["dir1/file1.txt", "dir1/file2.txt"]
        expected = (
            "└── dir1\n"
            "    ├── file1.txt\n"
            "    └── file2.txt"
        )
        self.assertEqual(build_directory_tree_string(selected_files), expected)

    def test_nested_directories(self):
        selected_files = [
            "dir1/dir2/file1.txt",
            "dir1/dir2/file2.txt",
            "dir1/dir3/file3.txt"
        ]
        expected = (
            "└── dir1\n"
            "    ├── dir2\n"
            "    │   ├── file1.txt\n"
            "    │   └── file2.txt\n"
            "    └── dir3\n"
            "        └── file3.txt"
        )
        self.assertEqual(build_directory_tree_string(selected_files), expected)

    def test_multiple_top_level_directories(self):
        selected_files = [
            "dir1/file1.txt",
            "dir2/file2.txt",
            "file3.txt"
        ]
        expected = (
            "├── dir1\n"
            "│   └── file1.txt\n"
            "├── dir2\n"
            "│   └── file2.txt\n"
            "└── file3.txt"
        )
        self.assertEqual(build_directory_tree_string(selected_files), expected)

    def test_conflicting_file_and_directory(self):
        selected_files = [
            "dir1/file1.txt",
            "dir1/file1.txt/subfile.txt"  # This implies file1.txt is a directory
        ]
        with self.assertRaises(ValueError) as context:
            build_directory_tree_string(selected_files)
        self.assertIn("Conflict at 'file1.txt'", str(context.exception))

    def test_duplicate_files(self):
        selected_files = [
            "dir1/file1.txt",
            "dir1/file1.txt"  # Duplicate, should be handled gracefully
        ]
        expected = (
            "└── dir1\n"
            "    └── file1.txt"
        )
        self.assertEqual(build_directory_tree_string(selected_files), expected)

    def test_files_with_common_prefix(self):
        selected_files = [
            "dir1/file.txt",
            "dir1/file_backup.txt",
            "dir1/files/file1.txt",
            "dir1/files/file2.txt"
        ]
        expected = (
            "└── dir1\n"
            "    ├── file.txt\n"
            "    ├── file_backup.txt\n"
            "    └── files\n"
            "        ├── file1.txt\n"
            "        └── file2.txt"
        )
        self.assertEqual(build_directory_tree_string(selected_files), expected)

    def test_absolute_paths(self):
        selected_files = [
            "/home/user/project/file1.py",
            "/home/user/project/dir1/file2.py",
            "/home/user/project/dir2/file3.py"
        ]
        expected = (
            "└── home\n"
            "    └── user\n"
            "        └── project\n"
            "            ├── dir1\n"
            "            │   └── file2.py\n"
            "            ├── dir2\n"
            "            │   └── file3.py\n"
            "            └── file1.py"
        )
        self.assertEqual(build_directory_tree_string(selected_files), expected)

    def test_mixed_relative_and_absolute_paths(self):
        selected_files = [
            "dir1/file1.txt",
            "/dir2/file2.txt",
            "dir1/dir3/file3.txt"
        ]
        expected = (
            "├── dir1\n"
            "│   ├── dir3\n"
            "│   │   └── file3.txt\n"
            "│   └── file1.txt\n"
            "└── dir2\n"
            "    └── file2.txt"
        )
        self.assertEqual(build_directory_tree_string(selected_files), expected)

    def test_files_with_special_characters(self):
        selected_files = [
            "dir-1/file_1.txt",
            "dir 2/file@2!.txt",
            "dir_3/sub-dir/file#3$.txt"
        ]
        expected = (
            "├── dir 2\n"
            "│   └── file@2!.txt\n"
            "├── dir-1\n"
            "│   └── file_1.txt\n"
            "└── dir_3\n"
            "    └── sub-dir\n"
            "        └── file#3$.txt"
        )
        self.assertEqual(build_directory_tree_string(selected_files), expected)

    def test_large_directory_structure(self):
        selected_files = [
            "atlaz/client.py",
            "atlaz/__init__.py",
            "atlaz/.atlaz_helper/original/",
            "atlaz/frontend/index.html",
            "atlaz/frontend/directory_structure.json",
            "atlaz/frontend/styles.css",
            "atlaz/frontend/__init__.py",
            "atlaz/frontend/main_frontend.py",
            "atlaz/frontend/files.json",
            "atlaz/frontend/livereload_server.py",
            "atlaz/frontend/python_backend/flask_server.py",
            "atlaz/frontend/python_backend/start_gen.py",
            "atlaz/frontend/python_backend/.atlaz_helper/original/",
            "atlaz/frontend/python_backend/.atlaz_helper/created/created-test7.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test1.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test6.py.txt.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test3.py.txt.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test3.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/created-test9.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/created-test5.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test7.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test9.py.txt.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test10.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/created-test1.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test4.py.txt.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test1.py.txt.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/created-test3.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test9.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test5.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test2.py.txt.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test0.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/created-test6.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/created-test8.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/created-test4.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test7.py.txt.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test10.py.txt.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test2.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/created-test0.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test0.py.txt.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test6.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test8.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test4.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/created-test10.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test8.py.txt.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/created-test2.py.txt",
            "atlaz/frontend/python_backend/.atlaz_helper/created/test5.py.txt.txt",
            "atlaz/frontend/scripts/fileViewer.js",
            "atlaz/frontend/scripts/buttonHandlers.js",
            "atlaz/frontend/scripts/messageForm.js",
            "atlaz/frontend/scripts/directoryTree.js",
            "atlaz/codeGen/__init__.py",
            "atlaz/codeGen/code_gen.py",
            "atlaz/codeGen/schema.py",
            "atlaz/codeGen/generate_input/bad_files.py",
            "atlaz/codeGen/generate_input/__init__.py",
            "atlaz/codeGen/generate_input/file_loader.py"
        ]
        # Due to the length and complexity, we'll verify key parts instead of exact match
        tree_string = build_directory_tree_string(selected_files)
        self.assertIn("└── atlaz", tree_string)
        self.assertIn("    ├── .atlaz_helper", tree_string)
        self.assertIn("    │   └── original", tree_string)
        self.assertIn("    ├── codeGen", tree_string)
        self.assertIn("    │   ├── __init__.py", tree_string)
        self.assertIn("    │   ├── code_gen.py", tree_string)
        self.assertIn("    │   ├── generate_input", tree_string)
        self.assertIn("    │   │   ├── bad_files.py", tree_string)
        self.assertIn("    │   │   ├── file_loader.py", tree_string)
        self.assertIn("    │   │   └── __init__.py", tree_string)
        self.assertIn("    │   └── schema.py", tree_string)
        self.assertIn("    ├── frontend", tree_string)
        self.assertIn("        ├── __init__.py", tree_string)
        self.assertIn("        ├── directory_structure.json", tree_string)
        self.assertIn("        ├── files.json", tree_string)
        self.assertIn("        ├── index.html", tree_string)
        self.assertIn("        ├── livereload_server.py", tree_string)
        self.assertIn("        ├── main_frontend.py", tree_string)
        self.assertIn("        ├── scripts", tree_string)
        self.assertIn("            ├── buttonHandlers.js", tree_string)
        self.assertIn("            ├── directoryTree.js", tree_string)
        self.assertIn("            ├── fileViewer.js", tree_string)
        self.assertIn("            └── messageForm.js", tree_string)
        self.assertIn("        ├── styles.css", tree_string)
        self.assertIn("        └── python_backend", tree_string)
        self.assertIn("            ├── .atlaz_helper", tree_string)
        self.assertIn("                ├── created", tree_string)
        self.assertIn("                └── replacing", tree_string)
        self.assertIn("            ├── flask_server.py", tree_string)
        self.assertIn("            └── start_gen.py", tree_string)
        self.assertIn("    ├── scripts", tree_string)
        self.assertIn("        ├── buttonHandlers.js", tree_string)
        self.assertIn("        ├── directoryTree.js", tree_string)
        self.assertIn("        ├── fileViewer.js", tree_string)
        self.assertIn("        └── messageForm.js", tree_string)
        self.assertIn("    └── client.py", tree_string)
        self.assertIn("    └── __init__.py", tree_string)

if __name__ == "__main__":
    unittest.main()