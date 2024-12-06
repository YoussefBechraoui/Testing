from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
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

    # Locate all "Add to Cart" buttons
    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")

    print(f"Found {len(add_to_cart_buttons)} 'Add to Cart' buttons. Testing them...")

    for index in range(len(add_to_cart_buttons)):
        # Re-locate the button before interacting (to avoid stale references)
        add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        button = add_to_cart_buttons[index]

        # Take a screenshot before clicking
        before_click_path = os.path.join(screenshot_folder, f"add_to_cart_{index + 1}_before.png")
        driver.save_screenshot(before_click_path)
        print(f"Before click screenshot saved: {before_click_path}")

        # Click the "Add to Cart" button
        button.click()
        time.sleep(1)  # Small delay to simulate real interaction

        # Re-locate the button again and check the text
        add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        button = add_to_cart_buttons[index]
        updated_button_text = button.text
        assert updated_button_text == "Remove", f"Button {index + 1} did not change to 'Remove' after clicking."

        print(f"Button {index + 1} works correctly. It changed to 'Remove'.")

        # Take a screenshot after clicking
        after_click_path = os.path.join(screenshot_folder, f"add_to_cart_{index + 1}_after.png")
        driver.save_screenshot(after_click_path)
        print(f"After click screenshot saved: {after_click_path}")

    print("All 'Add to Cart' buttons tested successfully.")

except TimeoutException:
    print("Login failed or 'Add to Cart' buttons could not be tested.")
except StaleElementReferenceException as e:
    print(f"Stale element encountered: {e}")
finally:
    # Close the browser
    time.sleep(2)  # Optional delay to observe
    driver.quit()
    print("Testing completed.")
