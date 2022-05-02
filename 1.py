import requests
from bs4 import BeautifulSoup

# URL = 'https://auto.ria.com/newauto/marka-peugeot/'
URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.69 Safari/537.36',

    'accept': '*/*'
}  # для отправки заголовков, чтобы сервер не посчитал нас ботами и не забанил
HOST = 'https://auto.ria.com'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('section', class_='proposition')
    # print(items)
    cars = []
    for item in items:
        usd_price = item.find('span', class_='green')
        uah_price = item.find('span', class_='size16')
        city = item.find('span', class_='region')
        if usd_price or uah_price or city:
            usd_price = usd_price.get_text(strip=True).replace(' ', '')
            uah_price = uah_price.get_text(strip=True).replace(' ', '')
            city = city.get_text(strip=True).replace(' ', '')
        else:
            usd_price = 'None price USD'
            uah_price = 'None Price UAH'

        cars.append({
            'title': item.find('h3', class_='proposition_name').get_text(strip=True),
            'link': HOST + item.find('a').get('href'),
            'usd_price': usd_price,
            'uah_price': uah_price,
            'city': city,

        })
    # return cars

    print(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Ебучая ошибка')


parse()
