import telebot
from telebot import types
import random
from exercises_youtube_links import ALL_EXERCISES
from Constants import API_KEY

bot = telebot.TeleBot(API_KEY)


# Top button messages
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🎲 Случайное упражнение')
    item2 = types.KeyboardButton('💪 Упражения')
    item3 = types.KeyboardButton('🥗 Питание')
    item4 = types.KeyboardButton('📲 Тренер')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, f'Привет 👋, {message.from_user.first_name}!'
                                      f'\n'
                                      f'Этот бот покажет тебе правильную технику упражнений.'
                                      f'\n'
                                      f'Тут ты найдешь все что нужно для твоих тренировок'
                                      f'\n'
                                      f'\n'
                                      f'Перемещайся по меню внизу ⬇️ и выбирай все что тебе нужно 💪'
                                      f'\n'
                                      f'Если пропало меню напиши /start 😊, хороших тренировок 💪', reply_markup=markup)


# get message in console
@bot.message_handler(content_types=['text'])
def bot_message(message):
    random_exercises = ALL_EXERCISES
    # from text in console
    if message.chat.type == 'private':
        if message.text == '🎲 Случайное упражнение':
            bot.send_message(message.chat.id, 'Упражнение: ' + random.choice(random_exercises))
        elif message.text == '💪 Упражения':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('👉 Ноги / Ягодицы')
            item2 = types.KeyboardButton('👉 Грудь')
            item3 = types.KeyboardButton('👉 Спина')
            item4 = types.KeyboardButton('👉 Плечи')
            item5 = types.KeyboardButton('👉 Руки')
            item6 = types.KeyboardButton('👉 Пресс')
            back = types.KeyboardButton('◀️ Назад')
            markup.add(item1, item2, item3, item4, item5, item6, back)

            bot.send_message(message.chat.id, 'Упражения', reply_markup=markup)
        # legs
        elif message.text == '👉 Ноги / Ягодицы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Гиперэкстензия')
            item17 = types.KeyboardButton('Жим ногами')
            item2 = types.KeyboardButton('Румынская тяга со штангой')
            item3 = types.KeyboardButton('Зашагивания на тумбу')
            item4 = types.KeyboardButton('Махи в кроссовере')
            item5 = types.KeyboardButton('Обратные выпады')
            item6 = types.KeyboardButton('Разведения ног')
            item7 = types.KeyboardButton('Махи в сторону в кроссовере')
            item8 = types.KeyboardButton('Махи с утяжелителями')
            item9 = types.KeyboardButton('Ягодичный мостик по 1 ноге')
            item10 = types.KeyboardButton('Приседания с гантелями')
            item11 = types.KeyboardButton('Болгарские выпады')
            item12 = types.KeyboardButton('Приседания + румынская тяга')
            item13 = types.KeyboardButton('Приседания “Суммо”')
            item14 = types.KeyboardButton('Румынская тяга со штангой')
            item15 = types.KeyboardButton('Ягодичный мостик со штангой')
            item16 = types.KeyboardButton('Приседания со штангой в Смитте')
            back = types.KeyboardButton('◀️ Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7,
                       item8, item9, item10, item11, item12, item13,
                       item14, item15, item16, item17, back)

            bot.send_message(message.chat.id, 'Ноги / Ягодицы', reply_markup=markup)
        # chest muscles
        elif message.text == '👉 Грудь':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Жим гантелей под углом')
            item2 = types.KeyboardButton('Разведения гантелей под углом')

            back = types.KeyboardButton('◀️ Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Грудь', reply_markup=markup)
        # back muscles
        elif message.text == '👉 Спина':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Тяга верхнего блока к груди')
            item2 = types.KeyboardButton('Тяга среднего блока к груди')
            item3 = types.KeyboardButton('Тяга с канатом за голову')
            item4 = types.KeyboardButton('Тяга на скамье с гантелей')
            item5 = types.KeyboardButton('Тяга к поясу с гантелями')
            item6 = types.KeyboardButton('Тяга верхнего блока за паралельные ручки')

            back = types.KeyboardButton('◀️ Назад')
            markup.add(item1, item2, item3, item4, item5, item6, back)

            bot.send_message(message.chat.id, 'Спина', reply_markup=markup)

        elif message.text == '👉 Плечи':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Подъем блина перед собой')
            item2 = types.KeyboardButton('Махи гантелей в стороны')
            item3 = types.KeyboardButton('Жим гантелей сидя')
            item4 = types.KeyboardButton('Задняя дельта с канатом')
            item5 = types.KeyboardButton('Повороты блина перед собой')
            item6 = types.KeyboardButton('Тяга штанги к груди')

            back = types.KeyboardButton('◀️ Назад')
            markup.add(item1, item2, item3, item4, item5, item6, back)

            bot.send_message(message.chat.id, 'Плечи', reply_markup=markup)

        elif message.text == '👉 Руки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Молотки стоя')
            item2 = types.KeyboardButton('Трицепс стоя с канатом')
            item3 = types.KeyboardButton('Отжимания от скамьи')
            item4 = types.KeyboardButton('Трицепс лежа с гантелями')

            back = types.KeyboardButton('◀️ Назад')
            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, 'Руки', reply_markup=markup)
        # abs
        elif message.text == '👉 Пресс':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🙃 Легче')
            item2 = types.KeyboardButton('😎 Сложнее')
            back = types.KeyboardButton('◀️ Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Пресс', reply_markup=markup)
        elif message.text == '🙃 Легче':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Пресс с гантелей лежа')
            item2 = types.KeyboardButton('Пресс лежа ноги под углом')
            item3 = types.KeyboardButton('Пресс в статике “Маятник”')
            back = types.KeyboardButton('◀️ Назад')
            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, '🙃 Легче / Пресс', reply_markup=markup)

        elif message.text == '😎 Сложнее':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Боковая планка')
            item2 = types.KeyboardButton('Планка “Перекаты”')
            item3 = types.KeyboardButton('Подъемы коленей к груди')
            back = types.KeyboardButton('◀️ Назад')
            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, '😎 Сложнее / Пресс', reply_markup=markup)
        # nutrition
        elif message.text == '🥗 Питание':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('📍 Принципы питания')
            item2 = types.KeyboardButton('🤩 Лучшие продукты для фитнеса')
            back = types.KeyboardButton('◀️ Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Питание', reply_markup=markup)

        elif message.text == '◀️ Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🎲 Случайное упражнение')
            item2 = types.KeyboardButton('💪 Упражения')
            item3 = types.KeyboardButton('🥗 Питание')
            item4 = types.KeyboardButton('📲 Тренер')
            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)

        elif message.text == '📲 Тренер':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('📲 Instagram')
            item2 = types.KeyboardButton('📲 Telegram')
            back = types.KeyboardButton('◀️ Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Тренер', reply_markup=markup)
            # bot.send_message(message.chat.id, 'https://www.instagram.com/zadnepryansky/')

        elif message.text == 'Гиперэкстензия':
            ex = 'https://www.youtube.com/shorts/eYLPbzC1Xjs'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Румынская тяга со штангой':
            ex = 'https://www.youtube.com/shorts/UOyAHw0Ne08'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Зашагивания на тумбу':
            ex = 'https://youtube.com/shorts/DtOnHQoVkYU'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Жим ногами':
            ex = 'https://youtu.be/zVgrqY5ECeo'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Махи в кроссовере':
            ex = 'https://youtube.com/shorts/LmNcz9vy2ok'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Обратные выпады':
            ex = 'https://youtube.com/shorts/Z2MhvccsvuE'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Разведения ног':
            ex = 'https://youtube.com/shorts/y4ToTbDFD2g'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Махи в сторону в кроссовере':
            ex = 'https://youtube.com/shorts/Ghur7a-uBIw'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Румынская тяга с гантелями':
            ex = 'https://youtube.com/shorts/w0Me5DXFdx4'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Сведения ног':
            ex = 'https://youtube.com/shorts/tFqPGwjnlUY'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Махи с утяжелителями':
            ex = 'https://youtube.com/shorts/qMjyFu-22dA'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Ягодичный мостик по 1 ноге':
            ex = 'https://youtube.com/shorts/EDMzoe1Lpz4'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Приседания с гантелями':
            ex = 'https://youtube.com/shorts/5GmJbQRj3RY'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Болгарские выпады':
            ex = 'https://youtube.com/shorts/y0duVVnwthA'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Приседания + румынская тяга':
            ex = 'https://youtube.com/shorts/sLNUEMatAcQ?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Приседания “Суммо”':
            ex = 'https://youtube.com/shorts/lDEvck9nQsA?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Ягодичный мостик со штангой':
            ex = 'https://youtube.com/shorts/WDNsSGOsodw?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Приседания со штангой в Смитте':
            ex = 'https://youtube.com/shorts/HKNM--vxXl0'
            bot.send_message(message.chat.id, ex)

        elif message.text == 'Жим гантелей под углом':
            ex = 'https://youtube.com/shorts/ofB6Uuw6FG0'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Разведения гантелей под углом':
            ex = 'https://youtube.com/shorts/1nuULE0LOsU'
            bot.send_message(message.chat.id, ex)

        elif message.text == 'Тяга верхнего блока к груди':
            ex = 'https://youtube.com/shorts/tSfYGisrkLo'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Тяга среднего блока к груди':
            ex = 'https://www.youtube.com/shorts/PQD0ZlLiDEg'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Тяга с канатом за голову':
            ex = 'https://youtube.com/shorts/QUR4mccMmho?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Тяга на скамье с гантелей':
            ex = 'https://youtube.com/shorts/gQhpzRD4fNI?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Тяга к поясу с гантелями':
            ex = 'https://youtube.com/shorts/gQNR0qjFgTg?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Тяга верхнего блока за паралельные ручки':
            ex = 'https://youtube.com/shorts/udgP-HZ-BPU?feature=share'
            bot.send_message(message.chat.id, ex)

        elif message.text == 'Подъем блина перед собой':
            ex = 'https://youtube.com/shorts/uKqxrMMc1wQ'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Махи гантелей в стороны':
            ex = 'https://youtube.com/shorts/JtT7ZZ4jMN4'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Жим гантелей сидя':
            ex = 'https://youtube.com/shorts/LkooGlXo3-k'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Задняя дельта с канатом':
            ex = 'https://youtube.com/shorts/fY2tBsiH1e4?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Повороты блина перед собой':
            ex = 'https://youtube.com/shorts/ahc4Ls1tZe0?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Тяга штанги к груди':
            ex = 'https://youtube.com/shorts/9peqAqQcYdc?feature=share'
            bot.send_message(message.chat.id, ex)

        elif message.text == 'Молотки стоя':
            ex = 'https://youtube.com/shorts/pIBbyu4WUI4'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Трицепс стоя с канатом':
            ex = 'https://youtube.com/shorts/1hWbK820VFA?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Отжимания от скамьи':
            ex = 'https://youtube.com/shorts/prI8NAj7FKU?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Трицепс лежа с гантелями':
            ex = 'https://youtube.com/shorts/LvEMx49KIdo'
            bot.send_message(message.chat.id, ex)

        elif message.text == 'Пресс с гантелей лежа':
            ex = 'https://youtube.com/shorts/9LCQFNvmkg0?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Пресс лежа ноги под углом':
            ex = 'https://youtube.com/shorts/Yi-j91p0A8M?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Пресс в статике “Маятник”':
            ex = 'https://youtube.com/shorts/7ToZVrEZZH0?feature=share'
            bot.send_message(message.chat.id, ex)

        elif message.text == 'Боковая планка':
            ex = 'https://youtube.com/shorts/ZxHpe9_a068?feature=share'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Планка “Перекаты”':
            ex = 'https://youtube.com/shorts/sAfLfgVKyuo'
            bot.send_message(message.chat.id, ex)
        elif message.text == 'Подъемы коленей к груди':
            ex = 'https://youtube.com/shorts/vJwAGIYIObU'
            bot.send_message(message.chat.id, ex)

        elif message.text == '📲 Instagram':
            bot.send_message(message.chat.id, 'https://www.instagram.com/zadnepryansky/')
        elif message.text == '📲 Telegram':
            bot.send_message(message.chat.id, 'https://t.me/zadnepryansky')


bot.polling(none_stop=True)
