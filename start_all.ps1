# Start both servers for HireIQ

Write-Host "Starting HireIQ Backend on port 8000..." -ForegroundColor Cyan

# Start backend in new window
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd D:\HireIQ\backend; python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload"

# Wait for backend to start
Start-Sleep -Seconds 3

# Test backend health
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/health" -UseBasicParsing -TimeoutSec 5
    if ($response.StatusCode -eq 200) {
        Write-Host "Backend is running at http://127.0.0.1:8000" -ForegroundColor Green
    }
} catch {
    Write-Host "Warning: Backend health check failed. It may still be starting..." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Starting HireIQ Frontend on port 3000..." -ForegroundColor Cyan

# Start frontend
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd D:\HireIQ\frontend; npm start"

Write-Host ""
Write-Host "Both servers should be starting!" -ForegroundColor Green
Write-Host "- Backend API: http://localhost:8000" -ForegroundColor Yellow
Write-Host "- Frontend UI: http://localhost:3000" -ForegroundColor Yellow
