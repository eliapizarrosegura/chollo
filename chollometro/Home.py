
from chollometro.drivers.ChromeDriver import *

driver().get("https://www.chollometro.com/nuevos")

HOMELIST = driver().find_elements_by_css_selector(".cept-listing--card > div")
NAMES = driver().find_elements_by_css_selector("strong.thread-title")
PRICES = driver().find_elements_by_css_selector("span.thread-price")

titles = [name.text for name in NAMES]
prices = [price.text for price in PRICES]
catalog = []

listamapeada = list(map(lambda x, y: x+ ' -> ' +y, titles, prices))

for x in listamapeada:
    print(x)

# time.sleep(3)
driver().close()
