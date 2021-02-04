from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")

link =  driver.find_element_by_link_text("Python Programming")
link.click()


try:
    
    link2 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    # link2.clear() #clear the input field
    link2.click()

    link3 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    link3.click()

    driver.back() #Navigating the previous page
    driver.back()
    driver.back()

    driver.forward() #Navigate to the next page in the cache memory


except:
    driver.quit()
