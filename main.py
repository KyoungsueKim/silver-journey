import asyncio
import os
import uvicorn
import subprocess
from multiprocessing import Process
from dotenv import load_dotenv

load_dotenv()
port = os.environ['BACKEND_PORT']


def frontend_run_command():
    subprocess.run(["reflex", "run", "--frontend-only"], stdout=subprocess.PIPE, text=True)


def backend_process():
    uvicorn.run(
        "silver_journey.silver_journey:app.api",
        host="0.0.0.0",
        port=int(port),
        log_level="info",
        reload=True,
    )


if __name__ == '__main__':
    frontend_process = Process(target=frontend_run_command, daemon=True)
    frontend_process.start()
    backend_process()
