import requests

wikipedia = requests.get('https://en.wikipedia.org/w/api.php')

with open('robots.txt', 'w', encoding='utf-8') as text_file:
     text_object = wikipedia.text
     text_file.write(text_object)
