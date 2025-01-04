from setuptools import setup, find_packages
import os

# Read the long description from README.md
with open("Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Function to include non-Python files
def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(path, filename)
            paths.append(os.path.relpath(filepath, directory))
    return paths

# Include data and config files
extra_files = []
for algorithm in os.listdir("mu/algorithms"):
    alg_path = os.path.join("mu/algorithms", algorithm)
    if os.path.isdir(alg_path):
        extra_files.extend([os.path.join("mu", "algorithms", algorithm, f) for f in package_files(alg_path)])

setup(
    name="unlearn_diff",  # Replace with your project name
    version="0.1.4",
    author="nebulaanish",
    author_email="nebulaanish@gmail.com",
    description="A repo containing unlearning algorithms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RamailoTech/msu_unlearningalgorithm",  # Replace with your repo URL
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "mu.algorithms.erase_diff": ["configs/*.yaml", "environment.yaml"],
        "mu.algorithms.esd": ["configs/*.yaml", "environment.yaml"],
        "mu.algorithms.forget_me_not": ["configs/*.yaml", "environment.yaml"],
    },
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change if different
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'create_env=scripts.env_manager:main',
        ],
    },
)
