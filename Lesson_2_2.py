from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    picture1 = browser.find_element_by_id("treasure")
    picture_x = picture1.get_attribute("valuex")
    y = calc(picture_x)

    input1 = browser.find_element_by_css_selector("[id='answer']")
    input1.send_keys(y)
    checkbox1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    checkbox1.click()
    radiobutton1 = browser.find_element_by_css_selector("[id='robotsRule']")
    radiobutton1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
