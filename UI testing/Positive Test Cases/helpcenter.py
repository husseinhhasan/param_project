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

    # Step 1: Locate and click the "Question Circle" button
    print("Clicking the 'Question Circle' button...")
    question_circle_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-icon='question-circle']"))
    )
    question_circle_button.click()
    print("Clicked the 'Question Circle' button.")

    # Step 2: Locate and click the "Help Center" button
    print("Clicking the 'Help Center' button...")
    help_center_button = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Help Center"))
    )
    help_center_button.click()
    print("Clicked the 'Help Center' button.")

finally:
    time.sleep(30)  # Give time to observe the result before closing
    driver.quit()
