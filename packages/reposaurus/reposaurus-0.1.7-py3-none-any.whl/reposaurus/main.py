#!/usr/bin/env python3

"""
Reposaurus - Repository to Text Converter

This module provides the core functionality for converting repository contents into a
comprehensive text file. It supports both simple pattern matching for default exclusions
and advanced gitignore-style pattern matching for custom exclusions.

The tool can be used either with default exclusions (defined in patterns.py) or with
a custom exclusion file using gitignore syntax. This dual approach provides both
simplicity for common cases and power for advanced needs.
"""

import os
from pathlib import Path
import sys
import argparse
from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern
from reposaurus import patterns


def should_exclude_default(path):
    """
    Apply default pattern matching using simple string comparison.
    This is the original, straightforward approach for built-in patterns.

    Args:
        path (Path): Path object to check against default patterns

    Returns:
        bool: True if the path should be excluded based on default patterns
    """
    path_str = str(path)

    # Check if the path contains any of our default patterns
    for pattern in patterns.EXCLUDE_PATTERNS:
        if pattern in path_str:
            return True

    # Check file extensions specifically
    if path.is_file():
        extension = path.suffix.lower()
        if extension in patterns.EXCLUDE_PATTERNS:
            return True

    return False


def parse_gitignore_file(file_path):
    """
    Parse a custom exclusion file using gitignore syntax.
    Provides advanced pattern matching capabilities including wildcards and negation.

    Args:
        file_path (str): Path to the gitignore-style pattern file

    Returns:
        PathSpec: Object for gitignore pattern matching, or None if parsing fails
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            patterns = [
                line.strip()
                for line in f
                if line.strip() and not line.startswith('#')
            ]
            return PathSpec.from_lines(GitWildMatchPattern, patterns)
    except Exception as e:
        print(f"Warning: Could not read pattern file {file_path}: {str(e)}",
              file=sys.stderr)
        return None


def should_exclude(path, custom_spec=None):
    """
    Unified exclusion checker that combines both default and custom pattern matching.
    Default patterns are always checked first, then custom patterns if provided.

    Args:
        path (Path): Path object to check
        custom_spec (PathSpec, optional): Custom pattern matcher for gitignore rules

    Returns:
        bool: True if the path should be excluded
    """
    # Always check default patterns first
    if should_exclude_default(path):
        return True

    # If custom patterns were provided, check those too
    if custom_spec is not None:
        try:
            rel_path = str(path.relative_to(Path.cwd()))
            if custom_spec.match_file(rel_path):
                return True
        except ValueError:
            # Handle case where path is not relative to cwd
            pass

    return False


def get_directory_structure(start_path, custom_spec=None):
    """
    Generate a formatted string representing the directory structure.
    Applies both default and custom exclusion patterns if provided.

    Args:
        start_path (Path): Root path to start directory traversal
        custom_spec (PathSpec, optional): Custom pattern matcher for gitignore rules

    Returns:
        str: Formatted directory structure string
    """
    tree = []
    start_path = Path(start_path)

    for path in sorted(start_path.rglob('*')):
        if should_exclude(path, custom_spec):
            continue

        rel_path = path.relative_to(start_path)
        if path.is_dir():
            tree.append(f"{str(rel_path)}/")
        else:
            tree.append(str(rel_path))

    return '\n'.join('    ' + str(item) for item in tree)


def process_repository(repo_path, output_file, custom_patterns_file=None):
    """
    Process repository and create a text snapshot.
    Handles both file traversal and content extraction with pattern matching.

    Args:
        repo_path (str): Path to the repository to process
        output_file (str): Path where the output file should be created
        custom_patterns_file (str, optional): Path to custom exclusion patterns file
    """
    repo_path = Path(repo_path)
    custom_spec = None

    # Parse custom patterns if provided
    if custom_patterns_file:
        custom_spec = parse_gitignore_file(custom_patterns_file)
        if custom_spec is None:
            print("Warning: Using only default exclusion patterns")

    with open(output_file, 'w', encoding='utf-8') as f:
        # Write directory structure
        f.write("Directory structure:\n")
        f.write(f"└── {repo_path.name}/\n")
        f.write(get_directory_structure(repo_path, custom_spec))
        f.write('\n\n')

        # Write file contents
        for path in sorted(repo_path.rglob('*')):
            if should_exclude(path, custom_spec) or path.is_dir():
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
    """
    Main entry point for the Reposaurus tool.
    Handles command-line argument parsing and high-level program flow.
    """
    parser = argparse.ArgumentParser(
        description='Create a text snapshot of your repository with smart file filtering.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    reposaurus                     # Process current directory with default exclusions
    reposaurus /path/to/repo      # Process specific directory
    reposaurus -e .gitignore      # Use custom exclusion patterns

Exclusion file syntax (when using --exclude-file):
    # Ignore all .txt files
    *.txt

    # But keep important.txt
    !important.txt

    # Ignore temp folders anywhere
    **/temp/

    # Ignore specific directories
    build/
    node_modules/
""")

    parser.add_argument('path', nargs='?', default=os.getcwd(),
                        help='Repository path (default: current directory)')
    parser.add_argument('--exclude-file', '-e',
                        help='Path to custom exclusion file (uses .gitignore syntax)')

    args = parser.parse_args()

    # Validate repository path
    if not os.path.isdir(args.path):
        print(f"Error: {args.path} is not a directory")
        sys.exit(1)

    # Process repository and generate output
    output_file = Path(args.path) / 'repository_contents.txt'
    process_repository(args.path, output_file, args.exclude_file)
    print(f"Repository contents written to {output_file}")


if __name__ == "__main__":
    main()