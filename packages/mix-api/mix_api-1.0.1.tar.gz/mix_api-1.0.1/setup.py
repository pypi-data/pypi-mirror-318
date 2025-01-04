from setuptools import setup, find_packages

setup(
    name="mix-api",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.8.0"
    ],
    author="fuoip",
    author_email="magicwheelx@gmail.com",
    description="Mix Coin API Python3",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fuoip/mix-api",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 