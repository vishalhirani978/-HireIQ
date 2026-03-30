import subprocess
import time
import sys

proc = subprocess.Popen(
    [sys.executable, "-m", "uvicorn", "main:app", "--port", "5000", "--host", "127.0.0.1"],
    cwd=r"D:\HireIQ\backend",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print(f"Backend started with PID: {proc.pid}")
print("Press Ctrl+C to stop")

try:
    proc.wait()
except KeyboardInterrupt:
    proc.terminate()
    print("Backend stopped")
