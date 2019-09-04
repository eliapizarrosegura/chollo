from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
# options.add_argument(" — incognito")
__driver = webdriver.Chrome(executable_path=r"C:\Users\JRO16\Documents\chromedriver.exe",options=options)

def driver()->webdriver:
    return __driver

