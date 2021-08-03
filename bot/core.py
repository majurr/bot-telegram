from modulo.sys import temperatura, reboot
from modulo.hostname import get_hostname
from modulo.cam import testCam, allCam
from settings import TELEGRAM_TOKEN
from modulo.network import meu_ip
from modulo.disk import disk

import subprocess
import telebot
import os


bot = telebot.TeleBot(TELEGRAM_TOKEN)


# boas vindas
@bot.message_handler(commands=['start','hi'])
def command_help(message):
    host = subprocess.getoutput('hostname')
    bot.reply_to(message, f"Olá seja bem vindo ao veículo {host}")


# função que checa todos os pré-requisitos para o funcionamento do rasp.
@bot.message_handler(commands=['saude'])
def command_help(message):
    bot.reply_to(message, "hostname: {}\nip: {}\nespaço em disco:\n{}\ntemperatura: {}".format(get_hostname()[0], meu_ip(), disk()[0], temperatura()[0]))
    allCam()

    if os.path.isfile("camera1.jpg"):
        photo = open("camera1.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
    if os.path.isfile("camera2.jpg"):        
        photo = open("camera2.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
    if os.path.isfile("camera3.jpg"):
        photo = open("camera3.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
    if os.path.isfile("camera4.jpg"):
        photo = open("camera4.jpg", "rb")
        bot.send_photo(message.chat.id, photo)

    bot.send_message(message.chat.id, 'Check-up finalizado')


# estatísticas do disco
@bot.message_handler(commands=['space'])
def command_help(message):
    bot.reply_to(message, disk()[0])


# hostname
@bot.message_handler(commands=['bus'])
def command_help(message):
    bot.reply_to(message, get_hostname()[0])


# temperatura
@bot.message_handler(commands=['temp'])
def command_help(message):
    bot.reply_to(message, temperatura()[0])


# câmera 1
@bot.message_handler(commands=['cam1'])
def testCameras(message):
    testCam(1)
    if os.path.isfile("camera1.jpg"):
        photo = open("camera1.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
    else:
        bot.reply_to(message, "Não consegui capturar imagem da camera 1")


# câmera 2
@bot.message_handler(commands=['cam2'])
def testCameras(message):
    testCam(2)
    if os.path.isfile("camera2.jpg"):
        photo = open("camera2.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
    else:
        bot.reply_to(message, "Não consegui capturar imagem da camera 2")


# câmera 3
@bot.message_handler(commands=['cam3'])
def testCameras(message):
    testCam(3)
    if os.path.isfile("camera3.jpg"):
        photo = open("camera3.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
    else:
        bot.reply_to(message, "Não consegui capturar imagem da camera 3")


# câmera 4
@bot.message_handler(commands=['cam4'])
def testCameras(message):
    testCam(4)
    if os.path.isfile("camera4.jpg"):
        photo = open("camera4.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
    else:
        bot.reply_to(message, "Não consegui capturar imagem da camera 4")


# reboot
@bot.message_handler(commands=['reboot'])
def reboot(message):
    bot.reply_to(message, "Ficarei um tempo indisponível. Reiniciando...")
    reboot()


# ip
@bot.message_hangler(commands=['ping'])
def ping_pong(message):
    bot.reply_to(message, f"pong... {meu_ip()}")


bot.polling()
