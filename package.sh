#!/bin/bash

rm -r build/ dist/ ./*.egg-info/

python setup.py sdist bdist_wheel

twine upload -r pypi dist/*
