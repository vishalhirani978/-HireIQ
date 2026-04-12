import subprocess
import time
import sys
import os

os.chdir(r"D:\HireIQ\backend")

proc = subprocess.Popen(
    [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if sys.platform == 'win32' else 0
)

print(f"Backend started with PID: {proc.pid}")
print("Backend running at http://127.0.0.1:8000")

# Wait for server to start
time.sleep(3)

# Test the endpoint
import urllib.request
try:
    response = urllib.request.urlopen("http://127.0.0.1:8000/health")
    print(f"Health check: {response.read().decode()}")
except Exception as e:
    print(f"Health check failed: {e}")

print("\nBackend is running. Close this window to stop it.")
proc.wait()
