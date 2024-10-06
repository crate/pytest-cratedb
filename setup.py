import os
from pathlib import Path

from setuptools import setup


def here() -> Path:
    return Path(os.path.dirname(__file__))


def read(path: str) -> str:
    filepath: Path = here() / path
    with open(filepath.absolute(), "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="pytest-cratedb",
    version="0.4.0.dev0",
    description="Manages CrateDB instances during your integration tests",
    long_description=read("README.rst"),
    author="Christian Haudum",
    author_email="developer@christianhaudum.at",
    url="https://github.com/crate-workbench/pytest-cratedb",
    packages=["pytest_crate"],
    install_requires=[
        "cr8",
        "crate",
        "pytest>=4.0,<8",
    ],
    extras_require={
        "develop": [
            "flake8<3.8",
            "mypy<1",
            "pytest-cov<5",
            "pytest-flake8<2",
            "pytest-isort<4",
            "pytest-mypy<0.11",
        ],
    },
    entry_points={
        "pytest11": [
            "crate=pytest_crate.plugin:crate",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Testing",
        "Topic :: Database",
    ],
)
