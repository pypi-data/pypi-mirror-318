from setuptools import setup, find_packages

setup(
    name="reposaurus",
    version="0.1.4",  # Incrementing version for new feature
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'reposaurus=reposaurus.main:main',
        ],
    },
    install_requires=[
        'pathspec>=0.9.0',  # Adding pathspec for gitignore-style pattern matching
    ],
    author="Andy Thomas",
    author_email="your.email@example.com",
    description="Just turns your repo into a text file innit...🦖",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/reposaurus",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
    ],
    python_requires=">=3.6",
)