import requests
from bs4 import BeautifulSoup

# url = 'https://partyinfo.ru/company'


def get_html(url):
    r = requests.get(url, verify=False)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pag').find_all('a')[-2].text
    return int(pages)


print(get_total_pages(get_html('https://partyinfo.ru/company')))