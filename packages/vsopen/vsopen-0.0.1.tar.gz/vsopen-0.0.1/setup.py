from setuptools import setup, find_packages

setup(
    name="vsopen",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "gitpython>=3.1.0",
    ],
    entry_points={
        "console_scripts": [
            "vsopen=vsopen.cli:main",
        ],
    },
    author="frenzywall",
    author_email="sreeramjvp.work@gmail.com",
    description="Open GitHub repositories directly in VS Code",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/frenzywall/vsopen",
    project_urls={
        "Bug Tracker": "https://github.com/frenzywall/vsopen/issues",
        "Source Code": "https://github.com/frenzywall/vsopen",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
