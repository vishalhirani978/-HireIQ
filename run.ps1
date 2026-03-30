# Run HireIQ - PowerShell
Write-Host "Starting HireIQ..." -ForegroundColor Green
Write-Host ""

Write-Host "Starting Backend (FastAPI) on port 8000..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot\backend'; python -m uvicorn main:app --port 8000"

Start-Sleep -Seconds 2

Write-Host "Starting Frontend (React) on port 3000..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot\frontend'; npm start"

Write-Host ""
Write-Host "Done! Open http://localhost:3000 in your browser" -ForegroundColor Green
