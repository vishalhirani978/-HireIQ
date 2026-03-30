@echo off
echo Starting HireIQ...
echo.
echo Starting Backend (FastAPI) on port 8000...
start "Backend" cmd /k "cd /d %~dp0backend && python -m uvicorn main:app --port 8000"
timeout /t 2 /nobreak >nul
echo.
echo Starting Frontend (React) on port 3000...
start "Frontend" cmd /k "cd /d %~dp0frontend && npm start"
echo.
echo Done! Open http://localhost:3000 in your browser
pause
