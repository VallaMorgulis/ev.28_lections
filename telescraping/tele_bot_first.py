import telebot 
from telebot import types
import random
from my_token import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Как стать автором на Хабре?')
        btn2 = types.KeyboardButton('Правила сайта')
        btn3 = types.KeyboardButton('Советы по оформлению публикации')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'Как стать автором на Хабре?':
        bot.send_message(message.from_user.id, 'Вы пишете первый пост, его проверяют модераторы, и, если всё хорошо, отправляют в основную ленту Хабра, где он набирает просмотры, комментарии и рейтинг. В дальнейшем премодерация уже не понадобится. Если с постом что-то не так, вас попросят его доработать.\n \nПолный текст можно прочитать по ' + '[ссылке](https://habr.com/ru/sandbox/start/)', parse_mode='Markdown')

    elif message.text == 'Правила сайта':
        bot.send_message(message.from_user.id, 'Прочитать правила сайта вы можете по ' + '[ссылке](https://habr.com/ru/docs/help/rules/)', parse_mode='Markdown')

    elif message.text == 'Советы по оформлению публикации':
        bot.send_message(message.from_user.id, 'Подробно про советы по оформлению публикаций прочитать по ' + '[ссылке](https://habr.com/ru/docs/companies/design/)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть


# keyboard = types.ReplyKeyboardMarkup()
# # button1 = types.KeyboardButton('Искать фильм')
# button2 = types.KeyboardButton('/start')

# keyboard.add(button2)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot_message = bot.send_message(message.chat.id, 'Привет. Я помогу тебе выбрать фильм.\nВведите название фильма', reply_markup=keyboard) # , reply_markup=keyboard
#     bot.register_next_step_handler(bot_message, 'Ищу')
#     print(bot_message.text)
    # search(message)        #   bot.register_next_step_handler(message2, check_answer)

# def check_answer(message):
#   if message.text:
#     bot.send_message(message.chat.id, 'Готов?')
#     bot.register_next_step_handler(message, search(message))
    # search(message)


    # random_number = random.choice(range(1, 11))
    # print(random_number)
    # game(message, 3, random_number)
#   else:
#     bot.send_message(message.chat.id, 'Пока')

# def search(message):
#     message2 = bot.send_message(message.chat.id, 'Введите название фильма')
#     bot.register_next_step_handler(message2)
#     print(message2)
  
# def check_number(message, attempts, random_number):
#   if message.text == str(random_number):
#     bot.send_message(message.chat.id, 'Вы победили')
#   elif attempts == 0:
#     bot.send_message(message.chat.id, 'Извините, у вас закончились попытки')
#   else:
#     bot.send_message(message.chat.id, 'Попробуйте еще раз')
#     game(message, attempts, random_number)

# bot.polling()