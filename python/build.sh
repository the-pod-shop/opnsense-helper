#!/bin/sh
python setup.py bdist_wheel 
pip install --upgrade .
pip install --upgrade build --force
python /home/ji/Dokumente/podshop-org/opnsense-helper/python/opnsense_helper/examples/add_vlans.py