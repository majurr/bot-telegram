import subprocess

def get_hostname():
    return[
        subprocess.getoutput("hostname")
    ]