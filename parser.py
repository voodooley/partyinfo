import requests
from bs4 import BeautifulSoup
import csv
from random import uniform
from time import sleep


# url = 'https://partyinfo.ru/company'
def get_info(url):
    s = requests.Session()
    s.get(url, verify=False)
    data = {
        'name': 'voodoobet@yandex.ru',
        'pass': '5/Nigfbu',
        'antwort': '0691e4720280a8990ad058987108405e'
    }

    r = s.post('https://partyinfo.ru/auth', data=data)

    some = requests.get(url, verify=False, cookies=r.cookies)

    return some.text


def get_html(url):
    r = requests.get(url, verify=False)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pag').find_all('a')[-2].text
    return int(pages)


def write_csv(data):
    with open('partyinfo.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['company_name'],
                         data['company_phone'],
                         data['company_site'],
                         data['company_url'],
                         data['company_city']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    companies = soup.find('div', class_='place_items').find_all('div', class_='place_item')
    for company in companies:
        try:
            company_name = company.find('a', class_='name').text
        except:
            company_name = ''
        try:
            company_url = 'https://partyinfo.ru/' + company.find('a', class_='name').get('href')
        except:
            company_url = ''
        try:
            company_city = company.find('div', class_='city').text.strip()
        except:
            company_city = ''

        company_id = company.find('a', class_='info').get('data-id')
        try:
            info_html = get_info(
                f'https://partyinfo.ru/tabs?info=contacts&ess=event&essid={company_id}&cat={company_id}')
        except:
            info_html = ''

        soup2 = BeautifulSoup(info_html, 'lxml')

        try:
            company_phone = soup2.find('div', class_='contacts-pop-np__info-phone').find('a').text
            # company_phone = soup2.find('div', class_='contacts-pop-np__info-phone').find('a').get('href').split('+')[-1]
        except:
            try:
                company_phone = soup2.find('div', class_='cp_phone').text
            except:
                company_phone = 'не найден'
        try:
            company_site = soup2.find('div', class_='contacts-pop-np__info-add').find('a').get('href')
        except:
            company_site = 'Не найден'

        comany_data = {
            'company_name': company_name,
            'company_url': company_url,
            'company_city': company_city,
            'company_phone': company_phone,
            'company_site': company_site
        }

        write_csv(comany_data)


def main():
    base_url = 'https://partyinfo.ru/company'
    part_url = '_'
    total_pages = get_total_pages(get_html(base_url))

    for i in range(1, total_pages + 1):
        sleep(uniform(2, 5))
        print(f'Parse page {i}')
        url_gen = base_url + part_url + str(i)
        try:
            html = get_html(url_gen)
        except:
            continue
        try:
            get_page_data(html)
        except:
            continue


if __name__ == '__main__':
    main()
