import os
from datetime import datetime

from setuptools import find_packages, setup

VERSION = os.environ.get("TAG_VERSION", datetime.now().strftime("%Y.%m.%d.%H%M%S"))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kanban_indexer",
    version=VERSION,
    author="Nick McCleery",
    author_email="contact@nickmccleery.com",
    description="A lexicographic indexing system for Kanban boards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nickmccleery/kanban-indexer",
    packages=find_packages(include=["kanban_indexer", "kanban_indexer.*"]),
    package_data={"kanban_indexer": ["*.py"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest==8.2.2",
            "ruff==0.5.3",
            "setuptools==74.1.2",
        ],
    },
)
