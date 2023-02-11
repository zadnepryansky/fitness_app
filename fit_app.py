import telebot
from telebot import types
from exercises_youtube_links import Legs
from Constants import API_KEY

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u> </b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
    elif message.text == 'photo':
        photo = open('gym.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'приседания в смитте'.lower():
        squats_in_smith = Legs.squats_in_smith
        bot.send_message(message.chat.id, squats_in_smith)
    elif message.text == 'гиперэкстензия'.lower():
        hyperextension = Legs.hyperextension
        bot.send_message(message.chat.id, hyperextension)
    else:
        bot.send_message(message.chat.id, f'уупс, попробуй еще раз', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Фото сохранено')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Instagram', url='https://www.instagram.com/zadnepryansky/'))
    bot.send_message(message.chat.id, 'Перейти', reply_markup=markup)


@bot.message_handler(commands=['exercises'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Web site')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейти', reply_markup=markup)

bot.polling(none_stop=True)
