from selenium import webdriver
import time
import os
browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    browser.find_element_by_css_selector("[name=firstname]").send_keys("Alex")
    browser.find_element_by_css_selector("[name=lastname]").send_keys("Axel")
    browser.find_element_by_css_selector("[name=email]").send_keys("Minsk")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    browser.find_element_by_css_selector("#file").send_keys(file_path)
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
