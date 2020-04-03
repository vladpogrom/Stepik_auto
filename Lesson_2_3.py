from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    input1 = browser.find_element_by_id("num1")
    input1 = input1.text
    input2 = browser.find_element_by_id("num2")
    input2 = input2.text
    x = int(input1) + int(input2)
    x = str(x)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(x)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
finally:
    time.sleep(5)
    browser.quit()
