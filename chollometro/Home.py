import pprint

from pandas import DataFrame

from chollometro.drivers.ChromeDriver import *
from chollometro.model.Product import Product
import json
import pandas as pd

driver().get("https://www.chollometro.com/nuevos")

# COLUMNS = ["CATEGORY", "IMAGE", "NAME", "PRICE", "OLD_PRICE", "RATE", "DELIVERY", "MSG", "USER", "LINK"]

# Selector del catalogo en bruto
CATALOG = driver().find_elements_by_css_selector("section.gridLayout > div.gridLayout-item > article")

# Lista con los webelements del catalogo
catalog = [item for item in CATALOG]

products_catalog_json = []

for item in catalog:

#Selectores de los atributos aplicados a cada item
    try:
        category = item.find_element_by_css_selector(
            "section.gridLayout > div.gridLayout-item > article > div > div > span").text
    except:
        category = "..."

    try:
        image = item.find_element_by_class_name("thread-image").get_attribute("src")
    except:
        image = "..."
    try:
        name = item.find_element_by_class_name("thread-title").text
    except:
        name = "..."
    try:
        price = item.find_element_by_class_name("thread-price").text
    except:
        price = "..."
    try:
        old_price = item.find_element_by_css_selector(
            "section.gridLayout > div.gridLayout-item > article > div:nth-child(4) > span:nth-child(2) > span:nth-child(1)").text
    except:
        old_price = "..."
    try:
        rate = item.find_element_by_css_selector(
            "section.gridLayout > div.gridLayout-item > article > div:nth-child(4) > span:nth-child(2) > span:nth-child(2)").text
    except:
        rate = "..."
    try:
        delivery = item.find_element_by_css_selector(
            "section.gridLayout > div.gridLayout-item > article > div:nth-child(4) > span:nth-child(3) > span > span").text
    except:
        delivery = "..."
    try:
        msg = item.find_element_by_css_selector(
            "section.gridLayout > div.gridLayout-item > article > div:nth-child(5) > div > div").text
    except:
        msg = "..."
    try:
        user = item.find_element_by_class_name("thread-username").text
    except:
        user = "..."
    try:
        link = item.find_element_by_css_selector(
            "section.gridLayout > div.gridLayout-item > article > div:nth-child(7) > a").get_attribute("href")
    except:
        link = "..."

# Se añade un diccionario con los atributos de cada item a la lista_json
    products_catalog_json.append(
        {
        'category': category,
        'image': image,
        'name': name,
        'price': price,
        'old_price': old_price,
        'rate': rate,
        'delivery': delivery,
        'msg': msg,
        'user': user,
        'link': link
        }
    )


for x in products_catalog_json:

    if x['rate'][2:-2].isnumeric() and int(x['rate'][2:-2]) > 35:
        print(x['rate'])
        print(x['link'])


driver().close()
