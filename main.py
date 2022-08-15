from lxml import etree
import requests
from bs4 import BeautifulSoup as BS
import json
import os
from datetime import datetime, timezone

menu_url = 'https://www.tacobell.com'
menu_json_name = './menu.json'

menu_table = {}

def time() -> int:
    return int(datetime.now(timezone.utc).timestamp())

def download_menu_and_save():
    global menu_table, menu_json_name
    menu_table = {}
    menu_table['food'] = {}
    agent = {"User-Agent":'Mozilla/5.0 (Gecko on Windows)'}
    page = requests.get(menu_url + '/food', headers=agent)

    container = BS(page.text, features='lxml')
    categories = container.find_all('div', attrs={'class':'content___lUjZW'})

    for category in categories:
        category_name = category.text
        url = category.find('a')['href']

        menu_table['food'][category_name] = []

        category_url = menu_url + url
        
        category_page = None
        cat_container = None
        try:
            category_page = requests.get(category_url, headers=agent)
            cat_container = BS(category_page.text, features='lxml')
        except Exception as e:
            print(f"Failed to go to category page '{category_url}': {e}")
            break

        if cat_container is None:
            print("Failed to get BeautfulSoup")
            return

        foods = cat_container.find_all('div', attrs={'class':'product-card___rCpV7'})

        for food in foods:
            name = food.find('h4').text
            details = food.find('p', attrs={'class':'product-details___2EQ7_'})
            price, cals = details.find_all('span')

            price = float(price.text.replace('$', ''))
            cals = int(cals.text.replace('-', ' ').split()[0])

            food_item = {}
            food_item['name'] = name
            food_item['price'] = price
            food_item['cals'] = cals

            menu_table['food'][category_name].append(food_item)

    menu_table['version'] = 1
    menu_table['time'] = time()

    f = open(menu_json_name, 'w')
    json.dump(menu_table, f)
    f.close()

    return menu_table

def load_menu_json():
    if not os.path.exists(menu_json_name):
        return None

    f = open(menu_json_name, 'r')
    data = json.load(f)
    f.close()

    return data

if __name__ == "__main__":
    menu_table = None

    menu_table = load_menu_json()

    then = 0
    try:
        then = menu_table['time']
    except Exception as e:
        pass
    
    now = time() - then

    if menu_table is None or now > 259200:
        print("Downloading Taco Bell menu...")
        menu_table = download_menu_and_save()
    else:
        print("Using cached Taco Bell menu from disk...")

    if menu_table is None:
        print("Failed to load menu data somewhere, sorry")
        exit()

    for category in menu_table['food'].keys():
        sorted_items = sorted(menu_table['food'][category], key=lambda x:x['cals'] / (x['price'] if x['price'] != 0 else 1))

        print(category)
        for food in sorted_items:
            cals_per_unit_price = food['cals'] / (food['price'] if food['price'] != 0 else 1)
            print(f"\t{int(cals_per_unit_price)}\t{food['name']}")