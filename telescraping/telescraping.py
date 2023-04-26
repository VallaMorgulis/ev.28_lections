import telebot
from telebot import types
from bs4 import BeautifulSoup
from requests import get
from my_token import token

bot = telebot.TeleBot(token)


markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
btn1 = types.KeyboardButton('/start')
markup.add(btn1)

@bot.message_handler(commands=['start', 'text'])
def start_message(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Давай послушаем музыку!\nВведи название исполнителя или композицию', reply_markup=markup)
    bot.register_next_step_handler(msg, find_the_song)
    

def find_the_song(message):
    url = f'https://sefon.pro/search/?q={message.text}'
    html = get_html(url)
    soup = get_soup(html)
    try:
        singerMain = soup.find('div', class_='b_list_mp3s _')
    except:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Ничего не нашли. Уточните исполнителя или композицию.')
        start_message(message)
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

def get_html(url: str) -> str:
    '''Эта функция получает HTML разметку по определенному сайту по URL'''
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = get(url, headers=headers)
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

def no_search_result(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Нет такой композиции или исполнителя. Во всяком случае мы не нашли. Уточни запрос. Начнем сначала!')
    start_message()



bot.polling()




