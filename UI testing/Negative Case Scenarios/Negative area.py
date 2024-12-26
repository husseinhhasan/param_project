from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Launch Chrome browser
driver = webdriver.Chrome()

try:
    # Step 2: Navigate to RentCast homepage
    driver.get("https://app.rentcast.io/app")
    print("Navigated to RentCast homepage.")

    # Step 3: Locate and click the Search Box
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search by property address']"))
    )
    search_box.click()
    print("Clicked the search box.")

    # Step 4: Enter the address into the Search Box
    search_box.send_keys("Calibre St, Fairhope, AL, 36532")
    print("Entered the address into the search box.")

    # Step 5: Locate and input a negative value into the Square Feet input box
    square_feet_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Living area size']"))
    )
    square_feet_box.click()
    square_feet_box.send_keys("-500")
    print("Entered a negative value in the square feet box.")

    # Step 6: Locate and click the Search button
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-block.btn-primary"))
    )
    search_button.click()
    print("Clicked the Search button.")

    # Step 7: Log behavior
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'invalid value')]"))  # Adjust XPath if needed
        )
        print(f"Error message displayed: {error_message.text}")
    except Exception:
        print("No error message displayed. Check page behavior for negative square feet input.")

    # Step 8: Pause to observe the result
    input("Test complete. Press Enter to close the browser...")

except Exception as e:
    print(f"An error occurred: {e}")
    input("An error occurred. Press Enter to close the browser...")

finally:
    # Step 9: Close the browser
    driver.quit()
    print("Browser closed.")