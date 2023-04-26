# task 1

# import requests

# url = requests.get('https://stackoverflow.com/questions')
# source = url.status_code
# print(source)

# task 2

# from bs4 import BeautifulSoup
# import requests
# import lxml

# source = requests.get('http://www.example.com/').text 
# my_page = BeautifulSoup(source, 'lxml')
# print('h1:', my_page.h1.text) 
# print('p:', my_page.p.text) 
# print('a:', my_page.a.get('href'))

# task 3

# from bs4 import BeautifulSoup
# import requests
# import lxml

# source = requests.get('https://wikipedia.org/').text 
# my_page = BeautifulSoup(source, 'lxml')
# a = my_page.find('div', class_ = 'central-featured-lang lang4').find('a')
# lang = a.find('strong').text
# num = a.find('small').find('bdi').text
# artik = a.find('small').find('span').text

# print(lang)
# print(num, artik)

# task 4

# def getTitle(url):
#     from bs4 import BeautifulSoup
#     import requests
#     import lxml

#     source = requests.get(url).text 
#     my_page = BeautifulSoup(source, 'lxml')
#     if my_page.find('h1'):
#         return my_page.find('h1')
#     else: 
#         return 'Title could not be found'

# print(getTitle('http://www.example.com/'))

# task 5

# from bs4 import BeautifulSoup
# from requests import get
# import lxml
# import re


# source = get('https://enter.kg/').text
# my_page = BeautifulSoup(source, 'lxml')
# category_li = my_page.find('ul', class_="VMmenu").text.strip()
# category_list = re.sub("  +", ";!", category_li).split(';!')

# def find_category(categories: list, keyword: str) -> list:
#     res = [x for x in categories if x.startswith(keyword.capitalize())]
#     return res

# print(find_category(category_list, 'ноутбуки'))



# from bs4 import BeautifulSoup
# from requests import get



# html = get('https://enter.kg/').text
# soup = BeautifulSoup(html, 'html.parser')
# container = soup.find('ul', class_="VMmenu")
# category_list = [x.text for x in container.find_all('a')]

# def find_category(categories: list, keyword: str) -> list:
#     return [x for x in categories if keyword.lower() in x.lower()]

# print(find_category(category_list, ''))


# task 6

# from bs4 import BeautifulSoup
# import requests

# response = requests.get('https://www.imdb.com/chart/top').text
# soup = BeautifulSoup(response, 'lxml')
# container = soup.find('div', class_='lister').find('table', class_='chart full-width').find('tbody', class_='lister-list')
# films = container.find_all('tr')
# title_list = []
# for item in films:
#     film_link = 'https://www.imdb.com' + item.find('td', class_='titleColumn').find('a').get('href')
#     film_name = item.find('td', class_='titleColumn').find('a').text
#     data = {'name': film_name, 'link': film_link}
#     title_list.append(data)

# def get_link(title_list, name):
#     for i in title_list:
#         if name.lower() in i['name'].lower():
#             return i['link']
    

# print(get_link(title_list, 'shawshank'))
