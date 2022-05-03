import json

import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://knigorai.com/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'lxml')
pagen = int([x.text for x in soup.find_all('li', class_='page-item')][-2])


class Parser:
    def __init__(self):
        self.page_url_list = []
        self.cards_url = []
        self.result_json = []

    def gen_url(self):
        for i in range(1, pagen + 1):
            self.page_url_list.append(f'https://knigorai.com/?p={i}')

    def gen_cards_url(self):
        for url in self.page_url_list:
            response = requests.get(url=url).text
            soup = BeautifulSoup(response, 'lxml')
            url_card = [f"{x['href']}" for x in soup.find_all('a', class_='book-title')]
            self.cards_url.append(url_card)

            for x in url_card:
                response_card = requests.get(url=x).text
                soups = BeautifulSoup(response_card, 'lxml')
                try:
                    if not soups.find('h2', {'itemprop': 'author'}).find('a'):
                        continue

                except Exception as _ex1:
                    # Создание тега для автора
                    new_tag_author_h2 = soups.new_tag('h2', itemprop='author')
                    new_tag_author_a = soups.new_tag('a')
                    new_tag_author_a.string = 'Not author'

                    soups.html.body.h1.insert_after(new_tag_author_h2)
                    soups.html.body.h2.insert(2, new_tag_author_a)

                try:
                    self.result_json.append({
                        'name_book': soups.find('h1', {'itemprop': 'name'}).text.replace('Not autor', ''),
                        'author': soups.find('h2', {'itemprop': 'author'}).find('a').text,
                        'duration': soups.find('i', class_='fa-clock-o').next_sibling.replace('\r\n        ',
                                                                                              '').strip(),
                        'link': x,
                        'json_link': f"{x}/playlist.txt",
                        # 'voice_reader': soups.find('i', class_='fa fa-microphone').find_next_sibling('a').text,
                        'description': soups.find('div', class_='description').find('p').text,
                        'genre': [f'{x.text}' for x in soups.find('div', class_='col-lg-12').find_all('a')],

                    })

                    with open('json.json', 'w', encoding='utf-8') as file:
                        json.dump(self.result_json, file, ensure_ascii=False, indent=4)
                        print(f"{soups.find('h1', {'itemprop': 'name'}).text}")

                except Exception as _ex2:
                    print(_ex2, x)


if __name__ == '__main__':
    parser = Parser()
    parser.gen_url()
    parser.gen_cards_url()
