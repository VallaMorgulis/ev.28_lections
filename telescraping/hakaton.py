import telebot
from telebot import types
from bs4 import BeautifulSoup
from requests import get
from my_token import token
from parsing import pars_all_news, pars_1news

bot = telebot.TeleBot(token)
url = 'https://kaktus.media/?lable=8&date=2023-04-24&order=time'

list_parsed = None
ch = 0

@bot.message_handler(commands=['start'])
def start(message):
    global list_parsed  
    global ch  
    list_parsed = pars_all_news(url)
    msg_list = []
    for i in list_parsed:
        num_ = i['n']
        name = i['name']
        msg = f'Номер: "{num_}"\nСтатья: "{name}"\n\n'
        msg_list.append(msg)
        all_msg = ''.join(msg_list)

    chat_id = message.chat.id
    bot.send_message(chat_id, all_msg)
    msg = bot.send_message(chat_id, 'Выберите статью по номеру от 1 до 20')
    bot.register_next_step_handler(msg, detect_and_handle)

@bot.message_handler(content_types=['text'])
def detect_and_handle(message):
    global list_parsed
    global ch
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Description')
    btn2 = types.KeyboardButton('Photo')
    markup.add(btn1, btn2)
    ch = int(message.text)
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, '"some title news you can see Description of this news and Photo"', reply_markup=markup)
    bot.register_next_step_handler(msg, choice)

@bot.message_handler(commands=['Photo', 'Description'])
def choice(message):
    global ch
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Quit')
    markup.add(btn1)
    dict_ = list(filter(lambda x: x['n'] == ch, list_parsed))[0]
    img = dict_['img']
    link = dict_['link']
    if message.text == 'Photo':
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, img, reply_markup=markup)
    elif message.text == 'Description':
        descr = pars_1news(link)
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, descr, reply_markup=markup)

    bot.register_next_step_handler(msg, bye)
    
@bot.message_handler(commands=['Quit', 'start'])    
def bye(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/start')
    markup.add(btn1)
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'До свидания', reply_markup=markup)
    
    #reply_markup=types.ReplyKeyboardRemove())
   
    



        



   




    # chat_id = message.chat.id
    # msg = bot.send_message(chat_id, 'Здравствуйте, я Ваш бот')
    # bot.register_next_step_handler(msg, find_the_news)   

#         chat_id = message.chat.id
#         bot.send_message(chat_id, 'Здравствуйте, я Ваш бот')

# @bot.message_handler(content_types=['text'])
# def detect_and_handle(message):
#     if message.text == 'Начнем':
#         markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton('Оформление заказа')
#         btn2 = types.KeyboardButton('Проблемы с оплатой')
#         btn3 = types.KeyboardButton('Стоимость доставки')
#         btn4 = types.KeyboardButton('Сроки доставки')
#         btn5 = types.KeyboardButton('Оставить сообщение')
#         btn6 = types.KeyboardButton('Поиск по каталогу')
#         markup1.add(btn1, btn2, btn3, btn4, btn5, btn6)   
#         chat_id = message.chat.id
#         bot.send_message(chat_id, 'Выберите тему вопроса', reply_markup=markup1)

#     elif message.text == 'Оформление заказа':
#         keyboard = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Как сделать заказ", url="https://ekobambuk.ru/makeorder") #callback_data
#         keyboard.add(btn1)
#         chat_id = message.chat.id
#         bot.send_message(chat_id, 'Нажав на кнопку вы попадете на наш сайт и статью как сделать заказ', reply_markup=keyboard)

#     elif message.text == 'Проблемы с оплатой':
#         keyboard = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Оплата онлайн", url="https://ekobambuk.ru/payment") #callback_data
#         keyboard.add(btn1)
#         chat_id = message.chat.id
#         bot.send_message(chat_id, 'Оплатить ваш заказ вы можете здесь, нажав на кнопку', reply_markup=keyboard)

#     elif message.text == 'Стоимость доставки':
#         keyboard = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Стоимость доставки", url="https://ekobambuk.ru/delivery") #callback_data
#         keyboard.add(btn1)
#         chat_id = message.chat.id
#         bot.send_message(chat_id, 'Положить нужный товар в корзину. Перейти к оформлению и на шаге доставки вам будет доступны цена и сроки доставки как курьером так и самовывозом (ПВЗ и постаматы), а также почтой.', reply_markup=keyboard)

#     elif message.text == 'Сроки доставки':
#         keyboard = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Сроки доставки", url="https://ekobambuk.ru/delivery") #callback_data
#         keyboard.add(btn1)
#         chat_id = message.chat.id
#         bot.send_message(chat_id, 'Положить нужный товар в корзину. Перейти к оформлению и на шаге доставки вам будет доступны цена и сроки доставки как курьером так и самовывозом (ПВЗ и постаматы), а также почтой.', reply_markup=keyboard)

#     elif message.text == 'Оставить сообщение':
#         keyboard = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text="Оставить сообщение", url="https://ekobambuk.ru") #callback_data
#         keyboard.add(btn1)
#         chat_id = message.chat.id
#         bot.send_message(chat_id, 'На любой странице сайта в правом верхнем углу есть форма: "ПОЛУЧИТЬ КОНСУЛЬТАЦИЮ ПО E-MAIL". Откройте ее и оставье нам сообщение. Мы ответим Вам.', reply_markup=keyboard)   

#     elif message.text == 'Поиск по каталогу':
#         chat_id = message.chat.id
#         msg = bot.send_message(chat_id, 'Введите наименование')
#         bot.register_next_step_handler(msg, find_the_goods)

#     else:
#         chat_id = message.chat.id
#         msg = bot.send_message(chat_id, 'Вероятнее всего мы ничего не нашли. Нажимайте на кнопки, пожалуйста')

# def find_the_news(message):
#     url = f'https://kaktus.media/?lable=8&date=2023-04-24&order=time'
#     html = get_html(url)
#     soup = get_soup(html)
#     newsMain = soup.find('div', class_='Tag--articles')
#     news = newsMain.find_all('div', class_='ArticleItem--data ArticleItem--data--withImage')
#     chat_id = message.chat.id
#     bot.send_message(chat_id, 'Что то пошло не так')
#     res_loads = []
#     count = 1
#     for item in news:
#         if count == 21:
#             break
#         news_name = item.find('a', class_='ArticleItem--name').text.strip()
#         news_link = item.find('a', class_='ArticleItem--name').get('href')
#         news_img = item.find('a', class_='ArticleItem--image').find('img').get('src')
#         data = {
#             'name': news_name,
#             'link': news_link,
#             'img' : news_img
#             }
#         res_loads.append(data)
#         count +=1
#     print(res_loads)
#     return res_loads

def get_html(url: str) -> str:
    response = get(url)
    return response.text

def get_soup(html: str) -> BeautifulSoup:
    ''' Получает html разметку и структурирует ее в красивый bs'''
    soup = BeautifulSoup(html, 'lxml')
    return soup

# def get_data_catalog(goods):
#     res_search = []
#     for item in goods:
#         good_name = item.find('div', class_='product-item__link').text
#         good_price = item.find('div', class_='product-item__price -inline-group').find('div', class_='product-item-price product-item-price_with-old').text.strip()
#         good_url = item.find('div', class_='product-item__link').find('a').get('href')
#         data = {
#                 'name': good_name,
#                 'price': good_price,
#                 'url': good_url
#             }
#         res_search.append(data)
    
#     return res_search

# def no_search_result(message):
#     chat_id = message.chat.id
#     msg = bot.send_message(chat_id, 'Нет такой композиции или исполнителя. Во всяком случае мы не нашли. Уточни запрос. Начнем сначала!')
#     detect_and_handle(message)

bot.polling()


