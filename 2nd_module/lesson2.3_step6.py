from selenium import webdriver
import time
from math import log, sin
browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.find_element_by_css_selector("button.trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_css_selector("#input_value").text
    y = log(abs(12*sin(int(x))))
    browser.find_element_by_css_selector("#answer").send_keys(str(y))
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
