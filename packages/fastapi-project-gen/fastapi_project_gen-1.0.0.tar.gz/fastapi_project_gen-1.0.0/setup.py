from setuptools import setup, find_packages

setup(
    name="fastapi_project_gen",  # Your library's name on PyPI
    version="1.0.0",
    description="A CLI tool to generate FastAPI MVC project structure",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/fastapi_project_gen",  # Your GitHub repo
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "generate_fastapi_project=fastapi_project_gen.generator:generate_project"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],  # Add dependencies here, e.g., ["fastapi", "pymongo"]
)
