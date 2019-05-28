@echo off
setx path "%~dp0;%path%"
pip install virtualenv
virtualenv venv
pip install -r requirements.txt