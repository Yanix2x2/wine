from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
from collections import defaultdict
import argparse

from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas


def get_age_suffix(age):
    if 11 <= age % 100 <= 19:
        return 'лет'

    num = age % 10
    if num == 1:
        return 'год'
    elif 2 <= num <= 4:
        return 'года'
    
    return 'лет'


def get_product_categories(path_to_file):
    excel_data_product = pandas.read_excel(
        io=path_to_file,
        na_values='None',
        keep_default_na=False
    ).to_dict(orient='records')

    products = defaultdict(list)
    for product in excel_data_product:
        products[product['Категория']].append(product)
    return dict(products)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file', 
        '-f',
        type=str,
        default='wine.xlsx',
        help='Path to Excel file'
    )
    args = parser.parse_args()

    age = datetime.datetime.now().year - 1920

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        year=age,
        noun=get_age_suffix(age),
        categories=get_product_categories(args.file)

    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
