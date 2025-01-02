from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="storage-bridge",
    version="0.1.2",
    packages=find_packages(),
    install_requires=requirements,
    author="Jacob Vartuli-Schonberg",
    author_email="jacob.vartuli.schonberg@gmail.com",
    description="A Python package for managing storage",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/storage-bridge",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)

