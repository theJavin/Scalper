

import time

from selenium import webdriver

browser = webdriver.Chrome('/home/particle/Documents/Mcprojects/Scalper/chromedriver')

# Bestbuy 3070 ti page
# https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789
#Bestbuy 3080 page
#https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440

browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")

buyButton = False

while not buyButton:
  try:
      addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")
      print("Card not available.")
      print("refreshing...")
      browser.refresh()
      time.sleep(1)  
      

  except:
    addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")
    addToCartBtn.click()
    print("Card added to cart!")
    buyButton = True
    time.sleep(3)
    
try:
  goToCartBtn = addButton = browser.find_element_by_class_name("go-to-cart-button")
  goToCartBtn.click()
  print("Going to cart!")
  time.sleep(3)

except:
  browser.quit()

