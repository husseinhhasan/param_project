from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Launch Chrome browser
driver = webdriver.Chrome()

try:
    # Step 2: Navigate to RentCast homepage
    driver.get("https://app.rentcast.io/app")
    print("Navigated to RentCast homepage.")

    # Step 3: Locate and click the Search Box
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search by property address']"))
    )
    search_box.click()
    print("Clicked the search box.")

    # Step 4: Enter the address into the Search Box
    search_box.send_keys("Alabama State Route 3, Bay Minette, AL, 36507")
    print("Entered the address into the search box.")

    # Step 5: Locate and click the Search button
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-block.btn-primary"))
    )
    search_button.click()
    print("Clicked the Search button.")

    # Step 6: Verify the URL contains the expected query
    WebDriverWait(driver, 10).until(
        EC.url_contains("address=Alabama%20State%20Rte,%20&type=single-family")
    )
    print("Search successfully performed. Redirected to the correct results page.")

    # Step 7: Pause to observe the result
    input("Test complete. Press Enter to close the browser...")

except Exception as e:
    print(f"An error occurred: {e}")
    input("An error occurred. Press Enter to close the browser...")

finally:
    # Step 8: Close the browser
    driver.quit()
    print("Browser closed.")