import telebot

bot = telebot.TeleBot('5512623741:AAE7OO4PNigKj_IeXbhPidcbvoDi-1RIhGw')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Ohhhhhhh'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    mess = f'Привет Dungeon master <b>{message.from_user.first_name}</b>'
    audio = open('F.mp3', 'rb')
    audio2 = open('oh.mp3', 'rb')
    audio3 = open('Sorry for what_.mp3', 'rb')
    if message.text == "fuck you":
        bot.send_audio(message.chat.id, audio)
    elif message.text == "oh shit im sorry":
        bot.send_audio(message.chat.id, audio2)
    elif message.text == "sorry for what":
        bot.send_audio(message.chat.id, audio3)
    elif message.text == "Привет Dude":
        bot.send_message(message.chat.id, mess)



bot.polling(none_stop=True)