import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup

category_lst = []
pagen_lst = []
domain = 'https://parsinger.ru/html/'


def get_soup(url):
    resp = requests.get(url=url)
    return BeautifulSoup(resp.text, 'lxml')


def get_urls_categories(soup):
    '''
    Эта функция извлекает ссылки со всех категорий на сайте и формирует глобальный список category_list
    Для дальнейшего извлечения с каждой категории длины пагинации.

    input: soup

    output:
    category_lst = [https://parsinger.ru/html/index1_page_1.html
                    https://parsinger.ru/html/index2_page_1.html
                    https://parsinger.ru/html/index3_page_1.html
                    https://parsinger.ru/html/index4_page_1.html
                    https://parsinger.ru/html/index5_page_1.html
                    ]

    '''
    all_link = soup.find('div', class_='nav_menu').find_all('a')

    for cat in all_link:
        category_lst.append(domain + cat['href'])


def get_urls_pages(category_lst):
    '''

    В эту функцию прилетает список категорий category_lst
    input:
    ['https://parsinger.ru/html/index1_page_1.html', 'https://parsinger.ru/html/index2_page_1.html',
     'https://parsinger.ru/html/index3_page_1.html', 'https://parsinger.ru/html/index4_page_1.html',
     'https://parsinger.ru/html/index5_page_1.html']

    output:
    так же эта функция выдёргивает с каждой категории ссылку из пагинации формируя глобальный список pagen_list

    pagen_lst = ['https://parsinger.ru/html/index1_page_1.html', 'https://parsinger.ru/html/index1_page_2.html',
                'https://parsinger.ru/html/index1_page_3.html', 'https://parsinger.ru/html/index1_page_4.html',
                'https://parsinger.ru/html/index2_page_1.html', 'https://parsinger.ru/html/index2_page_2.html',
                'https://parsinger.ru/html/index2_page_3.html', 'https://parsinger.ru/html/index2_page_4.html',
                'https://parsinger.ru/html/index3_page_1.html', 'https://parsinger.ru/html/index3_page_2.html',
                'https://parsinger.ru/html/index3_page_3.html', 'https://parsinger.ru/html/index3_page_4.html',
                'https://parsinger.ru/html/index4_page_1.html', 'https://parsinger.ru/html/index4_page_2.html',
                'https://parsinger.ru/html/index4_page_3.html', 'https://parsinger.ru/html/index4_page_4.html',
                'https://parsinger.ru/html/index5_page_1.html', 'https://parsinger.ru/html/index5_page_2.html',
                'https://parsinger.ru/html/index5_page_3.html', 'https://parsinger.ru/html/index5_page_4.html']
    '''
    for cat in category_lst:
        resp = requests.get(url=cat)
        soup = BeautifulSoup(resp.text, 'lxml')
        for pagen in soup.find('div', class_='pagen').find_all('a'):
            pagen_lst.append(domain + pagen['href'])


async def get_data(session, link):
    '''
    input: session, link

    Асинхронная функция которая принимает session и link переданные из асинхронной функции main()
    В этой функции происходит извлечение данных с каждой карточки на сайте, всего 160 шт
    Session является объектом модуля aiohttp
    Данные извлекаются при помощи BeautifulSoup
    Так же в этом функции происходит переиспользование сессии для более глубокого прохода по сайту,
    это помогает извлекать информацию непосредственно из каждой карточки.

    Output: извлекаемые данные с помощью BeautifulSoup
    '''
    async with session.get(url=link) as response:
        resp = await response.text()
        soup = BeautifulSoup(resp, 'lxml')
        item_card = [x['href'] for x in soup.find_all('a', class_='name_item')]
        for x in item_card:
            url2 = domain + x
            async with session.get(url=url2) as response2:
                resp2 = await response2.text()
                soup2 = BeautifulSoup(resp2, 'lxml')
                article = soup2.find('p', class_='article').text
                name = soup2.find('p', id='p_header').text
                price = soup2.find('span', id='price').text
                print(url2, price, article, name)


async def main():
    '''
    input : None

    Контрольная точка для запуска event loop, в этой асинхронной функции создаётся сессия aiohttp,
    так же формируются задачи при помощи asyncio.create_task()
    каждая задача содержит в себе запуск асинхронной функции get_data(session, link)
    в которую передаётся открытая сессия и линк полученный из глобального списка pagen_lst
    функция gather() одновременно запускает все awaitable объекты которые мы поместили в список tasks

    Output: Запуск асинхронной функции get_data()

    '''
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in pagen_lst:
            task = asyncio.create_task(get_data(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)


url = 'https://parsinger.ru/html/index1_page_1.html'
soup = get_soup(url)
get_urls_categories(soup)
get_urls_pages(category_lst)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
