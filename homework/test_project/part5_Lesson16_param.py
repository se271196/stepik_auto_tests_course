import time
import math
import pytest
import unittest
from selenium import webdriver
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def f():
    return math.log(int(time.time()+1.1))

#links=["236895", "236896","236897","236898","236899","236903","236904","236905"]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestLogin:
    @pytest.mark.parametrize('links', ["236895", "236896","236897","236898","236899","236903","236904","236905"])
    def test_guest_should_see_login_link(self,browser,links):
        browser.implicitly_wait(10)
        link = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(link)
        input1=browser.find_element(By.TAG_NAME,"textarea")
        input1.send_keys(str(f()))


        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()
        text=browser.find_element(By.CSS_SELECTOR,"pre.smart-hints__hint").text
    #pre.smart-hints__hint
        assert 'Correct!'==text,F"ACTUAL:{text}; Expected Correct"
        print(text)


