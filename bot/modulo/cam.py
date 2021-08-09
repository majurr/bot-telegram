import subprocess
import os


def newPhoto(pathCam):
    files = os.listdir(pathCam)
    paths = [os.path.join(pathCam, basename) for basename in files]
    return max(paths, key=os.path.getctime)
