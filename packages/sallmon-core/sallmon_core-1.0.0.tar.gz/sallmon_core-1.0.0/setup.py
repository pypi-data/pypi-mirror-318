from setuptools import setup, find_packages

setup(
    name="sallmon-core",
    version="1.0.0",
    description="Sallmon Core: A Bitcoin Clone",
    author="c80129b (Andrew Polykandriotis)",
    author_email="andrew@example.com",
    url="https://github.com/minakilabs/sallmon_core",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=[
        "click",       # CLI framework
        "fastapi",     # WebSocket server
        "uvicorn",     # ASGI server
        "websockets",  # WebSocket management
        "cryptography" # Cryptographic utilities
    ],
    entry_points={
        "console_scripts": [
            "sallmon=sallmon.cli.main:main",
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
