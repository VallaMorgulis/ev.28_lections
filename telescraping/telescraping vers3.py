import telebot
from telebot import types
from bs4 import BeautifulSoup
from requests import get
from my_token import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привет")
    markup.add(btn1)
    chat_id = message.chat.id
    bot.send_message(chat_id, "👋 Привет! Я твой бот! Помогаю найти музыку", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Привет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('Найти')
        btn2 = types.KeyboardButton('Хиты')
        btn3 = types.KeyboardButton('Новинки')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Нажмите на кнопочку Найти', reply_markup=markup) 


    elif message.text == 'Найти':
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, 'Введи название исполнителя/композицию или нажмите Хиты или Новинки', parse_mode='Markdown')
        bot.register_next_step_handler(msg, find_the_song)

    elif message.text == 'Хиты':
        bot.register_next_step_handler(message, find_the_song)

    elif message.text == 'Новинки':
        bot.register_next_step_handler(message, find_the_song)


def find_the_song(message):
    url = f'https://zaycev.net/search.html?query_search={message.text}'
    html = get_html(url)
    soup = get_soup(html)
    try:
        singerMain = soup.find('div', class_='sc-1ivpr86-3 dcizwQ').find('ul', class_='sc-18st3ox-1 eKEXNL')
    except:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Ничего не нашли. Уточните исполнителя или композицию.')
        get_text_messages(message)
        return
    else:
        all_songs = get_data_songs(singerMain)
        chat_id = message.chat.id
        msg_list = []
        for i in all_songs:
            art = i['artist']
            name = i['name']
            link = i['url']
            msg = f'Название: "{name}"\nАртист: "{art}"\nCсылка {link}\n\n'
            msg_list.append(msg)
        all_msg = ''.join(msg_list)
        bot.send_message(chat_id, all_msg)
        bot.send_message(chat_id, 'Кнопочки внизу, если еще что то нужно')
        get_text_messages(message)

def get_html(url: str) -> str:
    '''Эта функция получает HTML разметку по определенному сайту по URL'''
    response = get(url)
    return response.text

def get_soup(html: str) -> BeautifulSoup:
    ''' Получает html разметку и структурирует ее в красивый bs'''
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_data_songs(singerMain):
    res_search = []
    singer = singerMain.find_all('li')
    for item in singer:
        song_art = item.find('div', class_='sc-1cisiq-6 gmCfCb').text
        song_name = item.find('div', class_='fa9swr-6 eOPoOa').find('a', class_='sc-1vuj2t8-0 pbfhi').text
        song_url = 'https://zaycev.net'+item.find('div', class_='fa9swr-6 eOPoOa').find('a', class_='sc-1vuj2t8-0 pbfhi').get('href')
        data = {
                'artist': song_art,
                'name': song_name,
                'url': song_url
            }
        res_search.append(data)
    
    return res_search

def no_search_result(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Нет такой композиции или исполнителя. Во всяком случае мы не нашли. Уточни запрос. Начнем сначала!')
    get_text_messages(message)


bot.polling(none_stop=True, interval=0)
