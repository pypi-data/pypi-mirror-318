from setuptools import setup, find_packages

setup(
    name="telegram-session-converter",
    version="0.1.2",
    packages=find_packages(),
    install_requires=["telethon", "pydantic"],
    author="bundemshake",
    author_email="bundemshake@gmail.com",  # Added comma here
    description="A simple library for converting .session files from/to telethon or pyrogram format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Adjust according to your license
    ],
)
