#!/bin/bash

# git add .
# git commit -m $1
# git push


rm -rf dist
rm -rf build
python -m pip install --upgrade pip setuptools wheel twine ez_setup
python setup.py sdist
python -m twine upload dist/*
