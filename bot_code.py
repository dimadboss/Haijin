import telebot
import constraints
from telebot import types
my_bot = telebot.TeleBot(constraints.token)

@my_bot.message_handler(commands=['start'])
def first_start(message):
    my_bot.send_message(message.chat.id, "Привет! Наш бот генерирует IT-хокку. Напиши /help для помощи или воспользуйся клавиатурой!")

@my_bot.message_handler(commands=['help'])
def help_protocol(message):
    my_bot.send_message(message.chat.id, "FIX ME!")

@my_bot.message_handler(content_types=['text'])
def bot_keyboard(message):
    keyboard = types.InlineKeyboardMarkup()
    git_button = types.InlineKeyboardButton(text = 'Перейти в репозиторий проекта на GitHub', url = "https://github.com/DdiavaLL/MyHaikuBot")
    keyboard.add(git_button)
    my_bot.send_message(message.chat.id, "Выбери одну из следующих возможностей бота.", reply_markup=keyboard)



my_bot.polling(none_stop=True, interval=0)
