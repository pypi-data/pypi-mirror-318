from setuptools import setup, find_packages

setup(
    name="yophonebot",
    version="0.1.1",
    description="Python package for interacting with YoPhone Bot API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nairi Hovhannisyan",
    author_email="your.email@example.com",
    url="https://github.com/nairihovh/yophone",
    packages=find_packages(),
    install_requires=[
        "requests>=2.20.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

