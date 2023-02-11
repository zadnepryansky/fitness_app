import telebot
from telebot import types
import random
from exercises_youtube_links import ALL_EXERCISES, POSTERIOR_THIGH
from Constants import API_KEY

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Случайное упражнение')
    item2 = types.KeyboardButton('Верх тела')
    item3 = types.KeyboardButton('Ноги')
    item4 = types.KeyboardButton('Пресс')
    item5 = types.KeyboardButton('Другое')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    random_exercises = ALL_EXERCISES
    if message.chat.type == 'private':
        if message.text == 'Случайное упражнение':
            bot.send_message(message.chat.id, 'Упражнение: ' + random.choice(random_exercises))
        elif message.text == 'Верх тела':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Спина')
            item2 = types.KeyboardButton('Грудь')
            item3 = types.KeyboardButton('Плечи')
            item4 = types.KeyboardButton('Руки')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, 'Верх тела', reply_markup=markup)

        elif message.text == 'Ноги':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Ягодицы')
            item2 = types.KeyboardButton('Задняя поверхность бедра')
            item3 = types.KeyboardButton('Комплексно')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, 'Ноги', reply_markup=markup)

        elif message.text == 'Пресс':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Легко')
            item2 = types.KeyboardButton('Сложнее')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Пресс', reply_markup=markup)

        elif message.text == 'Другое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Настройки')
            item2 = types.KeyboardButton('Подписка')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Другое', reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Случайное упражнение')
            item2 = types.KeyboardButton('Верх тела')
            item3 = types.KeyboardButton('Ноги')
            item4 = types.KeyboardButton('Пресс')
            item5 = types.KeyboardButton('Другое')

            markup.add(item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)

        elif message.text == 'Подписка':
            bot.send_message(message.chat.id, 'https://www.instagram.com/zadnepryansky/')

        elif message.text == 'Задняя поверхность бедра':
            bot.send_message(message.chat.id, POSTERIOR_THIGH)













#         bot.send_photo(message.chat.id, photo)
#     elif message.text == 'приседания в смитте'.lower():
#         squats_in_smith = Legs.squats_in_smith
#         bot.send_message(message.chat.id, squats_in_smith)
#     elif message.text == 'гиперэкстензия'.lower():
#         hyperextension = Legs.hyperextension
#         bot.send_message(message.chat.id, hyperextension)
#     else:
#         bot.send_message(message.chat.id, f'уупс, попробуй еще раз', parse_mode='html')
#
#
# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, 'Фото сохранено')
#
#
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Instagram', url='https://www.instagram.com/zadnepryansky/'))
#     bot.send_message(message.chat.id, 'Перейти', reply_markup=markup)
#
#
# @bot.message_handler(commands=['exercises'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     website = types.KeyboardButton('Web site')
#     start = types.KeyboardButton('Start')
#     markup.add(website, start)
#     bot.send_message(message.chat.id, 'Перейти', reply_markup=markup)

bot.polling(none_stop=True)
