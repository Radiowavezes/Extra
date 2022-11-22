import requests
import json
from copy import deepcopy
import concurrent.futures


params = {
    "apiKey": "51a2b38a0d27d3445d7a49c2ebf0a697",
    "oddsFormat": "american",
    "markets": "h2h",
    "regions": "us",
}
urls = ["https://api.the-odds-api.com/v4/sports/upcoming/odds/"] * 3

def get_page(url, params, timeout=5):
    response = requests.get(url, params, timeout=timeout)
    json_object = response.json()
    with open("sample.json", "w+", encoding="utf-8") as json_file:
            working_object = deepcopy(json_object)

            for ind, row in enumerate(json_object):
                working_object[ind].pop("bookmakers")

            json.dump(sorted(working_object, key=lambda x: x["commence_time"]), json_file)
    return 'Done'

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in urls:
        futures.append(executor.submit(get_page, url=url, params=params))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
