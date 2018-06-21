#!/bin/bash

TAG=v`cat generic_encoders/VERSION`

git tag $TAG
git push origin $TAG

rm -r build/ dist/ ./*.egg-info/

python setup.py sdist bdist_wheel

twine upload -r pypi dist/*
