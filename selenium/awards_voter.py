from selenium import webdriver
from selenium.webdriver.common.by import By
import time

votes = 0

while True:
    driver = webdriver.Firefox()
    driver.get("https://www.thuisbezorgd.nl/awards/2023/nl/detail/best-sushi")
    driver.delete_all_cookies()

    time.sleep(0.5)
    cookie_notice = driver.find_element(By.CLASS_NAME, "button.cookie-notice__button.accept.button--outline")
    cookie_notice.click()

    buttons = driver.find_elements(By.CLASS_NAME, "nominee-card__vote-button")
    if buttons == []:
        driver.close()
        continue

    kaneda = buttons[7]
    kaneda.click()

    confirm = driver.find_element(By.CLASS_NAME, "voting-prepare__confirm-button")
    confirm.click()

    votes += 1
    print(votes)

    time.sleep(1)
    driver.close()

