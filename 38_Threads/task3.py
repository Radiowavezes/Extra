import requests
import json
from copy import deepcopy


params = {'apiKey':'51a2b38a0d27d3445d7a49c2ebf0a697',
          'oddsFormat':'american',
          'markets':'h2h',
          'regions':'us'
          }
response = requests.get(
    'https://api.the-odds-api.com/v4/sports/upcoming/odds/', params)

with open('sample.json', 'w+', encoding='utf-8') as json_file:
    json_object = response.json()
    working_object = deepcopy(json_object)
    
    for ind, row in enumerate(json_object):
        working_object[ind].pop('bookmakers')
                
    json.dump(sorted(working_object, key=lambda x: x['commence_time']), json_file)