from selenium import webdriver
from selenium.webdriver.common.by import By
from threading import Thread

def run():
    driver = webdriver.Firefox()
    driver.get("https://www.24baby.nl/babynamen/nathan/")
    
    while True:
        cookie_notice = driver.find_element(By.ID, "allowcookie")
        cookie_notice.click()

        button = driver.find_element(By.XPATH, '//*[@id="replace-on-vote"]/div/div/button[1]')
        button.click()

        driver.delete_all_cookies()
        driver.refresh()

for i in range(5):
    Thread(target=run).start()