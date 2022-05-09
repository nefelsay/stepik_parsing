import requests
from bs4 import BeautifulSoup
import lxml


class Parser:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'accept': '* / *'}
        self.gen_link = []
        self.completed_proxy_list = []
        self.pagen_count = 1

    def gen_links_lst(self):  # генерирует список ссылок по заданому оффсету
        for offset in range(0, 9216, 64):  # 9216
            link = f'https://hidemy.name/ru/proxy-list/?start={offset}'
            self.gen_link.append(link)

    def get_html(self):  # получает хтмл с каждой страницы
        page = 0
        try:
            for link in self.gen_link:
                page += 1
                response = requests.get(url=link, headers=self.headers)
                soup = BeautifulSoup(response.text, 'lxml')
                ip = soup.find('tbody').find_all('tr')
                port = soup.find('tbody').find_all('tr')
                for ip, port in zip(ip, port):
                    self.completed_proxy_list.append(
                        f"{ip.find_all('td')[0].text}:{port.find_all('td')[1].text} \n")
                print(f'page:{page}, find proxy:{len(self.completed_proxy_list)}')
        except Exception as _ex:
            print(_ex)

    def save_proxy_in_txt(self):    # записывает результат в файл
        with open('proxy_list.txt', 'w') as file:
            for proxy in self.completed_proxy_list:
                file.write(proxy)

    def main(self):
        self.gen_links_lst()
        parse.get_html()
        self.save_proxy_in_txt()


if __name__ == '__main__':
    parse = Parser()
    parse.main()
