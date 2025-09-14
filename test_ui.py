from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_homepage():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open your Flask app
    driver.get("http://127.0.0.1:5000")

    # Wait for the page
    time.sleep(2)

    # Grab the body text
    body_text = driver.find_element(By.TAG_NAME, "body").text
    print("Page says:", body_text)

    # Validate it
    assert "Automated Software Testing" in body_text

    driver.quit()
