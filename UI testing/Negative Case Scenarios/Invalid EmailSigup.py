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

def test_invalid_email_format():
    print("Starting Invalid Email Format Test...")
    driver.get("https://app.rentcast.io")  # Replace with the actual URL

    # Step 1: Locate and click the avatar icon to trigger the dropdown
    avatar_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.avatar-soft-dark"))
    )
    avatar_icon.click()
    print("Clicked the avatar icon to open the dropdown menu.")

    # Step 2: Click the "Sign up for free" button to open the Sign-Up modal
    sign_up_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'btn-link') and contains(text(), 'Sign up for free')]"))
    )
    sign_up_button.click()
    print("Clicked 'Sign up for free' button to open the Sign-Up modal.")

    # Step 3: Wait for the modal to appear
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-dialog")))
    print("Sign-Up modal is visible.")

    # Step 4: Fill in fields with an invalid email
    name_field = wait.until(EC.presence_of_element_located((By.ID, "signUpFullName")))
    name_field.send_keys("Test User")
    print("Name field filled.")

    email_field = driver.find_element(By.ID, "signUpEmail")
    email_field.send_keys("abood@1234565")  # Invalid email format
    print("Invalid email entered: 'invalid-email'")

    password_field = driver.find_element(By.ID, "signUpPassword")
    password_field.send_keys("securepassword123")
    print("Password field filled.")

    # Step 5: Click the Create Account button
    create_account_button = driver.find_element(By.XPATH, "//rc-button-spinner")
    create_account_button.click()
    print("Clicked the Create Account button.")

    # Step 6: Validate error message for invalid email
    try:
        email_error = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Please enter a valid email address')]"))
        )
        print("Error message displayed for invalid email:", email_error.text)
        print("Invalid Email Format Test Passed!")
    except Exception as e:
        print("Invalid Email Format Test Failed: Error message not displayed.", e)

try:
    test_invalid_email_format()
finally:
    time.sleep(5)  # Observe the result
    driver.quit()