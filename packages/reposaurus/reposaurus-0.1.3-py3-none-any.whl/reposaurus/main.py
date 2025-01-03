#!/usr/bin/env python3
import os
from pathlib import Path
import sys


def should_exclude(path):
    """Check if a path should be excluded from processing."""
    exclude_patterns = [
        # Development directories
        '.git',
        '.vs',
        '.idea',
        '.vscode',
        '__pycache__',
        'venv',
        '.env',

        # Build and dependency directories
        'bin',
        'obj',
        'build',
        'dist',
        'node_modules',
        'packages',
        'target',

        # Cache directories
        '.cache',
        '.pytest_cache',
        '.mypy_cache',

        # System files
        '.DS_Store',
        'Thumbs.db',

        # Common large file extensions
        '.pyc',
        '.pyo',
        '.pyd',
        '.so',
        '.dll',
        '.dylib',
        '.exe',
        '.bin',
        '.jar',
        '.war',
        '.zip',
        '.tar',
        '.gz',
        '.7z',
        '.rar',

        # Log and data files
        '.log',
        '.sqlite',
        '.db',

        # Media files
        '.jpg',
        '.jpeg',
        '.png',
        '.gif',
        '.ico',
        '.mp3',
        '.mp4',
        '.avi',
        '.mov'
    ]

    path_str = str(path)

    # Check if the path contains any of the patterns
    for pattern in exclude_patterns:
        if pattern in path_str:
            return True

    # Check file extensions
    if path.is_file():
        extension = path.suffix.lower()
        if extension in exclude_patterns:
            return True

    return False

def get_directory_structure(start_path):
    """Generate a directory structure string."""
    tree = []
    start_path = Path(start_path)

    for path in sorted(start_path.rglob('*')):
        if should_exclude(path):
            continue

        rel_path = path.relative_to(start_path)
        if path.is_dir():
            tree.append(f"{str(rel_path)}/")
        else:
            tree.append(str(rel_path))

    return '\n'.join('    ' + str(item) for item in tree)

def process_repository(repo_path, output_file):
    """Process repository and write to output file."""
    repo_path = Path(repo_path)

    with open(output_file, 'w', encoding='utf-8') as f:
        # Write directory structure
        f.write("Directory structure:\n")
        f.write(f"└── {repo_path.name}/\n")
        f.write(get_directory_structure(repo_path))
        f.write('\n\n')

        # Write file contents
        for path in sorted(repo_path.rglob('*')):
            if should_exclude(path) or path.is_dir():
                continue

            try:
                with open(path, 'r', encoding='utf-8') as source_file:
                    content = source_file.read()

                f.write('=' * 48 + '\n')
                f.write(f"File: /{path.relative_to(repo_path)}\n")
                f.write('=' * 48 + '\n')
                f.write(content)
                f.write('\n\n')
            except UnicodeDecodeError:
                print(f"Warning: Could not read {path} as text file", file=sys.stderr)
            except Exception as e:
                print(f"Error processing {path}: {str(e)}", file=sys.stderr)

def main():
    """Main entry point."""
    # Use current working directory by default
    if len(sys.argv) == 1:
        repo_path = os.getcwd()  # Get current working directory
    elif len(sys.argv) == 2:
        repo_path = sys.argv[1]
    else:
        print("Usage: reposaurus [repository_path]")
        sys.exit(1)

    if not os.path.isdir(repo_path):
        print(f"Error: {repo_path} is not a directory")
        sys.exit(1)

    output_file = Path(repo_path) / 'repository_contents.txt'
    process_repository(repo_path, output_file)
    print(f"Repository contents written to {output_file}")

if __name__ == "__main__":
    main()