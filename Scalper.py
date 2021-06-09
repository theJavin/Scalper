

import time

from selenium import webdriver

browser = webdriver.Chrome('/Documents/Projects/Scalper/chromedriver')

# Bestbuy 3070 ti page
# https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789

browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789")

buyButton = False

while not buyButton:

    try:
        addToCartBtn = addButton = browser.find_element_by_class_name_("btn-disabled")

        print("button is not ready yet")

        time.sleep(0.5)
        browser.refresh()

    except:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")
        

