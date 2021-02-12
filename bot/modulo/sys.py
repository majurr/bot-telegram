import subprocess

def temperatura():
    return[
        subprocess.check_output(["vcgencmd"," measure_temp"])
    ]