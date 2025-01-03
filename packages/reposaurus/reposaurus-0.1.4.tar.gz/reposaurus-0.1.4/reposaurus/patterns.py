# patterns.py
"""Configuration file containing patterns for file and directory exclusion."""

# Development directories
DEV_DIRS = [
    '.git',
    '.vs',
    '.idea',
    '.vscode',
    '__pycache__',
    'venv',
    '.venv',
    '.env',
    '.egg-info',
]

# Build and dependency directories
BUILD_DIRS = [
    'bin',
    'obj',
    'build',
    'dist',
    'node_modules',
    'packages',
    'target',
]

# Cache directories
CACHE_DIRS = [
    '.cache',
    '.pytest_cache',
    '.mypy_cache',
]

# System files
SYSTEM_FILES = [
    '.DS_Store',
    'Thumbs.db',
]

# Binary file extensions
BINARY_EXTENSIONS = [
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
]

# Log and data files
DATA_FILES = [
    '.log',
    '.sqlite',
    '.db',
]

# Media files
MEDIA_FILES = [
    '.jpg',
    '.jpeg',
    '.png',
    '.gif',
    '.ico',
    '.mp3',
    '.mp4',
    '.avi',
    '.mov',
]

# Combine all patterns into a single list for easy access
EXCLUDE_PATTERNS = (
    DEV_DIRS +
    BUILD_DIRS +
    CACHE_DIRS +
    SYSTEM_FILES +
    BINARY_EXTENSIONS +
    DATA_FILES +
    MEDIA_FILES
)