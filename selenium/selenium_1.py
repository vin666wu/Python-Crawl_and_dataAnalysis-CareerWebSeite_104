import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''below three lines will be figured out for chrome webdriver'''
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = "/usr/lib/google-chrome-stable"
# driver = webdriver.Chrome(options=chrome_options)

'''below three lines are for bug of geckodriver'''
options = webdriver.FirefoxOptions()
options.binary_location = "/usr/lib/firefox/firefox"
driver = webdriver.Firefox(options=options)

driver.get("https://www.google.com")
element = driver.find_element_by_id("APjFqb")
element.clear()
element.send_keys("Python")
# element.submit()            # Submit the search form

#Keys usage, select all textarea, and then copy it
element.send_keys(Keys.SPACE)
time.sleep(1)
element.send_keys("3.11")
time.sleep(3)
element.send_keys(Keys.ENTER)   # Simulate pressing the Enter key to submit the search query
time.sleep(3)
element = driver.find_element_by_id("APjFqb")
element.send_keys(Keys.CONTROL, "a")
time.sleep(2)
element.send_keys(Keys.CONTROL, "c")

#paste to a new page
driver.get("https://www.google.com")
element = driver.find_element_by_id("APjFqb")
element.send_keys(Keys.CONTROL, "v")
element.send_keys(" with Selenium")

#last page and then next page
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
