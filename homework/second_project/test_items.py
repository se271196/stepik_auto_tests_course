import pytest
import time
from selenium.webdriver.common.by import By

def is_element_present(browser):
    try:
        browser.find_element(By.CSS_SELECTOR,'button.btn-add-to-basket')
        return True
    except:
        return False


def test_check_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #css button.btn-add-to-basket

    assert is_element_present(browser)==True, "Not found button add to basket"
    time.sleep(30)