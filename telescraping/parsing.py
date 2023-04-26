from bs4 import BeautifulSoup
from requests import get

# url = f'https://kaktus.media/?lable=8&date=2023-04-24&order=time'

def pars_all_news(url):
    html = get_html(url)
    soup = get_soup(html)
    newsMain = soup.find('div', class_='Tag--articles')
    news = newsMain.find_all('div', class_='ArticleItem--data ArticleItem--data--withImage')
    res_loads = []
    count = 1
    for item in news:
        if count == 21:
            break
        news_name = item.find('a', class_='ArticleItem--name').text.strip()
        news_link = item.find('a', class_='ArticleItem--name').get('href')
        news_img = item.find('a', class_='ArticleItem--image').find('img').get('src').replace('small', 'big')
        data = {
            'n': count,
            'name': news_name,
            'link': news_link,
            'img' : news_img
            }
        res_loads.append(data)
        count +=1
    return res_loads

    

def get_html(url: str) -> str:
    response = get(url)
    return response.text

def get_soup(html: str) -> BeautifulSoup:
    ''' Получает html разметку и структурирует ее в красивый bs'''
    soup = BeautifulSoup(html, 'lxml')
    return soup


def pars_1news(url):
    html = get_html(url)
    soup = get_soup(html)
    newsMain= soup.find('div', class_='Article--text').find('div', class_='BbCode').text.strip()
    if len(newsMain) > 1000:
        newsMain = newsMain[0:1000]
    return newsMain

