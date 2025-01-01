from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sallmon-core",
    version="1.0.6",  # Increment version
    description="Sallmon Blockchain FastAPI Server",
    long_description=long_description,  # Include the README content
    long_description_content_type="text/markdown",  # Specify that the long description is in Markdown
    author="Andrew Polykandriotis",
    author_email="andrew@minakilabs.com",
    url="https://github.com/minakilabs/sallmon-sdk",
    py_modules=["server"],  # Include server.py explicitly
    include_package_data=True,
    install_requires=[
        "fastapi>=0.101.0",
        "uvicorn>=0.27.1",
        "websockets>=10.4",
        "requests>=2.0",
    ],
    entry_points={
        "console_scripts": [
            "sallmon-server=server:start_server",  # Entry point for server.py
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
