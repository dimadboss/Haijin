# -*- coding: utf-8 -*-
import telebot
import os
import constraints
import functions
import keyboards
from telebot import types
import time

haijin = telebot.TeleBot(constraints.token)
haijin_keyboard = keyboards.keyboard1

@haijin.message_handler(commands=['start'])
def first_start(message):
    haijin.send_message(message.chat.id, "Привет! Наш бот генерирует IT-хокку. Напиши /help для помощи или воспользуйся клавиатурой!", reply_markup=haijin_keyboard)

@haijin.message_handler(commands=['help'])
def help_protocol(message):
    haijin.send_message(message.chat.id, '''/tophaiku — узнать 10 лучших хокку на IT-тематику. \n
/gethaiku — сгенерировать случайное хокку на IT-тематику. \n
/abouthaiku — узнать подробнее о хокку. \n
/topwords — узнать 10 лучших слов для хокку. \n
/aboutus — узнать подробнее о разработчиках. \n
/gitrep — перейти в репозиторий проекта на GitHub. \n
''')

@haijin.message_handler(commands=['aboutus'])
def help_protocol(message):
    haijin.send_message(message.chat.id, functions.about_us())


@haijin.message_handler(commands=['topwords'])
def help_protocol(message):
    haijin.send_message(message.chat.id, functions.top_words())

@haijin.message_handler(commands=['gethaiku'])
def help_protocol(message):
    os.system(r"Hokku\Hokku Hokku\markov-wp.json Hokku\out.txt")
    handle = open(r"Hokku\out.txt", "r", encoding="utf-8")
    data = handle.read()
    haijin.send_message(message.chat.id, data)
    handle.close()


@haijin.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'топ-10 хокку' or message.text.lower() == '/tophaiku':
        rez = functions.top_haiku()
        rez2 = functions.toph_haiku2()
        haijin.send_message(message.chat.id, rez)
        haijin.send_message(message.chat.id, rez2)
    elif message.text.lower() == 'случайное it-хокку' or message.text.lower() == '/gethaiku':
        os.system(r"Hokku\Hokku Hokku\markov-wp.json Hokku\out.txt")
        handle = open(r"Hokku\out.txt", "r", encoding="utf-8")
        data = handle.read()
        haijin.send_message(message.chat.id, data)
        handle.close()
    elif message.text.lower() == 'о хокку' or message.text.lower() == '/abouthaiku':
        ab_haiku = functions.about_haiku()
        haijin.send_message(message.chat.id, ab_haiku)
    elif message.text.lower() == 'топ-10 популярных слов' or message.text.lower() == '/topwords':
        haijin.send_message(message.chat.id, functions.top_words())
    elif message.text.lower() == 'перейти в репозиторий бота на GitHub' or message.text.lower() == '/gitrep':
        bot_keyboard(message)
    elif message.text.lower() == 'о разработчиках' or message.text.lower() == '/aboutus':
        help_prot = functions.about_us()
        haijin.send_message(message.chat.id, help_prot)
    elif message.text.lower() == '/greathaijins':
        haijins_keyboard(message)
    elif message.text.lower() == 'помощь':
        haijin.send_message(message.chat.id,
    '''/tophaiku — узнать 10 лучших хокку на IT-тематику. \n
/gethaiku — сгенерировать случайное хокку на IT-тематику. \n
/abouthaiku — узнать подробнее о хокку. \n
/topwords — узнать 10 лучших слов для хокку. \n
/aboutus — узнать подробнее о разработчиках. \n
/gitrep — перейти в репозиторий проекта на GitHub. \n
/start — обновить бота, если не работают некоторые возможности. \n
''')
    else:
        haijin.send_message(message.chat.id, 'Неверная команда')


@haijin.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

@haijin.message_handler(content_types=['/gitrep'])
def bot_keyboard(message):
    keyboard = types.InlineKeyboardMarkup()
    git_button = types.InlineKeyboardButton(text = 'Перейти в репозиторий проекта на GitHub', url = "https://github.com/DdiavaLL/MyHaikuBot")
    keyboard.add(git_button)
    haijin.send_message(message.chat.id, "Репозиторий проекта!", reply_markup=keyboard)

@haijin.message_handler(content_types=['/greathaijins'])
def haijins_keyboard(message):
    keyboard = types.InlineKeyboardMarkup()
    basho_button = types.InlineKeyboardButton(text = 'Подробнее о Мацуо Басё.', url = "https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%86%D1%83%D0%BE_%D0%91%D0%B0%D1%81%D1%91")
    buson_button = types.InlineKeyboardButton(text = 'Подробнее о Ёса Бусоне.', url = "https://ru.wikipedia.org/wiki/%D0%81%D1%81%D0%B0_%D0%91%D1%83%D1%81%D0%BE%D0%BD")
    issa_button = types.InlineKeyboardButton(text = 'Подробнее о Кобаяси Иссе.', url = "https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B1%D0%B0%D1%8F%D1%81%D0%B8_%D0%98%D1%81%D1%81%D0%B0")
    siki_button = types.InlineKeyboardButton(text = 'Подробнее о Масаоке Сики.', url = "https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%81%D0%B0%D0%BE%D0%BA%D0%B0_%D0%A1%D0%B8%D0%BA%D0%B8")
    keyboard.add(basho_button)
    keyboard.add(buson_button)
    keyboard.add(issa_button)
    keyboard.add(siki_button)
    haijin.send_message(message.chat.id, "Выберите хайдзина:", reply_markup=keyboard)

haijin.polling(none_stop=True, interval=0)
