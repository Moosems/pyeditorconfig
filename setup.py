from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()


setup(
    name="pyeditorconfig",
    version="0.0.1",
    description="A better way to handle .editorconfig files with Python.",
    author="Moosems",
    author_email="moosems.j@gmail.com",
    url="https://github.com/Moosems/pyeditorconfig",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    python_requires=">=3.7",
    license="MIT license",
    packages=["pyeditorconfig"],
    package_data={},
)
