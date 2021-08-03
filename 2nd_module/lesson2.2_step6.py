from selenium import webdriver
import time
from math import log, sin
browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element_by_css_selector("#input_value").text
    y = log(abs(12*sin(int(x))))
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_css_selector("#answer").send_keys(str(y))
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()
