import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
#<span class="nowrap" id="input_value">346</span>

link="http://suninjuly.github.io/math.html"

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
    input2.click()
#<input class="form-check-input" type="radio" name="ruler" id="robotsRule" value="robots">
    input3 = browser.find_element_by_id("robotsRule")
    input3.click()
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()
#<button type="submit" class="btn" disabled="disabled">Submit</button>
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()