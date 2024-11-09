#!/bin/sh
python setup.py bdist_wheel 
pip install --upgrade .
pip install --upgrade build --force