#!/bin/bash
. env/bin/activate
export FLASK_DEBUG=ON
flask run
deactivate
