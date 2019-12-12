import telebot

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.add('Топ-10 хокку', 'IT-хокку по слову')
keyboard1.add('О хокку', 'Топ-10 слов для хокку')
keyboard1.add('О разработчиках', 'Помощь')