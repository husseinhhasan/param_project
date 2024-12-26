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
wait = WebDriverWait(driver, 10)

try:
    print("Opening the website...")
    driver.get("https://app.rentcast.io")  # Replace with the actual URL

    # Step 1: Locate and click the "API Dashboard" button
    print("Clicking the 'API Dashboard' button...")
    api_dashboard_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Dashboard']"))
    )
    api_dashboard_button.click()
    print("Clicked the 'API Dashboard' button.")

    # Step 2: Locate and click the "Sign In" button
    print("Clicking the 'Sign In' button...")
    sign_in_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
    )
    sign_in_button.click()
    print("Clicked the 'Sign In' button.")

    # Step 3: Wait for the Sign-In modal to appear
    print("Waiting for the Sign-In modal to appear...")
    sign_in_modal = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal-dialog"))
    )
    print("Sign-In modal appeared.")

    # Step 4: Fill in the Email field
    email_field = wait.until(EC.presence_of_element_located((By.ID, "signInEmail")))
    email_field.send_keys("testuser@example.com")
    print("Email field filled.")

    # Step 5: Fill in the Password field
    password_field = driver.find_element(By.ID, "signInPassword")
    password_field.send_keys("securepassword123")
    print("Password field filled.")

    # Step 6: Click the Sign-In button in the modal
    modal_sign_in_button = driver.find_element(By.XPATH, "//rc-button-spinner")
    modal_sign_in_button.click()
    print("Sign-In button clicked in the modal.")

    # Step 7: Validate successful login
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "dashboard-container"))
    )
    print("Sign-In Test Passed! Navigated to API Dashboard.")

finally:
    time.sleep(5)  # Give time to observe the result before closing
    driver.quit()
