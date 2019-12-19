import telebot
from telebot import types
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.add('Топ-10 хокку', 'Случайное IT-хокку')
keyboard1.add('О хокку', 'Топ-10 слов для хокку')
keyboard1.add('О разработчиках', 'Помощь')