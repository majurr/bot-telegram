from modulo.sys import temperatura, reiniciar
from modulo.hostname import get_hostname
from settings import TELEGRAM_TOKEN
from modulo.network import meu_ip
from modulo.cam import newPhoto
from modulo.disk import disk

from datetime import date
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
    msg = """Vou fazer uma auto análise e lhe dizer como eu estou.\n \
        Isso pode levar um tempinho...\n\n
        Meu IP tem {}\n\n \
        Meu espaço: {} \n\n \
        Temperatura em grau Celsius é de: {} \n\n \
        Eu sou o veículo {} \n\n \
        Agora vou gerar as imagens de agora. Capturando...""".format(meu_ip(), disk()[0], temperatura()[0], get_hostname()[0])

    bot.send_message(message.chat.id, msg)
    allCam()

    try:        
        pathCam = f'/home/pi/CAMS/1/{date.today()}/' 
        newFoto = newPhoto(pathCam)
        photo = open(newFoto, "rb")
        bot.send_photo(message.chat.id, photo)
    except Exception as err:
        bot.send_message(message.chat.id, f"Não consegui capturar imagem da camera 1. {err}")
        
    try:        
        pathCam = f'/home/pi/CAMS/2/{date.today()}/' 
        newFoto = newPhoto(pathCam)
        photo = open(newFoto, "rb")
        bot.send_photo(message.chat.id, photo)
    except Exception as err:
        bot.send_message(message.chat.id, f"Não consegui capturar imagem da camera 2. {err}")
        
    try:        
        pathCam = f'/home/pi/CAMS/3/{date.today()}/' 
        newFoto = newPhoto(pathCam)
        photo = open(newFoto, "rb")
        bot.send_photo(message.chat.id, photo)
    except Exception as err:
        bot.send_message(message.chat.id, f"Não consegui capturar imagem da camera 3. {err}")
        
    try:        
        pathCam = f'/home/pi/CAMS/4/{date.today()}/' 
        newFoto = newPhoto(pathCam)
        photo = open(newFoto, "rb")
        bot.send_photo(message.chat.id, photo)
    except Exception as err:
        bot.send_message(message.chat.id, f"Não consegui capturar imagem da camera 4. {err}")

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
    try:        
        pathCam = f'/home/pi/CAMS/1/{date.today()}/' 
        newFoto = newPhoto(pathCam)
        photo = open(newFoto, "rb")
        bot.send_photo(message.chat.id, photo)
    except Exception as err:
        bot.reply_to(message, f"Não consegui capturar imagem da camera 1. {err}")


# câmera 2
@bot.message_handler(commands=['cam2'])
def testCameras(message):
    try:        
        pathCam = f'/home/pi/CAMS/2/{date.today()}/' 
        newFoto = newPhoto(pathCam)
        photo = open(newFoto, "rb")
        bot.send_photo(message.chat.id, photo)
    except Exception as err:
        bot.reply_to(message, f"Não consegui capturar imagem da camera 2. {err}")


# câmera 3
@bot.message_handler(commands=['cam3'])
def testCameras(message):
    try:        
        pathCam = f'/home/pi/CAMS/3/{date.today()}/' 
        newFoto = newPhoto(pathCam)
        photo = open(newFoto, "rb")
        bot.send_photo(message.chat.id, photo)
    except Exception as err:
        bot.reply_to(message, f"Não consegui capturar imagem da camera 3. {err}")


# câmera 4
@bot.message_handler(commands=['cam4'])
def testCameras(message):
    try:        
        pathCam = f'/home/pi/CAMS/4/{date.today()}/' 
        newFoto = newPhoto(pathCam)
        photo = open(newFoto, "rb")
        bot.send_photo(message.chat.id, photo)
    except Exception as err:
        bot.reply_to(message, f"Não consegui capturar imagem da camera 4. {err}")


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
