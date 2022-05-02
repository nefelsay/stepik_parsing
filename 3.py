import json

import requests
# from bs4 import BeautifulSoupф
# import lxml
import img2pdf



def get_data():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    link_list = []
    for i in range(1, 48):
        url = f'https://recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg'
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f'img/{i}.jpg', 'wb') as file:
            file.write(response)
            link_list.append(f'img/{i}.jpg')
            print(f'Downloads {i}.img')

    with open('img/result.pdf', 'wb') as file:
        file.write(img2pdf.convert(link_list))
    print(link_list)
    print('PDF created successful')


def main():
    get_data()


if __name__ == '__main__':
    main()
