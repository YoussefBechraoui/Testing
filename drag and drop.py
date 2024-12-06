from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time


folder = r"C:\Users\sabri\OneDrive\Bureau\testing"

if not os.path.exists(folder):
    os.makedirs(folder)

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

try:
    source = driver.find_element(By.ID, "column-a")
    target = driver.find_element(By.ID, "column-b")

    initial_screenshot_path = os.path.join(folder, "drag_and_drop_initial.png")
    driver.save_screenshot(initial_screenshot_path)
    print(f"Initial state screenshot saved: {initial_screenshot_path}")

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
    time.sleep(2)  

    
    after_screenshot_path = os.path.join(folder, "drag_and_drop_after.png")
    driver.save_screenshot(after_screenshot_path)
    print(f"Post drag-and-drop screenshot saved: {after_screenshot_path}")

    if source.text == "B" and target.text == "A":
        print("Drag and drop successfully swapped columns.")
    else:
        print("Drag and drop failed or did not produce expected results.")

finally:
    driver.quit()
    print("Testing completed.")
