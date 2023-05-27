# В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.

# with open('text.txt') as file:
#     list_ = file.readlines()

# strok = len(list_)
# simbols_in_str = []
# words_in_str = []

# for i in list_:
#     s = len(i.strip().replace(' ',''))
#     simbols_in_str.append(s)
#     w = len(i.split())
#     words_in_str.append(w)

# print(f'Количество строк {strok},\nKоличество символов в строках {simbols_in_str}\nKоличество слов в строках {words_in_str}')


# Спарсить vesti.kg только названия новостей(title) и записать результат в csv файл


from bs4 import BeautifulSoup
from requests import get
import csv

def get_html(url):
    response = get(url)
    return response.text

def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_data(link):
    html = get_html(link)
    soup = get_soup(html)
    div_title = soup.find_all('div', class_='itemBody')
    data= []
    for item in div_title:
        title_ = item.find('a').text.strip()
        href_ = 'https://vesti.kg/' + item.find('a').get('href')
        res = {
            'title': title_,
            'link': href_
        }
        data.append(res)

    return data

def prepare_csv():
    with open('titles.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow([
                '№',
                'Titles',
                'Link'
            ])
    
def write_to_csv(data: list) -> None:
    with open('titles.csv', 'a') as file:
        fieldnames = ['№', 'Titles', 'Link']
        writer = csv.DictWriter(file, fieldnames) 
        count = 1
        for item in data:
            writer.writerow({
            '№' : count,
            'Titles' : item['title'],
            'Link' : item['link']
            })
            print(f'Parsing {count} title(s)!')
            count += 1

def main():
    prepare_csv()
    url = 'https://vesti.kg/'
    data = get_data(url)
    write_to_csv(data)

main()



