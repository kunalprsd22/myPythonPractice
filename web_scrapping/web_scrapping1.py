import bs4
import requests

result = requests.get('https://www.aajtak.in/')

bs = bs4.BeautifulSoup(result.text, 'html.parser')

images = bs.select('img')
for image in images:
    print(image['src'])

