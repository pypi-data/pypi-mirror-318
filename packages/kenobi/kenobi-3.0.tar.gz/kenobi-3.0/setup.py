
"""
KenobiDB is a small document based DB, supporting very simple
usage including insertion, removal and basic search. Made with YAML.
Written by Harrison Erd (https://patx.github.io/)
Website: https://patx.github.io/kenobi/
"""

from distutils.core import setup

setup(name="kenobi",
    version="3.0",
    description="document based database using yaml",
    long_description=__doc__,
    author="Harrison Erd",
    author_email="harrisonerd@gmail.com",
    license="three-clause BSD",
    url="http://patx.github.io/kenobi",
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Topic :: Database"],
    py_modules=['kenobi'],
    install_requires=["pyyaml>=5.2",],)

