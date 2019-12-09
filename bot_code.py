import telebot
import constraints

my_bot = telebot.TeleBot(constraints.token)

@my_bot.message_handler(content_types=['text'])
def start_message(message):
    my_bot.send_message(message.chat.id, 'Привет, ты написал мне, но пока я ничего не умею. /start')

@my_bot.message_handler(content_types=['text'])
def handle_text(message):
    print('Пришло простое сообщение!')

my_bot.polling(none_stop=True, interval=0)
