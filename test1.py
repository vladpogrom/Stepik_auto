from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    input1 = browser.find_element_by_css_selector("[placeholder*=first]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[placeholder*=last]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[placeholder*=email]")
    input3.send_keys("vladpogrom1234@mail.ru")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    assert "Congratulations! You have successfully registered!" == welcome_text_elt.text

finally:
    time.sleep(1)
    browser.quit()
