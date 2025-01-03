# 🦖 Reposaurus

A tool for turning repositories into text files innit.

## Overview

Reposaurus scans your repository and creates a comprehensive text file containing your directory structure and file contents. It's perfect for:
- Creating documentation snapshots
- Sharing code context with AI tools
- Archiving project states
- Code review preparation

## Installation

```bash
pip install reposaurus
```

## Usage

Basic usage:
```bash
reposaurus           # Process current directory
reposaurus /my/path  # Process specific directory
```

This will create a `repository_contents.txt` file in your target directory.

## Features

- 📁 Directory structure visualization
- 📝 File content extraction
- 🧠 Smart file filtering (ignores build directories, binaries, etc.)
- 🦖 Works with any git repository

## File Filtering

Reposaurus automatically excludes:
- Development directories (.git, .vs, .idea, etc.)
- Build and dependency directories (bin, obj, node_modules, etc.)
- Cache directories (.cache, __pycache__, etc.)
- System files (.DS_Store, Thumbs.db)
- Binary and media files (.exe, .jpg, .mp3, etc.)
- Log and database files (.log, .sqlite, etc.)

## Authors

- Andy Thomas - Initial work

## Acknowledgments

- Inspired by the need to share repository contents with AI tools
- Built with love and a touch of prehistoric magic 🦖✨