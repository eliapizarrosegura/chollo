from pandas import DataFrame

from chollometro.drivers.ChromeDriver import *
from chollometro.model.Product import Product
import pandas as pd

driver().get("https://www.chollometro.com/nuevos")

COLUMNS = ["CATEGORY", "IMAGE", "NAME", "PRICE", "OLD_PRICE", "RATE", "DELIVERY", "MSG", "USER", "LINK"]

CATALOG = driver().find_elements_by_css_selector("section.gridLayout > div.gridLayout-item > article")

catalog = [item for item in CATALOG]

products_catalog = []

for item in catalog:

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

    products_catalog.append(Product(category,
                                    image,
                                    name,
                                    price,
                                    old_price,
                                    rate,
                                    delivery,
                                    msg,
                                    user,
                                    link
                                    ))
df: DataFrame = DataFrame()


for x in products_catalog:
    # print(x.get_name() + " -> " + x.get_price() + " -> " + x.get_rate())

    df.append(pd.DataFrame(products_catalog,COLUMNS))
print(df)
driver().close()
