#-*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot 
import os

bot = ChatBot('teste') #Adicionar -->ChatBot('teste', read_only=True)<-- quando o Bot estiver treinado. 
bot.set_trainer(ListTrainer)

for arq in os.listdir('arq'):
    chat = open('arq/' + arq, 'r').readlines()
    bot.train(chat)

while True:
    resq = input('Você: ')

    resp = bot.get_response(resq)
    print('Bot: '+ str(resp))
