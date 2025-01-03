#!/usr/bin/env python3
import os
from pathlib import Path
import sys
import argparse
from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern
from reposaurus import patterns


def create_default_pathspec():
    """
    Convert our default exclusion patterns to a PathSpec object.
    We need to modify the patterns slightly to match gitignore syntax.
    """
    gitignore_patterns = []

    # Convert our existing patterns to gitignore format
    for pattern in patterns.EXCLUDE_PATTERNS:
        # If it's an extension, make it a wildcard pattern
        if pattern.startswith('.'):
            gitignore_patterns.append(f'**/*{pattern}')
        # If it's a directory, make it match anywhere in the path
        else:
            gitignore_patterns.append(f'**/{pattern}/**')
            gitignore_patterns.append(f'**/{pattern}')

    return PathSpec.from_lines(GitWildMatchPattern, gitignore_patterns)


def parse_exclusion_file(file_path):
    """
    Parse an exclusion file and return a PathSpec object.
    The file should use gitignore-style pattern syntax.

    Args:
        file_path: Path to the exclusion file

    Returns:
        PathSpec object for pattern matching
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Filter out empty lines and comments
            patterns = [line.strip() for line in f
                        if line.strip() and not line.startswith('#')]
            return PathSpec.from_lines(GitWildMatchPattern, patterns)
    except Exception as e:
        print(f"Warning: Could not read exclusion file {file_path}: {str(e)}",
              file=sys.stderr)
        return PathSpec.from_lines(GitWildMatchPattern, [])


def should_exclude(path, exclusion_spec):
    """
    Check if a path should be excluded using gitignore-style pattern matching.

    Args:
        path: Path object to check
        exclusion_spec: PathSpec object for pattern matching

    Returns:
        bool: True if the path should be excluded, False otherwise
    """
    # Convert path to string relative to current directory
    try:
        rel_path = str(path.relative_to(Path.cwd()))
    except ValueError:
        # If path is not relative to cwd, use the full path
        rel_path = str(path)

    return exclusion_spec.match_file(rel_path)


def get_directory_structure(start_path, exclusion_spec):
    """
    Generate a directory structure string.

    Args:
        start_path: Root path to start traversal
        exclusion_spec: PathSpec object for pattern matching

    Returns:
        str: Formatted directory structure
    """
    tree = []
    start_path = Path(start_path)

    for path in sorted(start_path.rglob('*')):
        if should_exclude(path, exclusion_spec):
            continue

        rel_path = path.relative_to(start_path)
        if path.is_dir():
            tree.append(f"{str(rel_path)}/")
        else:
            tree.append(str(rel_path))

    return '\n'.join('    ' + str(item) for item in tree)


def process_repository(repo_path, output_file, exclusion_spec):
    """
    Process repository and write to output file.

    Args:
        repo_path: Path to repository root
        output_file: Path to output file
        exclusion_spec: PathSpec object for pattern matching
    """
    repo_path = Path(repo_path)

    with open(output_file, 'w', encoding='utf-8') as f:
        # Write directory structure
        f.write("Directory structure:\n")
        f.write(f"└── {repo_path.name}/\n")
        f.write(get_directory_structure(repo_path, exclusion_spec))
        f.write('\n\n')

        # Write file contents
        for path in sorted(repo_path.rglob('*')):
            if should_exclude(path, exclusion_spec) or path.is_dir():
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
    Main entry point with argument parsing and error handling.
    """
    parser = argparse.ArgumentParser(
        description='Create a text snapshot of your repository with smart file filtering.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example exclusion file format (.gitignore syntax):
  # Ignore all .txt files
  *.txt

  # But include important.txt
  !important.txt

  # Ignore temp folders anywhere
  **/temp/

  # Ignore specific file
  path/to/specific/file.md
""")

    parser.add_argument('path', nargs='?', default=os.getcwd(),
                        help='Repository path (default: current directory)')
    parser.add_argument('--exclude-file', '-e',
                        help='Path to custom exclusion file (uses .gitignore syntax)')
    parser.add_argument('--append-exclude', '-a', action='store_true',
                        help='Append custom exclusions to defaults instead of replacing them')

    args = parser.parse_args()

    # Validate repository path
    if not os.path.isdir(args.path):
        print(f"Error: {args.path} is not a directory")
        sys.exit(1)

    # Create default exclusion spec
    default_spec = create_default_pathspec()

    # Handle custom exclusion file
    if args.exclude_file:
        if not os.path.exists(args.exclude_file):
            print(f"Warning: Exclusion file '{args.exclude_file}' not found. Using default exclusions.")
            exclusion_spec = default_spec
        else:
            custom_spec = parse_exclusion_file(args.exclude_file)
            if args.append_exclude:
                # Combine both specs (order matters - custom patterns can override defaults)
                exclusion_spec = PathSpec.from_lines(GitWildMatchPattern,
                                                     list(custom_spec.patterns) + list(default_spec.patterns))
            else:
                exclusion_spec = custom_spec
    else:
        exclusion_spec = default_spec

    output_file = Path(args.path) / 'repository_contents.txt'
    process_repository(args.path, output_file, exclusion_spec)
    print(f"Repository contents written to {output_file}")


if __name__ == "__main__":
    main()