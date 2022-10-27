# Парсер собирает данные из профилей стартапов на платформе https://platform.slush.org
# Данные собираются с помощью Selenium, имитируюя работу пользователя. Необходимость использования
# Selenium обусловлена тем, что сайт подгружает данные только по частям, через определенные интервалы, при нажатии на определенные кнопки.


import csv
import time
import random
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By



class PlatformParser:
    def __init__(self):
        self._scrolls = 0
        self._total_profiles = 0

    # функиця возващает случайно выбранное значение из заданного диапазона
    # в зависимости от операции разное время засыпания скрипта (скролинг, загрузка страницы, просмотр профиля)
    @staticmethod
    def _awaiting(scroll=False, wait=False, load_profile=False):
        if scroll:
            return random.choice(np.linspace(0.2, 0.5, 5))
        if wait:
            return random.choice(np.linspace(2.0, 2.7, 6))
        if load_profile:
            return random.choice(np.linspace(1.0, 1.5, 5))

    # основная функция, в которой реализована вся логика
    def parse(self, default_args):

        # передаем дополнительные аргументы в webdriver
        options = webdriver.ChromeOptions()
        options.add_argument(default_args.get('user_agent')) # переносим основной профиль из Хрома, т.к. аккаунт закрытый
        options.add_argument('--headless')

        with webdriver.Chrome(options=options) as browser:
            browser.get(default_args.get('url'))  # открваем сайт
            print('Парсер начал работу.')
            time.sleep(self._awaiting(wait=True)) # ожидаем пока прогрузиться страница

            section_button = browser.find_element(By.XPATH, default_args.get('section')) # находим кнопку с нужным разделом
            section_button.click() # переходим в нужный раздел

            time.sleep(self._awaiting(wait=True)) # ожидаем пока прогрузиться страница
            print('Прогружаются все страницы раздела.')

            try:
                load_more_button = browser.find_element(By.XPATH, default_args.get('load_more_button')) # находим в DOM HTML не отображаемую кнопку загрузки контента
                while load_more_button: # до тех пор, пока отображается в DOM HTML кнопка
                    load_more_button.click() # кликаем по ней
                    self._scrolls += 1
                    time.sleep(self._awaiting(scroll=True)) # ожидаем пока подгрузятся данные
            except:
                print(f'Прогружено страниц: {self._scrolls}')

            time.sleep(self._awaiting(wait=True))

            # собираем ссылки на все загруженные аккаунты
            all_profiles = browser.find_elements(By.XPATH, default_args.get('profiles_tag'))

            # открываем файл, куда будем записывать данные
            with open(default_args.get('output_file_name'), 'a', encoding='utf-8-sig', newline='') as file:
                writer = csv.writer(file, delimiter=';')

                # записываем заголовки таблицы
                writer.writerow(tuple(('Name', 'Location', 'LinkedIn', 'Web-site', 'Description')))

                print('Начинается сбор данных из профилей.')

                # проходимся по каждому аккаунту (нужно кликуть на кнопку) и собираем данные
                for profile in all_profiles:
                    blocks = tuple(range(50, 3000, 100)) # точки засыпания скрипта на чуть больший интервал
                    try:
                        profile.click() # кликаем на кнопку "view profile"
                        if self._total_profiles in blocks:
                            time.sleep(self._awaiting(wait=True))
                            print(f'Обработано профилей на текущий момент: {self._total_profiles}')
                        else:
                            time.sleep(self._awaiting(load_profile=True))

                        self._total_profiles += 1

                        # с помощью try except собираем нужню информацию с профиля (не в каждом профиле присутствуют все поля)
                        try:
                            name = browser.find_element(By.XPATH, default_args.get('name_tag')).text
                        except:
                            name = 'None'

                        try:
                            find_location = browser.find_element(By.XPATH, default_args.get('location_tag')).text
                            location = find_location if find_location else 'None'

                        except:
                            location = 'None'

                        try:
                            links = browser.find_elements(By.XPATH, default_args.get('links_tag'))
                            if len(links) >= 2:
                                linkedin = links[0].get_attribute('href')
                                web = links[1].get_attribute('href')
                            elif len(links) == 1:
                                linkedin = links[0].get_attribute('href')
                                web = 'None'
                            else:
                                linkedin, web = 'None', 'None'
                        except:
                            linkedin, web = 'None', 'None'

                        try:
                            raw_descr = browser.find_element(By.XPATH, default_args.get('description_tag')).text
                            descr = ' '.join(raw_descr.strip().split())
                        except:
                            descr = 'None'

                        # записываем собранные данные в файл
                        writer.writerow(tuple((name, location, linkedin, web, descr))) # записываем данные в CSV

                        browser.find_element(By.XPATH, default_args.get('close_button_tag')).click() # закрываем окно профиля
                        time.sleep(self._awaiting(scroll=True)) # делаем небольшую паузу

                    except:
                        time.sleep(self._awaiting(scroll=True))
                        continue

                print(f'Всего обработано профилей: {self._total_profiles}.')
                output = default_args.get('output_file_name')
                print(f'Данные записаны в файл "{output}".')


# аргументы по умолчанию, вынесены отдельно, чтобы можно было легко менять при необходимости
default_args = {
    'output_file_name': 'resuls.csv',
    'url': 'https://platform.slush.org/events/slush22/matchmaking/browse',
    'user_agent': r'user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data\Default',
    'section': "//button[@class='sc-fnGiBr sc-bBABsx sc-iJnaPW sc-bHnazb fjgLxw mrPjC bVuQjJ dnwqMT']",
    'load_more_button': "//button[@class='sc-fnGiBr sc-bBABsx iHSffU mrPjC']",
    'profiles_tag': "//button[@class='sc-fnGiBr sc-dmctIk cPTiCL eDQUpO']",
    'name_tag': "//span[@class='sc-iBYQkv sc-kZHVfI ewJrak folPLM']",
    'location_tag': "//span[@class='sc-iBYQkv sc-djhChl ewJrak ezkLka']",
    'links_tag': "//a[@target='_blank']",
    'description_tag': "//p[@class='sc-ipEyDJ sc-bVxQeI fKUwEv gbVfVC']",
    'close_button_tag': "//img[@class='sc-gIrjMU kcVEpU']"

}


def main(args):
    parser = PlatformParser()
    parser.parse(args)


# запускаем скрипт, собираем данные
if __name__ == '__main__':
    main(default_args)
