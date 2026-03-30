@echo off
cd /d %~dp0backend
python -m uvicorn main:app --port 8000 --host 0.0.0.0
