import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

screenshot_folder = r"C:\Users\sabri\OneDrive\Bureau\testing"
screenshot_path_valid = os.path.join(screenshot_folder, "valid_login_screenshot.png")
screenshot_path_invalid = os.path.join(screenshot_folder, "invalid_login_screenshot.png")

if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

try:
    print("Testing wrong username")
    
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(2)  

    error_message = driver.find_element(By.ID, "flash").text
    if "Your username is invalid!" in error_message:
        print("PASSED")
        driver.save_screenshot(screenshot_path_invalid)
    else:
        print("FAILED")

    print("Testing valid username")
    
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(2)  

    success_message = driver.find_element(By.ID, "flash").text
    if "You logged into a secure area!" in success_message:
        print("PASSED")
        driver.save_screenshot(screenshot_path_valid)
    else:
        print("FAILED")

finally:
    driver.quit()
    print("Testing completed.")
