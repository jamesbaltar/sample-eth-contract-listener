#!/bin/bash

python3 -m venv env
env/bin/python -m pip install -r requirements.txt
env/bin/python ./manage.py migrate

echo "Done with setup"
echo "============================"
echo "venv is on <project_root>/env. To use: source env/bin/activate"
echo "Run server with: make start"
echo "Run transfer listener with: make listen"
echo "============================"
