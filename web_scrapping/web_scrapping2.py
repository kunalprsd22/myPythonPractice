import bs4
import requests


basic_url = "https://books.toscrape.com/catalogue/page-{}.html"
result = requests.get(basic_url.format(1))
soup = bs4.BeautifulSoup(result.text, "html.parser")

books = soup.select(".product_pod")

for book in books:
    print(book.select('a')[1]['title'])