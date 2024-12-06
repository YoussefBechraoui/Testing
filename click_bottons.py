from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time

# Define folder for screenshots
screenshot_folder = r"C:\Users\sabri\OneDrive\Bureau\testing"

# Create the folder if it doesn't exist
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Login credentials
username = "standard_user"
password = "secret_sauce"

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the login page
    driver.get("https://www.saucedemo.com/")

    # Locate username and password fields and the login button
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Enter login credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click the login button
    login_button.click()

    # Wait for the inventory page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))

    print("Login successful. Navigated to inventory page.")

    # Example: Verify the "menu button" is clickable (adjust selector as needed)
    element_selector = "#react-burger-menu-btn"  # Replace with the selector of the upload button or link
    upload_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_selector)))

    # Check if the button/link is clickable
    if upload_button.is_enabled():
        print("Upload button is clickable.")
        upload_button.click()  # Optional: Simulate a click action
    else:
        print("Upload button is not clickable.")

    # Take a screenshot
    screenshot_path = os.path.join(screenshot_folder, "upload_button_test.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

except TimeoutException:
    print("Login failed or the button/link is not clickable.")
finally:
    # Close the browser
    time.sleep(2)  # Optional delay to observe
    driver.quit()
    print("Testing completed.")
