import asyncio
import aiohttp


all_data = []

async def get_page_data(session, category: str, page_id: int):
    if page_id:
        url = f'https://ozon.ru/brands{category}/?page={page_id}'
    else:
        url = f'https://ozon.ru/brands{category}'

    async with session.get(url) as resp:
        assert resp.status == 200
        print(f'get url {url}')
        resp_text = await resp.text()
        all_data.append(resp_text)
        return resp_text


async def load_site_data():
    categories_list = ['cat1', 'cat2']
    async with aiohttp.ClientSession() as session:
        tasks = []
        for cat in categories_list:
            for page_id in range(100):
                task = asyncio.create_task(get_page_data(session, cat, page_id))
                tasks.append(task)
        await asyncio.gather(*tasks)


asyncio.run(load_site_data())
print(all_data)
