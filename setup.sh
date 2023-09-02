#!/bin/bash
rm -fr env
python3 -m venv env
. env/bin/activate
python3 -m pip install --upgrade -r requirement.txt
python3 -m pip cache purge
