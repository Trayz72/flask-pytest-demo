import time
import tempfile
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_homepage():
    options = webdriver.ChromeOptions()
    
    # Essential options for Jenkins/headless environment
    options.add_argument("--headless")  # Required for Jenkins
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    # Security and automation detection options
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    
    # Use unique temp directory to avoid conflicts
    unique_profile = f"/tmp/chrome-profile-{uuid.uuid4()}"
    options.add_argument(f"--user-data-dir={unique_profile}")
    
    # Additional stability options
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-images")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Try localhost first, then 127.0.0.1 as fallback
        driver.get("http://localhost:5000")
        time.sleep(5)  # Increased wait time for Flask to be ready

        # Check if page loaded successfully
        assert "Automated" in driver.page_source, f"Expected 'Automated' in page source, but got: {driver.page_source[:500]}"
        
        print("UI test passed successfully!")
        
    except Exception as e:
        print(f"UI test failed with error: {e}")
        print(f"Page source: {driver.page_source[:500]}")
        raise
    finally:
        driver.quit()