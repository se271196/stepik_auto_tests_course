import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # <img src="images/chest.png" height="40" width="40" id="treasure" valuex="115">
    x_element = browser.find_element_by_id('treasure').get_attribute('valuex')
    print(x_element)
    # x = x_element.text
    y = calc(x_element)
    # <input id="answer" class="form-control" type="text" required="">
    input1 = browser.find_element_by_id("answer")

    input1.send_keys(y)
    # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()
    # <input class="form-check-input" type="radio" name="ruler" id="robotsRule" value="robots">
    input3 = browser.find_element_by_id("robotsRule")
    input3.click()
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()
# <button type="submit" class="btn" disabled="disabled">Submit</button>
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
