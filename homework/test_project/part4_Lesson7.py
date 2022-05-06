from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

link="http://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')

    x = x_element.text
    y = calc(x)
#<input id="answer" class="form-control" type="text" required="">
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
#<input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
    input2 = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
    input2.click()
#<input class="form-check-input" type="radio" name="ruler" id="robotsRule" value="robots">
    input3 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    input3.click()
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
#<button type="submit" class="btn" disabled="disabled">Submit</button>
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()