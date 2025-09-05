from setuptools import setup, find_packages

setup(
    name="webserver_helper",               # package name
    version="1.0.0",
    description="Lightweight Flask web server wrapper with video and text streaming",
    packages=find_packages(),
    install_requires=[
        "Flask",
    ],
    python_requires=">=3.8",
)
