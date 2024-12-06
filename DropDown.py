from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time


folder = r"C:\Users\sabri\OneDrive\Bureau\testing"


if not os.path.exists(folder):
    os.makedirs(folder)


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

try:
    dropdown = Select(driver.find_element(By.ID, "dropdown"))

   
    path = os.path.join(folder, "dropdown_initial.png")
    driver.save_screenshot(path)
    print(f"Initial state screenshot saved: {path}")

    options = dropdown.options
    for index, option in enumerate(options):
        if index == 0: 
            continue

       
        dropdown.select_by_index(index)
        time.sleep(1)  

   
        selected_option = dropdown.first_selected_option
        assert selected_option.text == option.text, f"Option {option.text} not selected correctly!"

      
        screenshot_path = os.path.join(folder, f"dropdown_option_{index}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot after selecting {option.text} saved: {screenshot_path}")

    print("Dropdown test completed successfully.")

finally:
    driver.quit()
    print("Testing completed.")
