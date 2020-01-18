import requests

page = requests.get('http://books.toscrape.com/')
print(page.content)