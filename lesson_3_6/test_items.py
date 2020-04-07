link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    button = len(browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert button > 0, 'Элемент не найден'
