import psutil
import subprocess

def disk():
    return [
        subprocess.getoutput("df -H /")
    ]