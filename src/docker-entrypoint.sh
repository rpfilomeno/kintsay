#!/bin/bash

cd /app
pip install -r requirements.txt
pip install -e . 
python tasks/agent.py