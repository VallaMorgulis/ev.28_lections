from bs4 import BeautifulSoup as bs
from requests import get
import json
from datetime import datetime
from multiprocessing import Pool

def get_html(url: str) -> str:
    response = get(url)
    return response.text

def get_soup(html: str) -> bs:
    return bs(html, 'lxml')

def get_list_links(soup):
    container = soup.find('div', class_='se-news-list-page__items')
    all_news = container.find_all('div', class_='se-news-list-page__item')
    res = []
    for news in all_news:
        link = news.find('div', class_='se-material__title se-material__title--size-middle').find('a').get('href')
        res.append(link)

    return res

def get_data(link):
    html = get_html(link)
    soup = get_soup(html)
    container = soup.find('div', class_='se-material-page__body')
    title = container.find('h1', class_='se-material-page__title').text
    try:
        image = container.find('div', class_='se-photogallery-swipe__image').find('a').find('img').get('src')
    except:
        image = 'No image'
    text = container.find('div', class_='se-material-page__content').find_all('p')
    data = {'title': title, 'image': image, 'text': text}
    return data


url = get_html('https://www.sport-express.ru/news/')
soup = get_soup(url)


def make_all(link):
        data = get_data(link)
        news = News.objects.create(title=data['title'], image=data['image'], text=data['text'])


def main():
    links = get_list_links(soup)
    with Pool(40) as pool:
        pool.map(make_all, links)


if __name__ == '__main__':
    start = datetime.now()
    main()
    finish = datetime.now()
    print(f'Parsing takes: {finish - start} time')