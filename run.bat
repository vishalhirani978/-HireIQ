@echo off
echo Starting HireIQ Application...
echo.
echo Starting Backend Server on port 8000...
start cmd /k "cd backend && pip install -r requirements.txt > nul 2>&1 && uvicorn main:app --reload --port 8000"

timeout /t 3 /nobreak > nul

echo Starting Frontend Server on port 3000...
start cmd /k "cd frontend && npm start"

echo.
echo HireIQ is starting up!
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
pause
