from modulo.sys import temperatura, reiniciar
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
    bot.send_message(message.chat.id, f"Oi, seja bem vindo. Eu sou o veículo {get_hostname()[0]}")


# função que checa todos os pré-requisitos para o funcionamento do rasp.
@bot.message_handler(commands=['check'])
def command_help(message):
    msg = f"Vou fazer uma auto análise e lhe dizer como eu estou.\n \
        Isso pode levar um tempinho...\n\nMeu IP é: {meu_ip()} \
        Meu armazenamento está assim: {disk()[0]} \n \
        Minha temperatura é de: {temperatura()[0]} \n\n \
        Ah, só relembrando. Eu sou o veículo {get_hostname()[0]} \
        Agora vou mostrar as imagens de agora que eu consegui capturar."

    bot.send_message(message.chat.id, msg)
    allCam()

    if os.path.isfile("camera1.jpg"):
        photo = open("camera1.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
        os.remove("camera1.jpg")
    if os.path.isfile("camera2.jpg"):        
        photo = open("camera2.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
        os.remove("camera2.jpg")
    if os.path.isfile("camera3.jpg"):
        photo = open("camera3.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
        os.remove("camera3.jpg")
    if os.path.isfile("camera4.jpg"):
        photo = open("camera4.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
        os.remove("camera4.jpg")

    bot.send_message(message.chat.id, 'Prontinho, status da minha saúde finalizado')


# estatísticas do disco
@bot.message_handler(commands=['space'])
def command_help(message):
    bot.send_message(message.chat.id, disk()[0])


# hostname
@bot.message_handler(commands=['bus'])
def command_help(message):
    bot.send_message(message.chat.id, get_hostname()[0])


# temperatura
@bot.message_handler(commands=['temp'])
def command_help(message):
    bot.send_message(message.chat.id, temperatura()[0])


# câmera 1
@bot.message_handler(commands=['cam1'])
def testCameras(message):
    testCam(1)
    if os.path.isfile("camera1.jpg"):
        photo = open("camera1.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
        os.remove("camera1.jpg")
    else:
        bot.reply_to(message, "Não consegui capturar imagem da camera 1")


# câmera 2
@bot.message_handler(commands=['cam2'])
def testCameras(message):
    testCam(2)
    if os.path.isfile("camera2.jpg"):
        photo = open("camera2.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
        os.remove("camera2.jpg")
    else:
        bot.reply_to(message, "Não consegui capturar imagem da camera 2")


# câmera 3
@bot.message_handler(commands=['cam3'])
def testCameras(message):
    testCam(3)
    if os.path.isfile("camera3.jpg"):
        photo = open("camera3.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
        os.remove("camera3.jpg")
    else:
        bot.reply_to(message, "Não consegui capturar imagem da camera 3")


# câmera 4
@bot.message_handler(commands=['cam4'])
def testCameras(message):
    testCam(4)
    if os.path.isfile("camera4.jpg"):
        photo = open("camera4.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
        os.remove("camera4.jpg")
    else:
        bot.reply_to(message, "Não consegui capturar imagem da camera 4")


# reboot
@bot.message_handler(commands=['reboot'])
def reboot(message):
    bot.send_message(message.chat.id, 'Ficarei indisponível por um breve momento')
    bot.reply_to(message, reiniciar()[0])


# ip
@bot.message_handler(commands=['ping'])
def ping_pong(message):
    bot.reply_to(message, f"pong... {meu_ip()}")


try:
    bot.polling(none_stop=True)
except Exception as _err:
    print(f"Error: {_err}")
