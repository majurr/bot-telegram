import subprocess

def testCam(id):
    subprocess.getoutput("fswebcam -d v4l2:/dev/cam{} -S 10 --jpeg 95 --shadow --line-colour '#52d3aa' --banner-colour '#3f95ea' --title 'CIMMOV' --subtitle 'Go Ponto a Ponto' --info 'Camera #0{}: Ativa' camera{}.jpg")


def allCam():
    subprocess.getoutput("fswebcam -d v4l2:/dev/cam1 -S 10 --jpeg 95 --shadow --line-colour '#52d3aa' --banner-colour '#3f95ea' --title 'CIMMOV' --subtitle 'Go Ponto a Ponto' --info 'Camera #01: Ativa' camera1.jpg")
    subprocess.getoutput("fswebcam -d v4l2:/dev/cam2 -S 10 --jpeg 95 --shadow --line-colour '#52d3aa' --banner-colour '#3f95ea' --title 'CIMMOV' --subtitle 'Go Ponto a Ponto' --info 'Camera #02: Ativa' camera2.jpg")
    subprocess.getoutput("fswebcam -d v4l2:/dev/cam3 -S 10 --jpeg 95 --shadow --line-colour '#52d3aa' --banner-colour '#3f95ea' --title 'CIMMOV' --subtitle 'Go Ponto a Ponto' --info 'Camera #03: Ativa' camera3.jpg")
    subprocess.getoutput("fswebcam -d v4l2:/dev/cam4 -S 10 --jpeg 95 --shadow --line-colour '#52d3aa' --banner-colour '#3f95ea' --title 'CIMMOV' --subtitle 'Go Ponto a Ponto' --info 'Camera #04: Ativa' camera4.jpg")