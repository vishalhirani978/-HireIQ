@echo off
echo Starting HireIQ Backend and Frontend...
echo.
echo Starting Backend on port 8000...
start "HireIQ Backend" cmd /k "cd /d %~dp0backend && python -m uvicorn main:app --port 8000 --host 127.0.0.1"
timeout /t 3 /nobreak >nul
echo Starting Frontend on port 3000...
start "HireIQ Frontend" cmd /k "cd /d %~dp0frontend && npm start"
echo.
echo Both servers started!
echo Backend: http://127.0.0.1:8000
echo Frontend: http://localhost:3000
echo.
pause
