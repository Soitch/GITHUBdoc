<<<<<<< HEAD
#! /usr/bin/python3
=======
#!/usr/bin/python3
>>>>>>> 5c366e3ea3179c59971767d1a94cfcd429f13803
import config
import telebot

# Создаем экземпляр бота
bot = telebot.TeleBot(os.getenv("TELEGRAM_API_TOKEN"))
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)
