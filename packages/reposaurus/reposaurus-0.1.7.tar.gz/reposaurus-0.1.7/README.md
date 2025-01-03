# 🦖 Reposaurus

A powerful tool for transforming repositories into comprehensive text files. Perfect for documentation, AI tool integration, and code review preparation.

## Overview

Reposaurus is designed to capture your entire codebase in a single, well-organized text file. It features a dual pattern matching system: simple and efficient default exclusions for common cases, plus advanced gitignore-style pattern matching when you need more control. Whether you're preparing code for AI analysis, documenting your project, or archiving project states, Reposaurus helps you focus on what matters by excluding unnecessary files.

## Features

- 📁 Smart Directory Structure Visualization
- 📝 Complete File Content Extraction
- 🧠 Dual Pattern Matching System:
  - Simple, efficient matching for common exclusions
  - Advanced gitignore-style patterns when you need them
- 🦖 Compatible with Any Git Repository
- ⚡ Fast and Efficient Processing
- 🛠️ Simple Command-Line Interface

## Installation

Install Reposaurus using pip:

```bash
pip3 install reposaurus
```

On macOS, you might need to add Python's bin directory to your PATH:
```bash
echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## Basic Usage

Reposaurus offers straightforward command-line operation:

```bash
# Process current directory with default exclusions
reposaurus

# Process a specific directory
reposaurus /path/to/repository

# Use custom exclusion patterns
reposaurus --exclude-file my_patterns.txt
```

This creates a `repository_contents.txt` file in your target directory containing:
- A visual representation of your directory structure
- The complete contents of all included text files
- Automatic filtering of binary files and development artifacts

## Pattern Matching System

Reposaurus employs a dual approach to file exclusions:

### Default Pattern Matching

By default, Reposaurus uses a simple, efficient pattern matching system that automatically excludes:

- Development Directories:
  - Version control (`.git`, `.svn`)
  - IDE configurations (`.vs`, `.idea`, `.vscode`)
  - Python artifacts (`__pycache__`, `.egg-info`)
  - Virtual environments (`venv`, `.env`)

- Build and Dependencies:
  - Build outputs (`bin`, `obj`, `build`, `dist`)
  - Dependencies (`node_modules`, `packages`)
  - Cache directories (`.cache`, `__pycache__`)

- System and Binary Files:
  - System files (`.DS_Store`, `Thumbs.db`, `package.lock.json`, `repository_contents.txt`)
  - Compiled files (`.pyc`, `.exe`, `.dll`)
  - Archives (`.zip`, `.tar`, `.gz`)
  - Media files (`.jpg`, `.png`, `.mp3`)
  - Logs and databases (`.log`, `.sqlite`)

### Advanced Pattern Matching

When you need more control, you can provide a custom exclusion file using familiar gitignore syntax:

```bash
reposaurus --exclude-file my_patterns.txt
```

Your exclusion file can use the full `.gitignore` syntax:

```gitignore
# Ignore all .txt files
*.txt

# But keep important.txt
!important.txt

# Ignore temp folders anywhere
**/temp/

# Ignore specific directories
build/
node_modules/

# Complex patterns
docs/**/*.md
!docs/README.md
```

Pattern matching features include:
- Basic wildcards (`*.txt`, `project-*/`)
- Directory wildcards (`**/temp` matches temp anywhere)
- Negation patterns (`!important.txt`)
- Directory-specific matching (`docs/*.md`)
- Comments for pattern documentation

## Output Format

The generated `repository_contents.txt` file is structured for clarity:

```text
Directory structure:
└── repository/
    ├── src/
    │   ├── main.py
    │   └── utils.py
    ├── docs/
    │   └── README.md
    └── config.json

================================================
File: /src/main.py
================================================
[File contents here]

================================================
File: /src/utils.py
================================================
[File contents here]
```

## Error Handling

Reposaurus handles various edge cases gracefully:
- Binary files are automatically skipped
- Files with encoding issues are noted but don't halt processing
- Invalid patterns in exclusion files are reported with helpful messages
- Missing directories or permissions issues are clearly reported

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## License

MIT License - See LICENSE file for details

## Authors

- Andy Thomas - Initial work

## Acknowledgments

Built with love and a touch of prehistoric magic 🦖✨

For more information, visit our documentation or raise an issue on GitHub.

## Version History

- 0.1.4 - Added dual pattern matching system with gitignore support
- 0.1.3 - Initial public release