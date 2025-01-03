#!/bin/bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine
# "pkginfo" solves the issue of "InvalidDistribution: Metadata is missing required fields: Name, Version."
python3 -m pip install --upgrade pkginfo

python3 -m build
python3 -m twine upload --repository testpypi dist/*
