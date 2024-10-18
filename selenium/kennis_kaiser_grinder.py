from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

count = 0

driver = webdriver.Firefox()
driver.get("https://studygo.com/nl/learn/sign-in")

time.sleep(1)
inp = driver.find_elements(By.CLASS_NAME, "wrts-input.light")

email = inp[0]
password = inp[1]

email.send_keys("12646@hageveld.nl")
password.send_keys("Spyro7878")

submit = driver.find_element(By.CLASS_NAME, "wrts-btn-primary.green.light")
submit.click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[3]/section/div/div[1]/a"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div/div/div[1]/div/div/div[1]/button"))).click()

oefeningen = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/div/button")))
oefeningen.click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[1]/input"))).send_keys("maar")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div[1]/div/button"))).click()

while True:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div/div/div[1]/div/div/div[1]/button"))).click()


    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div[3]/div/button"))).click()

    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[1]/input"))).send_keys("maar")
    except:    
        try: 
            WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[3]/section/div/div/a"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div/div/div[1]/div/div/div[1]/button"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div[3]/div/button"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[1]/input"))).send_keys("maar")
        except:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[1]/input"))).send_keys("maar")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div[1]/div/button"))).click()
    count += 1
    print(count)
    
