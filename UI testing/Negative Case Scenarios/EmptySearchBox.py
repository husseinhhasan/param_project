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

    # Step 3: Locate the Search Box and click it (leave it empty)
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search by property address']"))
    )
    search_box.click()
    print("Clicked the search box (left empty).")

    # Step 4: Locate and click the Search button
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-block.btn-primary"))
    )
    search_button.click()
    print("Clicked the Search button.")

    # Step 5: Observe the result
    print("Observing behavior for an empty search field...")
    WebDriverWait(driver, 5)  # Adjust timeout as needed
    input("Press Enter after observing the result to close the browser...")

except Exception as e:
    print(f"An error occurred: {e}")
    input("An error occurred. Press Enter to close the browser...")

finally:
    # Step 6: Close the browser
    driver.quit()
    print("Browser closed.")