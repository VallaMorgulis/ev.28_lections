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

from bs4 import BeautifulSoup
import requests
import lxml

source = requests.get('https://enter.kg/').text 
my_page = BeautifulSoup(source, 'lxml')
category_list = my_page.find_all('ul', class_="VMmenu")


def getTitle(url):

