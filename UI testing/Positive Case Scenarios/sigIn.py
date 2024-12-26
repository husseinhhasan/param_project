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

def test_sign_in():
    print("Starting Sign-In Test...")
    driver.get("https://app.rentcast.io")  # Replace with the actual URL

    # Step 1: Locate and click the avatar icon to trigger the Sign-In modal
    avatar_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.avatar-soft-dark"))
    )
    avatar_icon.click()
    print("Clicked the avatar icon to open the Sign-In modal.")

    # Step 2: Wait for the Sign-In modal to appear
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-dialog")))

    # Step 3: Fill in the Email field
    email_field = wait.until(EC.presence_of_element_located((By.ID, "signInEmail")))
    email_field.send_keys("testuser@example.com")
    print("Email field filled.")

    # Step 4: Fill in the Password field
    password_field = driver.find_element(By.ID, "signInPassword")
    password_field.send_keys("securepassword123")
    print("Password field filled.")

    # Step 5: Click the Sign-In button
    sign_in_button = driver.find_element(By.XPATH, "//rc-button-spinner")
    sign_in_button.click()
    print("Sign-In button clicked.")

    # Step 6: Validate successful login
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dashboard-container")))
        print("Sign-In Test Passed!")
    except Exception as e:
        print("Sign-In Test Failed: Dashboard not found.", e)

try:
    test_sign_in()
finally:
    time.sleep(5)
    driver.quit()
