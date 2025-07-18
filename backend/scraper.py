import requests
from bs4 import BeautifulSoup
import redis
import json

def scrape_page_elements(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.prettify())  # For debugging purposes, to see the HTML structure

    # Scrape the head element
    head = soup.head

    # Scrape the header element (div with class 'bs-header')
    header = soup.find("div", class_="bs-header")
        
    response = {
        "head": str(head) if head else None,
        "header": str(header) if header else None,
    }
    return response

def store_in_redis(data):
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set("scraped_content", json.dumps(data))

def scrape_products(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = []
    # Updated selector for Croma: li with class 'product-item'
    product_cards = soup.find_all('li', class_='product-item')
    for card in product_cards:
        # Title is usually in a tag with class 'product-title' or inside an <a> tag
        title_tag = card.find('a', class_='product-title')
        if not title_tag:
            title_tag = card.find('h3')
        # Price and sale price
        price_tag = card.find('span', class_='amount')
        sale_price_tag = card.find('span', class_='new-price')
        # Discount message
        discount_tag = card.find('span', class_='discount')
        # Product ID (if available)
        product_id = card.get('data-product-id') or card.get('id')
        img_tag = card.find('img')
        image_url = ''
        if img_tag:
            if 'src' in img_tag.attrs and img_tag['src']:
                image_url = img_tag['src']
            elif 'data-src' in img_tag.attrs and img_tag['data-src']:
                image_url = img_tag['data-src']
        products.append({
            'product_id': product_id or '',
            'title': title_tag.text.strip() if title_tag else '',
            'price': price_tag.text.strip() if price_tag else '',
            'sale_price': sale_price_tag.text.strip() if sale_price_tag else '',
            'discount_message': discount_tag.text.strip() if discount_tag else '',
            'image_url': image_url
        })
    return products

def store_products_in_redis(products):
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set("products", json.dumps(products))

if __name__ == "__main__":
    url = "https://www.croma.com/televisions-accessories/c/997"
    page_elements = scrape_page_elements(url)
    store_in_redis(page_elements)
    # Scrape and store products
    products = scrape_products(url)
    print(f"Scraped {len(products)} products")  # <--- Add this line
    store_products_in_redis(products)
    print(products[0]['image_url'])  # Print the first image URL