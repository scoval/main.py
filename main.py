import telebot

bot = telebot.TeleBot('5592490008:AAFPsZWjADKcFe124kZWJ2ESOPjhNl6dtIs')


@bot.message_handler(commands=['start'])
def start(message):
    mass = f'' \
           f'Привет, <b>{message.from_user.first_name}</b>  <u>{message.from_user.last_name}</u>'
    bot.send_message(message.chat.id, mass, parse_mode = 'html')

@bot.message_handler()
def get_user_text(message):
    if message.text == "Как дела":
        bot.send_message(message.chat.id, "У меня нормально!", parse_mode='html')
    if message.text == "Что делаешь?":
        bot.send_message(message.chat.id, "С тобой общаюсь", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю!", parse_mode='html')

bot.polling(none_stop=False)