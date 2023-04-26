import telebot
from telebot import types
from bs4 import BeautifulSoup
from requests import get
from my_token1 import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начнем')
    markup.add(btn1)
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Здравствуйте, я Ваш бот помощник с сайта EkoBambuk.ru! Вы можете задать мне вопрос, но в ответах я ограничен - правильно формулируйте вопроса, а лучше просто нажимайте на кнопки', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def detect_and_handle(message):
    if message.text == 'Начнем':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Оформление заказа')
        btn2 = types.KeyboardButton('Проблемы с оплатой')
        btn3 = types.KeyboardButton('Стоимость доставки')
        btn4 = types.KeyboardButton('Сроки доставки')
        btn5 = types.KeyboardButton('Оставить сообщение')
        btn6 = types.KeyboardButton('Поиск по каталогу')
        markup1.add(btn1, btn2, btn3, btn4, btn5, btn6)   
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

    elif message.text == 'Поиск по каталогу':
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, 'Введите наименование')
        bot.register_next_step_handler(msg, find_the_goods)

    else:
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, 'В ответах я ограничен. Нажимайте на кнопки, пожалуйста')

def find_the_goods(message):
    url_plus = message.text.replace(' ','+')
    url = f'https://ekobambuk.ru/products/search?sort=0&balance=&categoryId=&min_cost=&max_cost=&page=1&text={url_plus}'
    html = get_html(url)
    soup = get_soup(html)
    try:
        goodsMain = soup.find('article', class_='catalog__list catalog__list_250x190')
        goods = goodsMain.find_all('div', class_='catalog__product')
    except:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Ничего не нашли. Уточните название товара или перефразируйте.')
        detect_and_handle(message)
        return
    else:
        all_songs = get_data_catalog(goods)
        chat_id = message.chat.id
        for i in all_songs:
            name = i['name']
            price = i['price']
            link = i['url']
            msg = f'Название товара:\n"{name}"\nЦена: "{price}"\nCсылка: {link}\n\n'
            bot.send_message(chat_id, msg)
        detect_and_handle(message)

def get_html(url: str) -> str:
    response = get(url)
    return response.text

def get_soup(html: str) -> BeautifulSoup:
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_data_catalog(goods):
    res_search = []
    for item in goods:
        try:
            good_name = item.find('div', class_='product-item__link').text
        except:
            good_name = "No name"
        try:
            good_price = item.find('div', class_='product-item__price -inline-group').find('div', class_='product-item-price product-item-price_with-old').text.strip()
        except:
            good_price = "No price"
        try:   
            good_url = item.find('div', class_='product-item__link').find('a').get('href')
        except:
            good_url = "No url"
        data = {
                'name': good_name,
                'price': good_price,
                'url': good_url
            }
        res_search.append(data)
    
    return res_search

def no_search_result(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Нет такой композиции или исполнителя. Во всяком случае мы не нашли. Уточни запрос. Начнем сначала!')
    detect_and_handle(message)

bot.polling(none_stop=True, interval=0)


