from setuptools import setup, find_packages

setup(
    name="storage-bridge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        "boto3>=1.20.0",
        "sqlalchemy>=1.4.0",
    ],
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

