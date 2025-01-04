from setuptools import setup
from pathlib import Path

setup(
    name="lineup-lang",
    version="0.1.4",
    description="Pseudo language interpreter for Python",
    long_description=Path(__file__).parent.joinpath("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/alex-bouget/Lineup",
    author="alex-bouget",
    packages=["lineup_lang", "lineup_lang.core", "lineup_lang.executor"],
    install_requires=[
        "regex",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Interpreters",
    ]
)
