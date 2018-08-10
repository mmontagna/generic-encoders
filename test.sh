#!/bin/bash
echo python3
./venv3/bin/python -m unittest discover test/

echo python2
./venv/bin/python -m unittest discover test/

