from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    input1 = browser.find_element_by_class_name("btn.btn-primary")
    input1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector("[id='answer']")
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()

