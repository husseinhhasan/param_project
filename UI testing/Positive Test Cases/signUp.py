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

def test_sign_up():
    print("Starting Sign-Up Test...")
    driver.get("https://app.rentcast.io")  # Replace with the actual URL

    # Step 1: Click the avatar icon or dropdown to trigger the menu
    avatar_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.avatar-soft-dark"))
    )
    avatar_icon.click()
    print("Clicked the avatar icon to open the dropdown menu.")

    # Step 2: Click the "Sign up for free" button
    sign_up_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'btn-link') and contains(text(), 'Sign up for free')]"))
    )
    sign_up_button.click()
    print("Clicked 'Sign up for free' button to open the Sign-Up modal.")

    # Step 3: Wait for the modal to appear
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-dialog")))

    # Step 4: Fill in the Name field
    name_field = wait.until(EC.presence_of_element_located((By.ID, "signUpFullName")))
    name_field.send_keys("Test User")
    print("Name field filled.")

    # Step 5: Fill in the Email field
    email_field = driver.find_element(By.ID, "signUpEmail")
    email_field.send_keys("testuserrr@example.com")
    print("Email field filled.")

    # Step 6: Fill in the Password field
    password_field = driver.find_element(By.ID, "signUpPassword")
    password_field.send_keys("securepassword123")
    print("Password field filled.")

    # Step 7: Click the Create Account button
    create_account_button = driver.find_element(By.XPATH, "//rc-button-spinner")
    create_account_button.click()
    print("Create Account button clicked.")

    # Step 8: Validate success message
    try:
        success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "success-message")))
        assert "success" in success_message.text.lower(), "Sign-Up Test Failed!"
        print("Sign-Up Test Passed!")
    except Exception as e:
        print("Sign-Up Test Failed: Success message not found.", e)

try:
    test_sign_up()
finally:
    time.sleep(5)
    driver.quit()
