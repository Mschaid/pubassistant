#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()


requirements = []

test_requirements = [
    "pytest>=3",
]

setup(
    author="Mike Schaid",
    author_email="michael.schaid@northwestern.edu",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="A simple web aggent to assist with writing and clarifying abstracts",
    install_requires=requirements,
    license="GNU GENERAL PUBLIC LICENSE",
    # long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords="pubassist",
    name="pubassist",
    packages=find_packages(include=["pubassist", "pubassist.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Mschaid/pubassistant.git",
    version="0.1.0",
    zip_safe=False,
)
