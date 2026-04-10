from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

URL = "https://admision.unmsm.edu.pe/Website20262/A/A.html"

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--headless")  # uncomment to run without opening a window

driver = webdriver.Chrome(
    service=Service("/usr/bin/chromedriver"),
    options=options,
)

driver.maximize_window()
driver.get(URL)
time.sleep(3)

print("Page title:", driver.title)
print("Browser opened successfully.")

input("Press Enter to close the browser...")
driver.quit()


