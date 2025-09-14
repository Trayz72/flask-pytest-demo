from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def test_google_search():
    # Setup Chrome with visible browser
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Open Google
    driver.get("https://www.google.com")

    # Find the search box and type a query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Automated Testing with Selenium")
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(3)

    # Print the page title (for explanation/demo)
    print("Page Title:", driver.title)

    # Close the browser
    driver.quit()
