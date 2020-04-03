from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("vladpogrom1234@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text.txt')  # добавляем к этому пути имя файла
    send1 = browser.find_element_by_id("file")
    send1.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
finally:
    time.sleep(8)
    browser.quit()
