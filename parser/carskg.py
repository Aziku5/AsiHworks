import requests
from parsel import Selector
from db.queries import save_cars, init_db, create_tables

url = 'https://www.mashina.kg/'

def get_html():
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

def parse_html(html):
    selector = Selector(text=html)
    return selector
init_db()
create_tables()
html = get_html()
selector = parse_html(html)
cars = selector.css('.listing.x-3.mb-80 .listing-item.main')
for car in cars:
    title = car.css('a span[title]::text').get()
    price = car.css('.font-big.custom-margins::text').get()
    save_cars(title, price)