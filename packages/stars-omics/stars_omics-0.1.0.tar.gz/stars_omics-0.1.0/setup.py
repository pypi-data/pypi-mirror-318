from setuptools import setup, find_packages

# Read the dependencies from requirements.txt
def read_requirements():
    import os
    req_file = "requirements.txt"
    if os.path.exists(req_file):
        print(f"Found {req_file}")  # Debugging: Check if the file is located
        with open(req_file, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    raise FileNotFoundError(f"{req_file} not found!")  # Explicit error if not found


setup(
    name="stars_omics",  # PyPI package name
    version="0.1.0",
    description="A spatial transcriptomics analysis tool.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Zhaocy-Research/STARS/tree/main",
    author="Chongyue Zhao",
    author_email="zhaocy.research@gmail.com",
    license="MIT",
    packages=find_packages(),  # Automatically finds the stars_omics/ directory
    python_requires=">=3.9",
    install_requires=read_requirements(),  # Dynamically load dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


