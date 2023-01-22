import time
import requests
import os
import threading
from concurrent.futures import ThreadPoolExecutor


# 멀티쓰레딩
# 멀티쓰레딩은 파이썬에서 병렬적으로 처리되지 않음
# 멀티 프로세싱 코드(GIL) 입력 필요
def fetcher(params):
    session = params[0]
    url = params[1]

    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://github.com", "https://apple.com"] * 50

    # 최대 쓰레드 개수 정의
    executor = ThreadPoolExecutor(max_workers=10)

    with requests.Session() as session:
        params = [(session, url) for url in urls]
        results = list(executor.map(fetcher, params))
        print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 싱글 쓰레드 - 8.1초 / 멀티 쓰레드(10) - 5.3초
