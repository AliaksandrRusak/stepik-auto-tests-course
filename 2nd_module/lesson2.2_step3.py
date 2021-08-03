from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    x = browser.find_element_by_css_selector("#num1").text
    y = browser.find_element_by_css_selector("#num2").text
    z = str(int(x) + int(y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
