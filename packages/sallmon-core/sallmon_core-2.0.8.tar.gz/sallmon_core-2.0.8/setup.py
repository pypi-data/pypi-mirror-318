from setuptools import setup, find_packages
from pathlib import Path

# Read the content of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="sallmon-core",
    version="2.0.8",  # Increment version
    description="Sallmon Core: a utility chain invented to eat Stripe's lunch",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specify markdown format
    author="c80129b (Andrew Polykandriotis)",
    author_email="andrew@minakilabs.com",
    url="https://github.com/minakilabs/sallmon_core",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=[
        "click",
        "fastapi",
        "uvicorn",
        "websockets",
        "cryptography"
    ],
    entry_points={
        "console_scripts": [
            "sallmon=sallmon.cli.main:cli",
            "sallmon-server=sallmon.sallmon_core.server:start_server",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
