from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Import the time module for adding delays

# Step 1: Launch Chrome browser
driver = webdriver.Chrome()

try:
    # Step 2: Navigate to RentCast homepage
    driver.get("https://app.rentcast.io/app")
    print("Navigated to RentCast homepage.")

    # Step 3: Locate and click the "?" button (question circle)
    question_mark_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "span.icon-wrapper > svg.svg-inline--fa.fa-question-circle"))
    )
    question_mark_button.click()
    print("Clicked the '?' button.")

    # Step 4: Pause for 5 seconds before clicking "Contact Support"
    time.sleep(2)
    print("Waited for 5 seconds.")

    # Step 5: Locate and click "Contact Support" from the dropdown
    contact_support = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Contact Support')]"))
    )
    contact_support.click()
    print("Clicked the 'Contact Support' option.")

    # Step 6: Pause to observe the result
    input("Test complete. Press Enter to close the browser...")

except Exception as e:
    print(f"An error occurred: {e}")
    input("An error occurred. Press Enter to close the browser...")

finally:
    # Step 7: Close the browser
    driver.quit()
    print("Browser closed.")