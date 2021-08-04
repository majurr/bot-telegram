import os
import subprocess

def temperatura():
    return[
        subprocess.check_output(["vcgencmd"," measure_temp"])
    ]

def reiniciar():
    return[
        subprocess.check_output(["sudo", "shutdown", "-r", "now"])
    ]
