import os
import json
import datetime
import csv
import requests

headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Is-Ajax-Request': 'X-Is-Ajax-Request',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',

}

def get_data():
    start_time = datetime.datetime.now()
    # url = 'https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y'
    url = 'https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&PAGEN_1=1'

    r = requests.get(url=url, headers=headers)
    # print(r.json())
    #
    # # with open('index.html', 'w', encoding='utf-8') as file:
    # #     file.write(r.text)
    # with open('info.json', 'w') as file:
    #     json.dump(r.json(),file, indent=4, ensure_ascii=False)


    page_count = r.json()['pageCount']

    data_list = []
    for page in range(1, page_count):
        url = f'https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&PAGEN_1={page}'
        r = requests.get(url=url, headers=headers)
        data = r.json()
        items = data['items']
        possible_store = ['discountStroes', 'fortochkiStores', 'commonStores']
        for item in items:
            total_amount = 0
            item_name = item['name']
            item_price = item['price']
            item_img = f"https://roscarservis.ru{item['imgSrc']}"
            item_url = f"https://roscarservis.ru{item['url']}"

            stores = []
            for ps in possible_store:
                if ps in item:
                    if item[ps] is None or len(item[ps]) < 1:
                        continue
                    else:
                        for store in item[ps]:
                            store_name = store["STORE_NAME"]
                            store_price = store['PRICE']
                            store_amount = store['AMOUNT']
                            total_amount += int(store['AMOUNT'])
                            stores.append({
                                'store_name': store_name,
                                'store_price': store_price,
                                'store_amount': store_amount,
                            })
        data_list.append({
            'name': item_name,
            'price': item_price,
            'url': item_url,
            'img_url': item_img,
            'stores': stores,
            'total_amount': total_amount
        })
        print(f'[INFO] Обработал {page} / {page_count}')
    current_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')

    with open(f'data_{current_time}.json', 'w') as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)

    diff_time = datetime.datetime.now() - start_time
    print(f'Затрачено времени {diff_time}')


def main():
    get_data()


if __name__ == '__main__':
    main()
