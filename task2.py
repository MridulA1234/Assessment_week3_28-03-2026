### Vogue.in automation using python selenium
#
# 1. Navigate to https://www.vogue.in/
# 2. Click on Shopping category
# 3. Scroll to Olive Crest (Wings) product and click on it
# 4. New tab opens switch to the new window
# 5. Fetch me the {name:price}

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.vogue.in/")
driver.maximize_window()
sleep(2)


driver.find_element(By.XPATH, '//a[text()="Shopping"]').click()
sleep(3)


product = driver.find_element(By.XPATH, '//img[@alt="Image may contain Accessories Adult Person and Headband"]')
driver.execute_script("arguments[0].scrollIntoView();", product)
sleep(3)
product.click()


all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
sleep(3)


name = driver.find_element(By.TAG_NAME, "h1").text
price = driver.find_element(By.XPATH, '//span[@class="money buckscc-money"]').text
print({name: price})
sleep(3)
driver.quit()
