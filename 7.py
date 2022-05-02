import requests
import json
import lxml
from bs4 import BeautifulSoup
import csv

def get_data():

    with open('csv_file.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Название книги',
                "Автор",
                "Издательство",
                "Цена со скидкой",
                "Старая цена",
                "Скидка",
                "Наличие на складе",
                "Ссылка"
            )
        )

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

    url = 'https://www.labirint.ru/genres/2308/?display=table'
    responce = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(responce.text, 'lxml')
    page_count = int(soup.find('div', 'pagination-number').find_all('a')[-1].text)
    books_data = []
    for page in range(1, page_count+1):
        url = f'https://www.labirint.ru/genres/2308/?display=table&page={page}'
        responce = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(responce.text, 'lxml')
        book_items = soup.find('tbody', 'products-table__body').find_all('tr')

        for bi in book_items:
            book_data = bi.find_all('td')
            # print(book_data)
            try:
                book_title = book_data[0].find('a').text.strip()
                book_link = f"https://www.labirint.ru{book_data[0].find('a').get('href').strip()}"
            except:
                book_title = 'Нет названия книги'

            try:
                book_autor = book_data[1].text.strip()
            except:
                book_autor = 'Автор не указан'

            try:
                # book_pubhouse = book_data[2].text.strip()
                book_pubhouse = book_data[2].find_all('a')
                book_pubhouse = ':'.join(bp.text for bp in book_pubhouse)
            except:
                book_autor = 'Издательство не указан'

            try:
                book_amount = int(book_data[3].find('span', 'price-val').find('span').text.replace(' ',''))

            except:
                book_amount = 'Цена не указана'

            try:
                book_old_amount = int(book_data[3].find('span', 'price-old').find('span').text.strip().replace(' ',''))
            except:
                book_old_amount ='Скидка отсутствует'
                discount = 0

            try:
                discount = round(100 - (book_amount*100/book_old_amount))
            except:
                continue

            try:
                book_status = book_data[-1].text.strip()
            except:
                book_status = 'Статус отсутствует'

            books_data.append(
                {
                    'name': book_title,
                    'autor': book_autor,
                    'publisher': book_pubhouse,
                    'amount': book_amount,
                    'olda_mount': book_old_amount,
                    'discount': discount,
                    'status':book_status,
                    'link': book_link,

                }
            )
            with open('csv_file.csv', 'a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        book_title,
                        book_autor,
                        book_pubhouse,
                        book_amount,
                        book_old_amount,
                        discount,
                        book_status,
                        book_link,
                )
                )

        with open('json_file.json', 'w') as file:
            json.dump(books_data, file, indent=4, ensure_ascii=False)

        print(f"Обработана {page} / {page_count}")




def main():
    get_data()













if __name__ == '__main__':
    main()
