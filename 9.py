import time
import requests
import json
import lxml
from bs4 import BeautifulSoup
import csv
import asyncio
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}

def test_request(url, headers, retry=5):

    try:
        response = requests.get(url=url, headers=headers)
        print(f' {url} [+] {response.status_code}')

    except Exception as ex:
        time.sleep(3)
        if retry:
            print(f'[INFO] retry={retry} = {url}')
            return test_request(url, retry=(retry-1))
        else:
            raise
    else:
        return response


def main():
    with open('link_lab.txt', 'r') as file:
        books_urls = file.read().splitlines()
        # print(books_urls)

    for book_url in books_urls:
        # test_request(url=book_url, headers=headers)
        try:
            r = test_request(url=book_url, headers=headers)
            soup = BeautifulSoup(r.text, 'lxml')
            print(f'{soup.title.text} \n')
        except Exception as ex:
            continue



if __name__ == '__main__':
    main()
