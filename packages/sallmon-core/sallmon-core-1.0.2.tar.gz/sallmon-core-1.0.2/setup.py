from setuptools import setup, find_packages

setup(
    name="sallmon-core",
    version="1.0.2",
    description="Sallmon Blockchain FastAPI Server",
    author="Andrew Polykandriotis",
    author_email="andrew@minakilabs.com",
    url="https://github.com/minakilabs/sallmon-sdk",
    packages=find_packages(),  # Automatically find all packages in the directory
    include_package_data=True,
    install_requires=[
        "fastapi>=0.101.0",
        "uvicorn>=0.27.1",
        "websockets>=10.4",
        "requests>=2.0",
    ],
    entry_points={
        "console_scripts": [
            "sallmon-server=server:start_server",  # Server entry point
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
