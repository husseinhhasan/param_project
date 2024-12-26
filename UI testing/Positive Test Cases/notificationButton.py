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

    # Locate and click the notification bell icon
    print("Starting Notification Button Click Test...")
    notification_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-icon='bell']"))
    )
    notification_icon.click()
    print("Clicked the notification bell icon.")

finally:
    time.sleep(5)  # Give time to observe the result before closing
    driver.quit()
