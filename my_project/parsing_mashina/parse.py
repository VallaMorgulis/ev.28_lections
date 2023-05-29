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

def get_last_page(link: str):
    html = get_html(link)
    soup = get_soup(html)
    container = soup.find('div', class_='search-results-table').find('ul', class_='pagination')
    last_page = container.find_all('li')[-1]
    total_pages = int(last_page.find('a').get('data-page'))
    return total_pages

def get_all_links():
    res = []
    i = 1
    last_page = get_last_page('https://www.mashina.kg/search/all/?page=1')
    while True:
        url = f'https://www.mashina.kg/search/all/?page={i}'
        res.append(url)
        print(url)
        if i == last_page:
            break
        i += 1
    print('\nИдет процесс парсинга! Это занимает от 3 до 5 минут! Наберись терпения!')
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
            img = 'No data'
        price_div = car.find('div', class_='block price')
        try:
            price = int(price_div.find('p').text.strip()[10:-4].strip().replace(' ',''))
        except:
            price = 'No data'
        try:
            color_str = str(car.find('p', class_='year-miles'))
            color = color_str[color_str.find('title=')::].replace('title="', '').replace('"></i>\n</p>', '')
        except:
            color = "No data"
        ls = ['year-miles', 'body-type', 'volume']
        desc = (', '.join(car.find('p', class_=x).text.strip() for x in ls)).split(',')
        if len(desc) == 7:
            year = desc[0].strip()[0:5].replace(' ', '')
            engine_capacity = float(desc[1].strip().replace(' л.', ''))
            gearbox_type = desc[2].strip()
            body_type = desc[3].strip()
            engine_type = desc[4].strip()
            wheel_position = desc[5].strip()
            try:
                mileage = int(desc[6].strip()[0:-3].replace(' ',''))
            except:
                mileage = 'No data'
            data = {
                'name': name,
                'year': year,
                'engine_capacity': engine_capacity,
                'gearbox_type': gearbox_type,
                'color': color,
                'body_type': body_type,
                'engine_type': engine_type,
                'wheel_position': wheel_position,
                'mileage': mileage,
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
            'Year',
            'Engine_capacity',
            'Gearbox_type',
            'Color',
            'Body_type',
            'Engine_type',
            'Wheel_position',
            'Mileage',            
            'Price',
            'Image URL'
        ])

def write_to_csv(data: list) -> None:
    '''Записывает все данные в csv файл'''
    with open('cars.csv', 'a') as file:
        fieldnames = ['Name', 'Year', 'Engine_capacity', 'Gearbox_type', 'Color', 'Body_type', 'Engine_type', 'Wheel_position', 'Mileage', 'Price', 'Image URL']
        writer = csv.DictWriter(file, fieldnames) 
        for car in data:
            writer.writerow({
            'Name': car['name'],
            'Year': car['year'],
            'Engine_capacity': car['engine_capacity'],
            'Gearbox_type': car['gearbox_type'],
            'Color': car['color'],
            'Body_type': car['body_type'],
            'Engine_type': car['engine_type'],
            'Wheel_position': car['wheel_position'],
            'Mileage': car['mileage'],            
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
