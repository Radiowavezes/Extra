import requests
from requests.sessions import Session
import time
from threading import Thread, local
from queue import Queue
import json
from copy import deepcopy
import threading


def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session

def download_link(params, q) -> None:
    session = get_session()
    while True:
        url = q.get()
        with session.get(url, params = params) as response:
            result = response.content
            print(f'Read {len(result)} from {url}')
            with open("sample.json", "w+", encoding="utf-8") as json_file:
                json_object = response.json()
                working_object = deepcopy(json_object)
                for ind, _ in enumerate(json_object):
                    working_object[ind].pop("bookmakers")
                working_object = sorted(working_object, key=lambda x: x["commence_time"])
                json.dump(working_object, json_file)
        q.task_done()
        
def download_all(params, q) -> None:
    thread_num = 3
    for _ in range(thread_num):
        t = threading.Thread(target=download_link, args=(params, q))
        t.start()
    q.join()
    
        
params = {
    "apiKey": "51a2b38a0d27d3445d7a49c2ebf0a697",
    "oddsFormat": "american",
    "markets": "h2h",
    "regions": "us",
}
url_list = ["https://api.the-odds-api.com/v4/sports/upcoming/odds/"] * 3
q = Queue(maxsize=0)            #Use a queue to store all URLs

for url in url_list:
    q.put(url)

thread_local = local()

start = time.time()
download_all(params, q)
end = time.time()
print(f'download {len(url_list)} links in {end - start} seconds')
