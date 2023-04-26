import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Pool

def get_html(url: str) -> str:
    '''Эта функция получает HTML разметку по определенному сайту по URL'''
    response = requests.get(url)
    return response.text

def get_soup(html: str) -> BeautifulSoup:
    ''' Получает html разметку и структурирует ее в красивый bs'''
    soup = BeautifulSoup(html, 'lxml')
    return soup


def get_all_links():
    res = []
    i = 1
    while True:
        url = f'https://www.mashina.kg/search/all/?page={i}'
        res.append(url)
        print(url)
        if i == 1749:
            break
        i += 1
    return res

def get_data(link: BeautifulSoup) -> list:
    html = get_html(link)
    soup = get_soup(html)
    '''Получает нужные данные с сайта машина кджи'''
    container = soup.find('div', class_='table-view-list')
    cars = container.find_all('div', class_='list-item')
    result = []
    for car in cars:
        name = car.find('h2', class_='name').text.strip()
        try:
            img = car.find('img', class_='lazy-image').get('data-src')
        except:
            img = 'No image'
        price_div = car.find('div', class_='block price')
        price = price_div.find('p').find('strong').text
        ls = ['year-miles', 'body-type', 'volume']
        desc = ', '.join(car.find('p', class_=x).text.strip() for x in ls)
        data = {
            'name': name,
            'desc': desc,
            'price': price,
            'img': img
        }
        result.append(data)
    return result

def prepare_csv() -> None:
    '''Функция, которя подготавливает csv файл!'''
    with open('cars.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow([
            'Name',
            'Description',
            'Price',
            'Image URL'
        ])

def write_to_csv(data: list) -> None:
    '''Записывает все данные в csv файл'''
    with open('cars.csv', 'a') as file:
        fieldnames = ['Name', 'Description', 'Price', 'Image URL']
        writer = csv.DictWriter(file, fieldnames) 
        for car in data:
            writer.writerow({
            'Name': car['name'],
            'Description': car['desc'],
            'Price': car['price'],
            'Image URL': car['img']
            }) 

def make_all(link):#8
        data = get_data(link)
        write_to_csv(data)        


def main():
    prepare_csv()
    links = get_all_links()
    with Pool(40) as pool:
        pool.map(make_all, links)


if __name__ == '__main__':
    start = datetime.now()
    main()
    finish = datetime.now()
    print(f'Parsing takes: {finish - start} time')
