from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class Parser:
    def __init__(self):
        self.completed_proxy_list = []
        self.source_page = []

    def open_chrome(self):
        # УКАЖИТЕ АКТУАЛЬНУЮ ВЕРСИЮ БРАУЗЕРА version_main=108 
        # chrome://version/  - в адресной строке браузера
         with uc.Chrome(version_main=114,service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())) as browser:
            browser.get('https://hidemy.name/ru/proxy-list/#list')
            browser.implicitly_wait(10)
            el = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))
            last_pagen = int(browser.find_element(By.CLASS_NAME, 'pagination').find_elements(By.TAG_NAME, 'li')[-2].text)
            if el:
                for x in range(1, last_pagen + 1):
                    try:
                        source = browser.page_source
                        a = browser.find_element(By.CLASS_NAME, 'next_array').find_element(By.TAG_NAME, 'a')
                        browser.execute_script("window.scrollBy(0,1000)")
                        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(a)).click()
                        print(f'Страница {x} обработана')
                        soup = BeautifulSoup(source, 'lxml')
                        ips = soup.find('table').find('tbody').find_all('tr')
                        port = soup.find('table').find('tbody').find_all('tr')
                        for ip, port in zip(ips, port):
                            g = f"{ip.find_all('td')[0].text}:{port.find_all('td')[1].text}\n"
                            print('Прокси сохранён в файл', g, end='')
                            file = open('proxy_list.txt', 'a')
                            file.write(g)
                        file.close()
                    except Exception:
                        continue


    def main(self):
        self.open_chrome()
        
        
if __name__ == '__main__':
    parse = Parser()
    parse.main()
