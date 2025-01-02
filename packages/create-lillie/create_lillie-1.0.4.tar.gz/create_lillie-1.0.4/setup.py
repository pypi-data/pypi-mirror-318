from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="create-lillie",
    version="1.0.4",
    author="Sarthak Ghoshal",
    author_email="sarthak22.ghoshal@gmail.com",
    description="A CLI tool for creating lilliepy projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/websitedeb/create-lillie",
    py_modules=["cli"],
    include_package_data=True,
    package_data={"": ["templates/**/*"]},
    install_requires=[
        "typer[all]",
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "create-lillie=cli:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
