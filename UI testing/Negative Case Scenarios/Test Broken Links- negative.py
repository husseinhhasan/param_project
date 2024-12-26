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

def test_broken_links():
    try:
        print("Starting Broken Links Test...")

        # Step 1: Navigate to a non-existent page
        driver.get("https://www.rentcast.io/nonexistent")
        print("Navigated to a non-existent URL.")

        # Step 2: Wait for the page to load and check for 404 or error elements
        try:
            # Look for a 404 message or error page element (Update selector based on actual page design)
            error_message = wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '404') or contains(text(), 'Not Found')]"))
            )
            print("404 error message detected: ", error_message.text)
            print("Broken Links Test Passed!")
        except Exception as e:
            print("Broken Links Test Failed: No 404 or error message detected.", e)

    finally:
        time.sleep(5)  # Give time to observe the result before closing
        driver.quit()

# Run the test
test_broken_links()
