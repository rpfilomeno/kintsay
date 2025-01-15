#!/bin/bash
cd /app
python -m venv venv
pip install -r requirements.txt
pip install -e .
python tasks/agent.py
