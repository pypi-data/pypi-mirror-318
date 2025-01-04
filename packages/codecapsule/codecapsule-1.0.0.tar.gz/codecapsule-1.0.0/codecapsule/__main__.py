#  _____             _        _____                            _
# /  __ \           | |      /  __ \                          | |
# | /  \/  ___    __| |  ___ | /  \/  __ _  _ __   ___  _   _ | |  ___
# | |     / _ \  / _` | / _ \| |     / _` || '_ \ / __|| | | || | / _ \
# | \__/\| (_) || (_| ||  __/| \__/\| (_| || |_) |\__ \| |_| || ||  __/
#  \____/ \___/  \__,_| \___| \____/ \__,_|| .__/ |___/ \__,_||_| \___|
#                                          | |
#                                          |_|

import argparse
import json
import os
import sys
from pathlib import Path


def is_binary_file(filepath, chunk_size=1024):
    """
    Heuristic: A file is considered binary if it contains a null byte
    in its first `chunk_size` bytes.
    """
    try:
        with open(filepath, "rb") as f:
            chunk = f.read(chunk_size)
            if b"\0" in chunk:
                return True
    except OSError:
        # If there's an error opening the file in binary mode, treat as binary
        return True
    return False


def create_capsule(root_dir, ignore_patterns=None):
    root_path = Path(root_dir).resolve()

    if (
        root_path == Path("/")  # Unix-like systems
        or root_path == Path("C:\\")  # Windows drive root
        or str(root_path).lower() in ["/", "\\", "c:\\", "c:"]
        or root_path.parent == root_path  # Covers edge cases
    ):
        print("Error: Refusing to run at the system root directory. Exiting ...")
        sys.exit(1)

    if ignore_patterns is None:
        # Adjust these patterns as needed.
        ignore_patterns = {
            ".venv",
            "venv",
            ".git",
            "__pycache__",
            "models",
            ".pytest_cache",
            ".mypy_cache",
            ".pyc",  # Use regex-like pattern for file extensions
            ".pyo",
            ".pyd",
            ".class",
            ".db",
            ".exe",
            ".dll",
            ".so",
            ".Python",
            ".pypirc",
            "dist/",
            "sdist/",
            ".env",
            ".venv",
            "env/",
            "venv/",
            "ENV/",
        }
    project_files = []
    total_files = 0
    total_size_bytes = 0
    root = Path(root_dir)

    def should_ignore(path):
        """Check if path should be ignored based on patterns."""
        path_str = str(path)
        return any(
            # Check if pattern matches anywhere in the path
            pattern in path_str or 
            # Check if pattern matches file extension (for .pyc, etc.)
            (pattern.startswith('.') and path_str.endswith(pattern))
            for pattern in ignore_patterns
        )
        
    for path in root.rglob("*"):

        # 1. Skip directories
        if path.is_dir():
            continue

        # 2. Skip paths that match the ignore patterns
        if should_ignore(path):
            continue

        # 3. Skip binary files or executables
        if is_binary_file(path):
            continue

        # 4. Try reading the file as UTF-8 text
        try:
            file_size = path.stat().st_size
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            project_files.append(
                {"path": str(path.relative_to(root)), "content": content}
            )
            # Update counters
            total_files += 1
            total_size_bytes += file_size
        except UnicodeDecodeError:
            # Skip binary files
            continue

    print(f"Total files added: {total_files} ...")
    print(f"Total size: {total_size_bytes:,} bytes ...")

    return project_files

def prepare_output_path(output_path):
    """
    Prepare and validate the output file path.

    Args:
        output_path (str): The provided output path.

    Returns:
        str: A validated, absolute path for the output file.

    Raises:
        argparse.ArgumentTypeError: If the path is invalid or cannot be created.
    """
    try:
        # Expand user home directory and convert to absolute path
        full_path = os.path.abspath(os.path.expanduser(output_path))

        # Ensure the directory exists
        output_dir = os.path.dirname(full_path)
        if not os.path.exists(output_dir):
            try:
                os.makedirs(output_dir, exist_ok=True)
            except PermissionError:
                raise argparse.ArgumentTypeError(
                    f"Permission denied: Cannot create directory {output_dir}"
                )

        # Check if we have write permissions
        if os.path.exists(output_dir) and not os.access(output_dir, os.W_OK):
            raise argparse.ArgumentTypeError(
                f"No write permission for directory {output_dir}"
            )

        # Ensure the file has a .json extension ONLY if it doesn't already have it
        if not full_path.lower().endswith(".json"):
            full_path += ".json"

        return full_path

    except Exception as e:
        raise argparse.ArgumentTypeError(f"Invalid output path: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="CodeCapsule is a powerful Python utility that transforms entire project directories into a single, portable JSON file. Perfect for sharing code with AI models, archiving projects, or creating compact code representations."
    )

    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version="%(prog)s 1.0.0",
        help="Show the program version and exit.",
    )

    # Positional argument for directory (default to current dir)
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Path to the directory you want to process (default: current directory).",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="project_capsule.json",
        type=prepare_output_path,
        help="Path to the output JSON file. Can be absolute or relative path. "
        "If only a filename is provided, it will be saved in the current working directory. "
        "Automatically adds .json extension if not provided.",
        metavar="OUTPUT_FILE",
    )

    args = parser.parse_args()

    try:
        capsule = create_capsule(args.directory)

        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(capsule, f, indent=2, ensure_ascii=False)

        print(f"Project capsule successfully saved to: {args.output} ...")
    except IOError as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Conversion error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
