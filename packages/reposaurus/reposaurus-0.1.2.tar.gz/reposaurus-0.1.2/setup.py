from setuptools import setup, find_packages

setup(
    name="reposaurus",
    version="0.1.2",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'reposaurus=repo2txt.main:main',  # This makes the command 'reposaurus' available
        ],
    },
    author="Andy Thomas",
    author_email="your.email@example.com",  # Update this if you want
    description="Just turns your repo into a text file innit...🦖",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/reposaurus",  # Update if you have a GitHub repo
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