from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

screenshot_folder = r"C:\Users\sabri\OneDrive\Bureau\testing"

if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

try:
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    print("Testing checkboxes:")

    for index, checkbox in enumerate(checkboxes):
        is_checked = checkbox.is_selected()
        print(f"Checkbox {index + 1} initial state: {'Checked' if is_checked else 'Unchecked'}")

        initial_screenshot_path = os.path.join(screenshot_folder, f"checkbox_{index + 1}_initial.png")
        driver.save_screenshot(initial_screenshot_path)
        print(f"Initial state screenshot saved: {initial_screenshot_path}")

        checkbox.click()
        time.sleep(1)  

        new_state = checkbox.is_selected()
        print(f"Checkbox {index + 1} new state: {'Checked' if new_state else 'Unchecked'}")

        new_state_screenshot_path = os.path.join(screenshot_folder, f"checkbox_{index + 1}_new_state.png")
        driver.save_screenshot(new_state_screenshot_path)
        print(f"New state screenshot saved: {new_state_screenshot_path}")

        assert is_checked != new_state, f"Checkbox {index + 1} did not toggle properly!"

    print("All checkboxes toggled successfully.")

finally:
    driver.quit()
    print("Testing completed.")
