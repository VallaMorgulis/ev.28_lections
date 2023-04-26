import telebot
from telebot import types
from bs4 import BeautifulSoup
from requests import get
from my_token import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начнем')
    markup.add(btn1)
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Здравствуйте, я Ваш бот помощник! Вы можете задать мне вопрос, но в ответах я ограничен - правильно формулируйте вопрос или просто нажимайте на кнопки', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def detect_and_handle(message):
    if message.text == 'Начнем':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Оформление заказа')
        btn2 = types.KeyboardButton('Проблемы с оплатой')
        btn3 = types.KeyboardButton('Стоимость доставки')
        btn4 = types.KeyboardButton('Сроки доставки')
        btn5 = types.KeyboardButton('Оставить сообщение')
        markup1.add(btn1, btn2, btn3, btn4, btn5)   
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Выберите тему вопроса', reply_markup=markup1)

    elif message.text == 'Оформление заказа':
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Как сделать заказ", url="https://ekobambuk.ru/makeorder") #callback_data
        keyboard.add(btn1)
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Нажав на кнопку вы попадете на наш сайт и статью как сделать заказ', reply_markup=keyboard)

    elif message.text == 'Проблемы с оплатой':
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Оплата онлайн", url="https://ekobambuk.ru/payment") #callback_data
        keyboard.add(btn1)
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Оплатить ваш заказ вы можете здесь, нажав на кнопку', reply_markup=keyboard)

    elif message.text == 'Стоимость доставки':
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Стоимость доставки", url="https://ekobambuk.ru/delivery") #callback_data
        keyboard.add(btn1)
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Положить нужный товар в корзину. Перейти к оформлению и на шаге доставки вам будет доступны цена и сроки доставки как курьером так и самовывозом (ПВЗ и постаматы), а также почтой.', reply_markup=keyboard)

    elif message.text == 'Сроки доставки':
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Сроки доставки", url="https://ekobambuk.ru/delivery") #callback_data
        keyboard.add(btn1)
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Положить нужный товар в корзину. Перейти к оформлению и на шаге доставки вам будет доступны цена и сроки доставки как курьером так и самовывозом (ПВЗ и постаматы), а также почтой.', reply_markup=keyboard)

    elif message.text == 'Оставить сообщение':
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Оставить сообщение", url="https://ekobambuk.ru") #callback_data
        keyboard.add(btn1)
        chat_id = message.chat.id
        bot.send_message(chat_id, 'На любой странице сайта в правом верхнем углу есть форма: "ПОЛУЧИТЬ КОНСУЛЬТАЦИЮ ПО E-MAIL". Откройте ее и оставье нам сообщение. Мы ответим Вам.', reply_markup=keyboard)       

bot.polling(none_stop=True, interval=0)


