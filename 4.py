import time

import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver

def get_data(url):
    headers = {

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'text/html; charset=utf-8',

    }

    r = requests.get(url=url, headers=headers)

    # with open('index.html', 'w') as file:
    #     file.write(r.text)


    r= requests.get('https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru', headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    hotels_card = soup.find_all('div', class_='hotel_card_dv')

    for hotel_url in hotels_card:
        hotel_url = hotel_url.find('a').get('href')


def get_data_with_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36')

    # try:
    #     driver = webdriver.Firefox(
    #         executable_path='G:\Мой диск\Roadmap Parsing\Code\Python today 3\geckodriver.exe',
    #         options=options
    #     )
    #
    #     driver.get(url=url)
    #     time.sleep(5)
    #
    #     with open('index_selenium.html', 'w', encoding='utf-8') as file:
    #         file.write(driver.page_source)
    #
    # except Exception as ex:
    #     print(ex)
    #
    # finally:
    #     driver.close()
    #     driver.quit()

    with open('index_selenium.html', encoding='utf-8' ) as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    hotels_card = soup.find_all('div', class_='hotel_card_dv')

    for hotel_url in hotels_card:
        hotel_url = 'https://tury.ru' + hotel_url.find('a').get('href')
        print(hotel_url)


def main():
    # get_data('https://tury.ru/hotel/most_luxe.php')
    get_data_with_selenium('https://tury.ru/hotel/most_luxe.php')






if __name__ == '__main__':
    main()
