from bs4 import BeautifulSoup
from requests import get
import csv

def get_html(url):
    response = get(url)
    return response.text

def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup

def main():
    url = 'https://www.karnatextile.ru/index.php?option=com_export&task=data&key=d90c258e1858a94a97f055e4faa589e4&type=xml'
    print(get_html(url))

main()
