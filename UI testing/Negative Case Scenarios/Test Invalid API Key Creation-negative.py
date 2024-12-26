import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Automatically install the correct ChromeDriver version
chromedriver_autoinstaller.install()

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)


def test_create_api_key():
    try:
        print("Starting Test: Create API Key...")

        # Step 1: Open the website and navigate to the API Dashboard
        driver.get("https://app.rentcast.io")
        print("Website opened.")

        # Step 2: Locate and click the "Dashboard" button
        dashboard_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Dashboard']"))
        )
        dashboard_button.click()
        print("Dashboard button clicked.")

        # Step 3: Check if Sign-In is required
        try:
            sign_in_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
            )
            print("Sign-In required. Proceeding to Sign-In...")

            # Click the Sign-In button
            sign_in_button.click()

            # Wait for the Sign-In modal
            sign_in_modal = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "modal-dialog"))
            )

            # Fill in Sign-In credentials
            email_field = wait.until(EC.presence_of_element_located((By.ID, "signInEmail")))
            email_field.send_keys("testuser@example.com")
            password_field = driver.find_element(By.ID, "signInPassword")
            password_field.send_keys("securepassword123")

            # Click the modal Sign-In button
            modal_sign_in_button = driver.find_element(By.XPATH, "//rc-button-spinner")
            modal_sign_in_button.click()
            print("Signed in successfully.")
        except Exception as e:
            print("Sign-In not required or already signed in:", e)

        # Step 4: Wait for the API Dashboard to load
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//h4[contains(text(), 'API Keys')]"))
        )
        print("API Dashboard loaded.")

        # Step 5: Locate and click the "Create API Key" button
        create_api_key_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create API Key')]"))
        )
        driver.execute_script("arguments[0].click();", create_api_key_button)  # Ensure precise click
        print("Create API Key button clicked.")

        # Step 6: Wait for the "New API Key" modal to appear
        new_api_key_modal = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "modal-dialog"))
        )
        print("New API Key modal appeared.")

        # Step 7: Leave required fields empty and click "Create API Key"
        create_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']"))
        )
        create_button.click()
        print("Attempted to create API Key with empty fields.")

        # Step 8: Validate error message
        try:
            error_message = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "validation-message"))
            )
            print("Validation error detected:", error_message.text)
            print("Test Passed: Validation message displayed correctly.")
        except Exception as e:
            print("Validation error not detected. Test Failed:", e)

    finally:
        time.sleep(15)  # Pause to observe the browser before quitting
        driver.quit()


# Run the test
test_create_api_key()
