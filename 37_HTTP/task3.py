import requests

user_city = input('Please, enter your city: ')
params = {'q': user_city, 'appid': '8cf47baf9ffbf5feed8db66ecb307ff6', 'units':'metric'}
url = 'https://api.openweathermap.org/data/2.5/weather?'
weather = requests.get(url, params)
data = weather.json()
for key, value in data['main'].items():
    print(f'{key.capitalize()}: {value}')
