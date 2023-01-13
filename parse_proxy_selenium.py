from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Parser:
    def __init__(self):
        self.completed_proxy_list = []
        self.source_page = []

    def open_chrome(self):
        with uc.Chrome(version_main=108) as browser:
            browser.get('https://hidemy.name/ru/proxy-list/#list')
            browser.implicitly_wait(10)
            el = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))
            last_pagen = int(browser.find_element(By.CLASS_NAME, 'pagination').find_elements(By.TAG_NAME, 'li')[-2].text)
            if el:
                for x in range(1, last_pagen + 1):
                    try:
                        self.source_page.append(browser.page_source)
                        a = browser.find_element(By.CLASS_NAME, 'next_array').find_element(By.TAG_NAME, 'a')
                        browser.execute_script("window.scrollBy(0,1000)")
                        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(a)).click()
                        print(f'Страница {x} обработана')
                        for link in self.source_page:
                            soup = BeautifulSoup(link, 'lxml')
                            ips = soup.find('table').find_all('tr')
                            port = soup.find('tbody').find_all('tr')
                            for ip, port in zip(ips, port):
                                g = f"{ip.find_all('td')[0].text}:{port.find_all('td')[1].text}\n"
                                print('Прокси сохранён в файл',g,end='')
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
