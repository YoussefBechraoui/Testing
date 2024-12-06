from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Define folder for screenshots
screenshot_folder = r"C:\Users\sabri\OneDrive\Bureau\testing"

# Create the folder if it doesn't exist
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Login credentials
username = "problem_user"
password = "secret_sauce"

# Initialize WebDriver
driver = webdriver.Chrome()

def capture_full_screen_screenshot(driver, file_path):
    # Maximize the window to ensure full screen capture
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to adjust to the new size

    # Capture the full screen screenshot
    driver.save_screenshot(file_path)
    print(f"Full screen screenshot saved at {file_path}")

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

    # Capture full screen screenshot before applying the filter
    before_filter_screenshot_path = os.path.join(screenshot_folder, "before_filter_full_screen.png")
    capture_full_screen_screenshot(driver, before_filter_screenshot_path)

    # Get the prices of the products before sorting
    product_prices_before = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices_before = []
    for price in product_prices_before:
        price_text = price.text.strip().replace('$', '')
        prices_before.append(float(price_text))

    print("Product prices before sorting:")
    print(prices_before)

    # Apply the filter (Price (low to high))
    sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    sort_dropdown.click()

    # Select "Price (low to high)"
    price_low_to_high_option = driver.find_element(By.XPATH, "//option[@value='lohi']")
    price_low_to_high_option.click()
    time.sleep(2)  # Wait for items to reload and be sorted

    # Capture full screen screenshot after applying the filter
    after_filter_screenshot_path = os.path.join(screenshot_folder, "after_filter_full_screen.png")
    capture_full_screen_screenshot(driver, after_filter_screenshot_path)

    # Get the prices of the products after sorting
    product_prices_after = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices_after = []
    for price in product_prices_after:
        price_text = price.text.strip().replace('$', '')
        prices_after.append(float(price_text))

    print("Product prices after sorting:")
    print(prices_after)

    # Verify that the prices are sorted
    sorted_prices = sorted(prices_before)
    if prices_after == sorted_prices:
        print("The products are correctly sorted by price (low to high).")
    else:
        print("The products are NOT sorted correctly.")
    
    # Compare the results of the filtration
    assert prices_after == sorted(prices_after), "The products are not sorted correctly by price."

except Exception as e:
    print(f"Error occurred: {e}")
finally:
    # Close the browser
    time.sleep(2)  # Optional delay to observe
    driver.quit()
    print("Testing completed.")
