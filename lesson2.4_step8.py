from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.maximize_window()
    browser.get(link)

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book = browser.find_element_by_id("book")
    book.click()

    var_x = browser.find_element_by_id("input_value")
    x = int(var_x.text)
    y = str(math.log(abs(12*math.sin(x))))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
