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

    # Step 3: Locate and click the avatar icon to open the Sign-In modal
    avatar_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.avatar-soft-dark"))
    )
    avatar_icon.click()
    print("Clicked the avatar icon to open the Sign In modal.")

    # Step 4: Wait for the Sign-In modal to appear
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "display-4"))
    )
    print("Sign In modal is now visible.")

    # Step 5: Locate the Sign-In button and click it without filling any fields
    try:
        # Use WebDriverWait to ensure button visibility
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//rc-button-spinner"))
        )
        sign_in_button.click()
        print("Sign-In button clicked with empty fields.")
    except Exception as e:
        print("Normal click failed. Attempting JavaScript click...")
        # Use JavaScript Executor as fallback
        sign_in_button = driver.find_element(By.XPATH, "//rc-button-spinner")
        driver.execute_script("arguments[0].click();", sign_in_button)
        print("Sign-In button clicked using JavaScript.")

    # Step 6: Verify error messages or login failure
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'required') or contains(text(), 'Invalid')]"))
    )
    print(f"Error message displayed: {error_message.text}")

    # Step 7: Pause to observe the result
    input("Test complete: Empty fields prevented sign-in. Press Enter to close the browser...")

except Exception as e:
    print(f"An error occurred: {e}")
    input("An error occurred. Press Enter to close the browser...")

finally:
    # Step 8: Close the browser
    driver.quit()
    print("Browser closed.")