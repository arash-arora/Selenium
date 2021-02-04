from selenium import webdriver #webdriver links up with the driver and is able to perform the actions
from selenium.webdriver.common.keys import Keys #access to enter or escape key

#explicit wait

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time #to make the program sleep to observe the outputs

PATH = "C:\Program Files (x86)\chromedriver.exe"        #path of the file so we can run it.

driver = webdriver.Chrome(PATH) #Chrome() - browser we'll be using, and the PATH is mentioned and the webdriver for the web browser is located at this path

driver.get("https://techwithtim.net") #opening a webiste
print(driver.title) #title of that website

search = driver.find_element_by_name("s") #find an element named s in html


search.send_keys("test") #search for text in search bar


search.send_keys(Keys.RETURN)#hit enter

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-date")
        print(header.text)
except:
    driver.quit()

# time.sleep(5) #make the program sleep

# print(driver.page_source) #scrape and access the entire website source code
# driver.close() #close the current tab

# driver.quit() #close the entire browser
