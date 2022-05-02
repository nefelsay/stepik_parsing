import json
import os
import requests
import time



headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

def get_data_file(headers):
    # url = 'https://www.landingfolio.com/'
    # r = requests.get(url=url, headers=headers)
    # print(r)
    # with open('index.html', 'w', encoding='utf-8') as file:
    #     file.write(r.text)

    offset = 0
    img_count = 0
    result_list = []

    while True:
        url = f'https://s1.landingfolio.com/api/v1/inspiration/?offset={offset}&color=%23undefined'

        response = requests.get(url=url, headers=headers)
        data = response.json()
        # print(data)
        for item in data:
            if 'description' in item:

                images = item.get('images')
                img_count += len(images)
                for img in images:
                    img.update({
                        'url': f'https://landingfoliocom.imgix.net/{img.get("url")}'
                    })
                result_list.append(
                    {
                        'title': item.get('title'),
                        'description': item.get('description'),
                        'url': item.get('url'),
                        'images': images
                    }

                )

            else:
                with open('output.json', 'w', encoding='utf-8') as file:
                    json.dump(result_list, file, indent=4, ensure_ascii=False)


                return f'[INFO] Work finished '
        offset += 1
        print(f'[+] Processed {offset}. Images count is: {img_count} \n{"-" * 50}')





def donwload_images(file_path):
    try:
        with open(file_path) as file:
            src = json.load(file)

    except Exception as _ex:
        print(_ex)
        return f'[INFO] Check the file path!'


    item_len = len(src)
    count = 1
    for item in src:
        item_name = item.get('title')
        item_imgs = item.get('images')
        # print(item)

        if not os.path.exists(f'data/{item_name}'):
            os.mkdir(f'data/{item_name}')

        for img in item_imgs:
            r = requests.get(url=img['url'])

            with open(f'data/{item_name}/{img["type"]}.png', 'wb') as file:
                file.write(r.content)

        print(f'[+] DONWLOAD {count} / {len(src)}')
        count += 1

    return f'[INFO] Work finished'



def main():
    time_start = time.time()
    # print(get_data_file(headers))
    print(donwload_images('output.json'))
    finish_time = time.time() - time_start
    print(f'Времени затрачено {finish_time}')


if __name__ == '__main__':
    main()
