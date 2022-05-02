import time
import requests
from bs4 import BeautifulSoup
import re
import lxml
import os
import csv
import sys
import json


class Parser:
    def __init__(self):
        # self.url = ''
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
        self.list_all_page = []
        self.list_all_card = []
        self.card_dict = dict()

    def save_html_all_page(self):
        for item in range(1, 9):
            response = requests.get(url=f'https://reprobank.ru/bank-donorov/katalog-donorov-spermi/?d_page={item}',
                                    headers=self.headers)
            soup = BeautifulSoup(response.text, 'lxml')
            all_card_donor_in_page = str(soup.find('div', class_='donors-catalog'))
            with open(f'data/index_{item}.html', 'w', encoding='utf-8') as file:
                file.write(all_card_donor_in_page)

    def parse_data(self):
        re_pattern = r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)'
        for item in range(1, 9):
            with open(f'data/index_{item}.html', 'r', encoding='utf-8') as file:
                src = file.read()
            soup = BeautifulSoup(src, 'lxml')
            for link in soup.find_all('a', attrs={'href': re.compile(re_pattern)}):
                self.list_all_card.append(link.get('href'))

    def save_html_info_in_card(self):
        for link, i in zip(self.list_all_card, range(1, len(self.list_all_card) + 1)):
            response = requests.get(url=link, headers=self.headers)
            soup = BeautifulSoup(response.text, 'lxml')
            get_html = soup.find('div', class_='params')
            with open(f'data/card/index_card_{i}.html', 'w', encoding='utf-8') as file:
                file.write(str(get_html))

    def save_csv(self):
        with open('result.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Ссылка', 'Рост', 'Вес', 'Цвет глаз', 'Цвет волос', 'Тип волос', 'Комплекция',
                             'Тип внешности', 'Национальность',
                             'Тип донора', 'Знак Зодиака', 'Группа крови', 'Вероисповедание', 'Образование',
                             'Уровень образования', 'Специализация', 'Профессия/Отрасль',
                             'Донор похож на', 'Подходит для', 'За рамками 2'])


        for i in range(1, len(self.list_all_card) + 1):
            with open(f'data/card/index_card_{i}.html', 'r', encoding='utf-8') as file:
                src = file.read()
                soup = BeautifulSoup(src, 'lxml')
                all_param = soup.find_all('div', class_='param')
                all_value = soup.find_all('div', class_='value')

                self.card_dict = {
                    'link': f'{self.list_all_card[i - 1]} ',
                }

                for item in range(len(all_param)):
                    self.card_dict.update({
                        all_param[item].text: all_value[item].text.replace('\t', '').replace('\n', '')
                    })


            with open('result.csv', 'a', encoding='utf-8', newline='') as files:
                writer = csv.writer(files, delimiter=';')
                writer.writerow([x for x in self.card_dict.values()])


if __name__ == '__main__':
    parser = Parser()
    # parser.save_html_all_page()
    parser.parse_data()
    # parser.save_html_info_in_card()
    parser.save_csv()
