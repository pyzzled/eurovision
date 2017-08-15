from bs4 import BeautifulSoup
import requests

page = requests.get("http://www.escstats.com/winners.htm")
soup = BeautifulSoup(page.content, "html.parser")

winners = {}

for row in soup.find_all('tr'):
    if row.contents[0].name != 'th':
        country = row.contents[2].contents[0]
        year = int(row.contents[0].contents[0])
        if year > 1955:
            if country in winners:
                winners[country] = winners[country] + 1
            else:
                winners[country] = 1

items = [(v, k) for k, v in winners.items()]
items.sort()
items.reverse()
items = [(k, v) for v, k in items]

print(items)

