from setuptools import setup, find_packages

setup(
    name="fastapi-create-project",  # valid name (without double hyphen)
    version="0.0.1",  # valid version
    description="A tool to generate FastAPI project structures",
    author="Meet velani",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fastapi_create_project=fastapi_project_gen.generator:main"  # Ensure entry point is correct
        ],
    },
    install_requires=[],  # Specify dependencies if needed
)
