import subprocess

def _run(bash_script):
    return subprocess.call(bash_script, shell=True)

def dev_server():
    return _run("uvicorn app.server:app")
