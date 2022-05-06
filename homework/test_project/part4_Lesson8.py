from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    #<input type="text" name="firstname" class="form-control" placeholder="Enter first name" required="" maxlength="32">
    input1 = browser.find_element(By.NAME,"firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME,"lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME,"email")
    input3.send_keys("t@test.ru")


    input4 = browser.find_element(By.ID, "file")
    input4.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()