import time
import requests
from bs4 import BeautifulSoup

import lxml
import os
import json
from datetime import datetime
import csv


def get_all_pages():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    }
    r = requests.get(url='https://shop.casio.ru/catalog/filter/gender-is-male/apply/', headers=headers)
    if not os.path.exists('data'):
        os.mkdir('data')
    with open('data/page_1.html', 'w', encoding='utf-8') as file:
        file.write(r.text)
    with open('data/page_1.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    pages_count = int(soup.find('div', class_='bx-pagination-container').find_all('a')[-2].text)
    for i in range(1, pages_count + 1):
        url = f'https://shop.casio.ru/catalog/filter/gender-is-male/apply/?PAGEN_1={i}'
        r = requests.get(url=url, headers=headers)
        with open(f'data/page_{i}.html', 'w', encoding='utf-8') as file:
            file.write(r.text)
        time.sleep(2)
    return pages_count + 1


def collect_data(pages_count):
    data = []
    current_date = datetime.now().strftime('%d_%m_%Y')
    with open(f'data{current_date}.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Артикул',
                'Ссылка',
                'Цена',
            )
        )

    for page in range(1, pages_count):
        with open(f'data/page_{page}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        item_cars = soup.find_all('a', class_='product-item__link')
        for item in item_cars:
            product_article = item.find('p', class_='product-item__articul').text.strip()
            product_price = item.find('p', class_='product-item__price').text.lstrip('руб.')
            product_url = f"https://shop.casio.ru{item.get('href')}"
            data.append({
                'product_article': product_article,
                'product_url': product_url,
                'product_price': product_price,
                }
            )
            with open(f'data{current_date}.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        product_article,
                        product_url,
                        product_price,
                    )
                )

        print(f'[INFO] Обрабатывается страница {page}/8')

    with open(f'data{current_date}.json', 'a') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    pages_count = get_all_pages()
    collect_data(pages_count=pages_count)


if __name__ == '__main__':
    main()
