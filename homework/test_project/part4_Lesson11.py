from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link="http://suninjuly.github.io/explicit_wait2.html"

#<button type="submit" class="trollface btn btn-primary">I want to go on a magical journey!</button>

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    #ожидание
    browser.implicitly_wait(5)
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))

    button = browser.find_element(By.ID,"book")
     #   find_element_by_css_selector("buttonbook")
    button.click()




    x_element = browser.find_element_by_id('input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(': ')[-1])
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()