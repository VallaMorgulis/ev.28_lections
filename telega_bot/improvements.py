import telebot
from telebot import types
import random

token = '6070876181:AAEbXSEX_q7I6y1RhZ2xQAR3IrQkdf7pceg'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Играть!')
btn2 = types.KeyboardButton('Нет, я Пасс!')
btn_start = types.KeyboardButton('start')
keyboard.add(btn1, btn2)


@bot.message_handler(commands=['start', 'game'])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, 'Привет King, начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(bot_message, check_answer)

def check_answer(message):
    if message.text == 'Играть!':
        bot.send_message(message.chat.id, 'Ok, тогда лови правила игры:\nНужно угадать число которое я загадаю в диапазоне от 1 до 10 включительно! У тебя будет 3 попытки. Если не угадаешь я тебя утоплю! :)')
        number = random.randint(1, 10)
        print(number, '!!!')
        game(message, 3, number)
    elif message.text == 'Нет, я Пасс!':
        bot.send_message(message.chat.id, 'Net tak net, Poka!')
    else:
        bot_message = bot.send_message(message.chat.id, 'Вы ввели неправильный ответ!\nВведите новый: ', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, check_answer)


def game(message, attempts, number):
    message_bot = bot.send_message(message.chat.id, 'Выбери число: ')
    bot.register_next_step_handler(message_bot, check_number, attempts-1, number)

def check_number(message, attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'Вы победили! Нарекаю Вас удачливым!')
    elif attempts == 0:
        bot.send_message(message.chat.id, 'К сожалению Вы проиграли!')
    else:
        bot.send_message(message.chat.id, 'Нет, ты не угадал число. Поробуй еще раз')
        game(message, attempts, number)

bot.polling()