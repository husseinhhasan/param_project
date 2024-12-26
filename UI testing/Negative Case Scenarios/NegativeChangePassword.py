from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Open the personal account page
    print("Opening the personal account page...")
    driver.get("https://app.rentcast.io/app/account")
    print("Personal account page loaded.")

    # Step 2: Click the "Sign In" button on the page
    print("Clicking the 'Sign In' button on the page...")
    sign_in_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-primary.px-6"))
    )
    sign_in_button.click()
    print("Clicked the 'Sign In' button.")

    # Step 3: Perform the sign-in process
    print("Waiting for the sign-in modal to appear...")
    sign_in_modal = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-dialog"))
    )
    print("Sign-In modal appeared.")

    # Enter email
    email_field = wait.until(EC.presence_of_element_located((By.ID, "signInEmail")))
    email_field.send_keys("aboudqaisi.77@gmail.com")  # Replace with your email
    print("Email field filled.")

    # Enter password
    password_field = driver.find_element(By.ID, "signInPassword")
    password_field.send_keys("Emailpass1")  # Replace with your password
    print("Password field filled.")

    # Click the Sign-In button in the modal
    modal_sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    modal_sign_in_button.click()
    print("Sign-In button clicked in the modal.")

    # Wait for successful sign-in
    print("Waiting for the account page to load after sign-in...")
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "page-header"))
    )
    print("Account page successfully loaded after sign-in!")

    # Step 4: Scroll to the "Change Your Password" section
    print("Scrolling to the 'Change Your Password' section...")
    change_password_section = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.card-header"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", change_password_section)
    print("'Change Your Password' section is now visible.")

    # Step 5: Enter the new password
    print("Entering the new password...")
    new_password_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#accountPassword"))
    )
    new_password_box.send_keys("ValidNewPassword123")  # Replace with a valid new password
    print("New password entered.")

    # Step 6: Enter a short random old password
    print("Entering a short random old password...")
    confirm_password_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#accountPasswordConfirm"))
    )
    confirm_password_box.send_keys("123")  # Short random invalid password
    print("Short random old password entered.")

    # Step 7: Click the "Save Password" button explicitly
    print("Clicking the 'Save Password' button...")
    save_password_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    save_password_button.click()
    print("Clicked the 'Save Password' button.")

    # Step 8: Capture the error message before it disappears
    try:
        error_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Password must be at least 6 characters.')]"))
        )
        print(f"Error message captured: {error_message.text}")
    except Exception:
        print("Error message disappeared before it could be captured.")

    # Step 9: Keep the browser open for observation
    input("Test complete. Observe the browser. Press Enter to close it...")

except Exception as e:
    print(f"An error occurred: {e}")
    input("An error occurred. Press Enter to close the browser manually...")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed.")