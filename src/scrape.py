
from types import NoneType
import requests
from bs4 import BeautifulSoup, Tag
from urllib.parse import urlparse

class Domain:
    ETSY = 'etsy'


def go_scrape(urls: list):
    parse_dict = []
    for idx, url in enumerate(urls, start=1):
        print(f"{idx} {url}")
        parse_dict.append(parse(url=url))

    return parse_dict


def parse(url) -> list:
    resp = requests.get(url=url)
    domain = urlparse(url).netloc
    if Domain.ETSY in domain:
        soup = BeautifulSoup(resp.text, 'html.parser')
        product_details = scrape_etsy(url, soup=soup)

        print(f"scrapped: {url}")

    return product_details


def scrape_etsy(url, soup: BeautifulSoup):
    product_details = []
    product_details.append(str(url))
    product_details.append(in_stock(soup=soup))
    product_details.append(option(soup=soup))
    product_details.append(get_title_and_auther(
        soup=soup))
    product_details.append(shipping_details(soup=soup))
    product_details.append(price(soup=soup))
    product_details.append(description(soup=soup))
    product_details.append(store(soup=soup))
    product_details.append(categories(soup=soup))
    product_details.append(created(soup=soup))
    product_details.append(country_of_origin(soup=soup))
    product_details.append(image_link(soup=soup))
    return product_details


def in_stock(soup: BeautifulSoup) -> chr:
    div = soup.find(
        'div', attrs={'data-buy-box-region': "stock_indicator"})
    return 'X' if div.p.strong.text.strip() != 'In stock' else ''


def option(soup: BeautifulSoup):
    div = soup.find('select', attrs={
        'id': 'inventory-variation-select-0'
    })
    if not isinstance(div, NoneType):
        for s in div.contents:
            if isinstance(s, Tag) and 'selected' in s.attrs:
                option = s.text.strip()
                return option


def get_title_and_auther(soup: BeautifulSoup) -> str:
    div = soup.find('div', attrs={
        'data-appears-component-name': 'shop_owners',
    })
    auther = str(div.div.div.div.img["alt"])

    h1 = soup.find('h1', attrs={
        'class': 'wt-text-body-03 wt-line-height-tight wt-break-word'
    })
    title = h1.text.strip()
    return f"{title} {auther}"


def price(soup: BeautifulSoup):
    div = soup.find('div', attrs={
        'data-buy-box-region': 'price'
    })
    price = div.div.div.p.text.strip()

    return price


def shipping_details(soup: BeautifulSoup):
    return_policy = ""
    s = soup.find('p', attrs={
        'class': 'wt-text-body-03 wt-mt-xs-1 wt-line-height-tight'
    })
    shipping_time = f"{s.text}"

    r = soup.find('div', attrs={
        'class': 'wt-grid__item-xs-6 wt-pr-xs-2 wt-mb-md-5 wt-mb-xs-4'
    })
    for c in r.children:
        return_policy += c.text

    return f"{shipping_time} {return_policy}"


def description(soup: BeautifulSoup):
    div = soup.find('div', attrs={
        'data-id': 'description-text'
    })
    return div.div.p.text.strip()


def store(soup: BeautifulSoup):
    div = soup.find('div', attrs={
        'id': 'listing-page-cart',
    })
    store = div.div.div.p.a
    return store["href"]


def categories(soup: BeautifulSoup):
    categories = []
    div = soup.find('div', {
        'id': 'wt-content-toggle-tags-read-more'
    })
    for c in div.ul.contents:
        if c.text.strip() == '':
            continue
        categories.append(c.text.strip())

    result = ", ".join(categories)
    return result


def created(soup: BeautifulSoup):
    div = soup.find('div', attrs={
        'class': 'wt-display-flex-xs wt-align-items-baseline wt-flex-direction-row-xs',
    })
    return div.div.text.replace('Listed on', '').strip()


def country_of_origin(soup: BeautifulSoup):
    div = soup.find('div', attrs={
        'class': 'wt-grid__item-xs-12 wt-text-black wt-text-caption'
    })
    return div.text.replace('Ships', '').strip()


def image_link(soup: BeautifulSoup):
    return str(soup.find('div', attrs={
        'class': 'image-carousel-container wt-position-relative wt-flex-xs-6 wt-order-xs-2 show-scrollable-thumbnails'
    }).ul.li.img["src"])
