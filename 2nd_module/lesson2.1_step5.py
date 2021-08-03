from selenium import webdriver
import time
import math
browser = webdriver.Chrome()


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text

    y = calc(x)

    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
