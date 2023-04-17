import telebot 
from telebot import types
import random

token = '6269999223:AAHc9kaAIuoLZ2zs3veGx9GgOjl9EA-kD-E' #'Введите свой токен'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('Играть')
button2 = types.KeyboardButton('Нет')

keyboard.add(button1, button2)

@bot.message_handler(commands=['start', 'game'])
def start_message(message):
  message2 = bot.send_message(message.chat.id, 'Привет, начнем игру?', reply_markup=keyboard)
  bot.register_next_step_handler(message2, check_answer)

def check_answer(message):
  if message.text == 'Играть':
    bot.send_message(message.chat.id, 'Хорошо, тогда вот правила, нужно угадать число за 3 попытки')
    random_number = random.choice(range(1, 11))
    print(random_number)
    game(message, 3, random_number)
  else:
    bot.send_message(message.chat.id, 'Пока')

def game(message, attempts, random_number):
  message2 = bot.send_message(message.chat.id, 'Введи число')
  bot.register_next_step_handler(message2, check_number, attempts-1, random_number)
  
def check_number(message, attempts, random_number):
  if message.text == str(random_number):
    bot.send_message(message.chat.id, 'Вы победили')
  elif attempts == 0:
    bot.send_message(message.chat.id, 'Извините, у вас закончились попытки')
  else:
    bot.send_message(message.chat.id, 'Попробуйте еще раз')
    game(message, attempts, random_number)

bot.polling()