from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a WebDriver instance
driver = webdriver.Chrome()

# Navigate to a web page
driver.get("https://example.com")

# Define a timeout for the explicit wait (e.g., 10 seconds)
wait = WebDriverWait(driver, 10)
try:
    # Wait for a specific element to be visible and clickable
    element = wait.until(EC.element_to_be_clickable((By.ID, "example_id")))

    # Perform actions on the element
    element.click()

    # You can also wait for the page title to change
    wait.until(EC.title_contains("New Page Title"))
finally:

# Close the WebDriver
  driver.quit()