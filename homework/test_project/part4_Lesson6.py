from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    part1=browser.find_element(By.ID,"num1").text
    part2 = browser.find_element(By.ID, "num2").text
    sum=int(part1)+int(part2)
    print(sum)
    ##dropdown
    select = Select(browser.find_element(By.ID,"dropdown"))
    #print(select)
    select.select_by_value(str(sum)).click()

    button = browser.find_element(By.XPATH,"//button[contains(text(), 'Submit')]")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()