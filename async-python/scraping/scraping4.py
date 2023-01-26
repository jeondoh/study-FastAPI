import os
import aiohttp
import asyncio
from config import get_secret
import aiofiles


# 스크래핑한 이미지 다운로드
async def img_downloader(session, img):
    img_name = img.split("/")[-1].split("?")[0]

    try:
        os.mkdir("./images")
    except FileExistsError:
        # 같은 폴더가 있을시
        pass

    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
                img_data = await response.read()
                await file.write(img_data)


async def fetch(session, url, i):
    headers = {
        "X-Naver-Client-Id": get_secret("NAVER_API_ID"),
        "X-Naver-Client-Secret": get_secret("NAVER_API_SECRET"),
    }
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result["items"]
        images = [item["link"] for item in items]
        # 이미지 다운로드
        await asyncio.gather(*[img_downloader(session, img) for img in images])


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "cat"
    urls = [f"{BASE_URL}?query={keyword}&display=5&start={1+ i*5}" for i in range(10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.run(main())
