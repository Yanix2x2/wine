from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
from collections import defaultdict

from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas


def year_format(age):
    if 11 <= age % 100 <= 19:
        return 'лет'

    num = age % 10
    if num == 1:
        return 'год'
    elif 2 <= num <= 4:
        return 'года'
    
    return 'лет'


def get_product_categories():
    excel_data_product = pandas.read_excel(
        'wine.xlsx',
        na_values='None',
        keep_default_na=False
    ).to_dict(orient='records')

    products = defaultdict(list)
    for product in excel_data_product:
        products[product['Категория']].append(product)
    return dict(products)


def main():
    age = datetime.datetime.now().year - 1920

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        year=age,
        year_format=year_format(age),
        categories=get_product_categories()

    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
