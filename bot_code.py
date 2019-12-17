import telebot
import constraints
import functions
import keyboards
from telebot import types

haijin = telebot.TeleBot(constraints.token)
haijin_keyboard = keyboards.keyboard1

@haijin.message_handler(commands=['start'])
def first_start(message):
    haijin.send_message(message.chat.id, "Привет! Наш бот генерирует IT-хокку. Напиши /help для помощи или воспользуйся клавиатурой!", reply_markup=haijin_keyboard)

@haijin.message_handler(commands=['help'])
def help_protocol(message):
    haijin.send_message(message.chat.id, '''/tophaiku — узнать 10 лучших хокку на IT-тематику. \n
/gethaiku — сгенерировать хокку на IT-тематику по слову. \n
/abouthaiku — узнать подробнее о хокку. \n
/topwords — узнать 10 лучших слов для хокку. \n
/aboutus — узнать подробнее о разработчиках. \n
/gitrep — перейти в репозиторий проекта на GitHub. \n
''')

@haijin.message_handler(commands=['about'])
def help_protocol(message):
    haijin.send_message(message.chat.id, functions.about())

@haijin.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'топ-10 хокку' or message.text.lower() == '/tophaiku':
        rez = functions.top_haiku()
        haijin.send_message(message.chat.id, rez)
    elif message.text.lower() == 'it-хокку по слову' or message.text.lower() == '/gethaiku':
        haijin.send_message(message.chat.id, '**Сгененировать хокку по заданному слову**')
    elif message.text.lower() == 'о хокку' or message.text.lower() == '/abouthaiku':
        haijin.send_message(message.chat.id, '**Выдать информацию о хокку**')
    elif message.text.lower() == 'топ-10 слов для хокку' or message.text.lower() == '/topword':
        haijin.send_message(message.chat.id, '**Выдать 10 наиболее популярных слов для хокку**')
    elif message.text.lower() == 'перейти в репозиторий бота на GitHub' or message.text.lower() == '/gitrep':
        bot_keyboard(message)
    elif message.text.lower() == 'о разработчиках' or message.text.lower() == '/aboutus':
        help_prot = functions.about()
        haijin.send_message(message.chat.id, help_prot)
    elif message.text.lower() == 'помощь':
        haijin.send_message(message.chat.id,
    '''/tophaiku — узнать 10 лучших хокку на IT-тематику. \n
/gethaiku — сгенерировать хокку на IT-тематику по слову. \n
/abouthaiku — узнать подробнее о хокку. \n
/topwords — узнать 10 лучших слов для хокку. \n
/aboutus — узнать подробнее о разработчиках. \n
/gitrep — перейти в репозиторий проекта на GitHub. \n
''')
    else:
        haijin.send_message(message.chat.id, '**Неверная команда**')


@haijin.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

@haijin.message_handler(content_types=['/gitrep'])
def bot_keyboard(message):
    keyboard = types.InlineKeyboardMarkup()
    git_button = types.InlineKeyboardButton(text = 'Перейти в репозиторий проекта на GitHub', url = "https://github.com/DdiavaLL/MyHaikuBot")
    keyboard.add(git_button)
    haijin.send_message(message.chat.id, "Выбери одну из следующих возможностей бота.", reply_markup=keyboard)



haijin.polling(none_stop=True, interval=0)
