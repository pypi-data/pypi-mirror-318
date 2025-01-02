from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sallmon-core",
    version="1.0.9",  # Increment version for every change
    description="Sallmon Blockchain FastAPI Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Andrew Polykandriotis",
    author_email="andrew@minakilabs.com",
    url="https://github.com/minakilabs/sallmon-sdk",
    packages=find_packages(include=["sallmon-core", "sallmon-core.*"]),  # Match current folder structure
    include_package_data=True,
    package_dir={"sallmon-core": "sallmon-core"},  # Explicitly map the folder
    install_requires=[
        "fastapi>=0.101.0",
        "uvicorn>=0.27.1",
        "websockets>=10.4",
        "requests>=2.0",
    ],
    entry_points={
        "console_scripts": [
            "sallmon-server=sallmon-core.server:start",  # Entry point for server
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
