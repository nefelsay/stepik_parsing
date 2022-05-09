# pip3 install requests
import requests

url = 'https://httpbin.org/'  # сервис для тестирования запросов
# url = 'https://www.youtube.com/results?search_query=BMW'
# query = {'search_query':'BMW'}
# responce = requests.get(url, params=query)  # чтобы получить данный от кого либо сайти или сервера используется метод get

responce = requests.get(url, stream=True) # Параметр stream даёт возможность удерживать соеденение с сервером и получать большой файл частями
# print(responce.encoding)
# Если ты записываешь контент, видео, аудио, картинку, знать кодировка не нужно
with open('file_2.txt', 'w') as file:
    for piece in responce.iter_content(chunk_size=500): # итерируемся частям большого файла размером в 5000кб
        print('piece write')
        # file.write(piece.decode('utf-8'))
# print('HEADERS ---', responce.headers)     # Показывает заголовки HTTP
# HEADERS --- {'Date': 'Thu, 18 Nov 2021 07:28:25 GMT',
#               'Content-Type': 'text/html; charset=utf-8',
#               'Content-Length': '9593', 'Connection': 'keep-alive',
#               'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*',
#               'Access-Control-Allow-Credentials': 'true'}
print('STATUS CODE ---', responce.status_code)  # Показывает код статуса
#                STATUS CODE --- 200 status_code
                    # Информационные 100 - 199
                    # Успешные 200 - 299
                    # Перенаправления 300 - 399
                    # Клиентские ошибки 400 - 499
                    # Серверные ошибки 500 - 599
# print('REQUESTS ---', responce.request)     # показывает тип запроса
#                REQUESTS --- <PreparedRequest [GET]> requests
print('URL ---', responce.url)
# print('CONTENT ---', responce.content)
# print('TEXT ---', responce.text)  # Покажет HTML код страницы
# print('JSON ---', responce.json) # если сервер способен отдавать данный в формате JSON он отдаст их в этом формате
# with open('file_1.txt', 'w', encoding='utf-8') as file:
#     file.write(responce.url)
