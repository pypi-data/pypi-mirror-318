from setuptools import setup, find_packages

setup(
    name="logstore",
    version="1.0.0",
    description="Python log store.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vicky Tenzin",
    author_email="vicky.tenzin@widas.in",
    url="https://gitlab.widas.de/cnips/arc-libs/py-logstore",  # Replace with your repo URL
    packages=find_packages(),
    python_requires=">=3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
