import telebot
#Telegram Bot

bot = telebot.TeleBot("1305315597:AAGNEio0BA6l547l_5MjFANfmMdmUDOkozQ")

@bot.message_handler(commands=["start","help"])
def send_welcome(message):
    bot.send_message(message.chat.id, str("Привет, я загадал число от 1 до 100. Попробуй отгадать."))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    import random
    i = random.randint(1,100)
    def new():
        if int(message.text) == int(i):
            bot.send_message(message.chat.id, str("Ура"))
        elif int(message.text) > int(i):
            bot.send_message(message.chat.id, str("Число меньше"))

        elif int(message.text) < int(i):
            bot.send_message(message.chat.id, str("Число больше"))
    new()
bot.polling()

