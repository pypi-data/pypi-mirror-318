from setuptools import setup, find_packages
from pathlib import Path

# Read the content of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="sallmon-core",
    version="2.3.2",  # Increment version for changes
    description="Sallmon Core: a utility chain invented to eat Stripe's lunch",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specify markdown format
    author="c80129b (Andrew Polykandriotis)",
    author_email="andrew@minakilabs.com",
    url="https://github.com/minakilabs/sallmon_core",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=[
        "click>=8.1.3",  # Ensure compatibility with Flask
        "fastapi",
        "uvicorn",
        "websockets",
        "cryptography",
        "flask>=3.0.0",  # Ensure modern Flask versions
        "gunicorn",  # Production-ready WSGI server for Flask
        "Pillow",
        "httpx",
    ],
    entry_points={
        "console_scripts": [
            "sallmond=sallmon.cli.sallmond:cli",  # CLI for managing services
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
