from setuptools import setup, find_packages

setup(
    name="frame-API",
    version="0.1.4",
    description="A lightweight Python web framework.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="matvix",
    author_email="",
    url="https://github.com/matvix90/frameapi.git",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "gunicorn==23.0.0",
        "packaging==24.2",
        "parse==1.20.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
