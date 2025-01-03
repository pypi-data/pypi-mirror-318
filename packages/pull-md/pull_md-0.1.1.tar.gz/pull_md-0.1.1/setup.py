from setuptools import setup, find_packages

setup(
    name="pull_md",
    version="0.1.1",
    packages=find_packages(),
    url="https://github.com/chigwell/pull_md",
    license="MIT",
    author="Eugene Evstafev",
    author_email="chigwel@gmail.com",
    description="A simple Python package to convert URLs to Markdown using the pull.md service.",
    install_requires=[
        "requests>=2.25.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)