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

# --- Step 2: Enter the first major and extract passing applicants ---

# Get the first major link from the list
first_major_link = driver.find_element(By.CSS_SELECTOR, "table a")
first_major_name = first_major_link.text.strip()
print(f"Entering major: {first_major_name}")
first_major_link.click()
time.sleep(3)

# Debug: find the actual table ID on the page
table_id = driver.execute_script("""
    var tables = $.fn.dataTable.tables();
    return tables.length > 0 ? tables[0].id : 'NOT FOUND';
""")
print(f"DataTable ID found: {table_id}")

# Use JavaScript to tell DataTables to show ALL records at once (-1 = all)
driver.execute_script(f"$('#{table_id}').DataTable().page.len(-1).draw();")
time.sleep(3)

# Debug: print the text of the last column of the first 3 rows
rows = driver.find_elements(By.CSS_SELECTOR, f"#{table_id} tbody tr")
print(f"Total rows visible: {len(rows)}")
for row in rows[:3]:
    cols = row.find_elements(By.TAG_NAME, "td")
    if cols:
        print(f"  Last col text: repr={repr(cols[-1].text)}")

# Collect all passing applicants
all_passed = []
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 6 and "VACANTE" in cols[5].text:
        all_passed.append({
            "Código": cols[0].text.strip(),
            "Apellidos y Nombres": cols[1].text.strip(),
            "Escuela": cols[2].text.strip(),
            "Puntaje": cols[3].text.strip(),
            "Mérito E.P": cols[4].text.strip(),
            "Observación": cols[5].text.strip(),
        })

print(f"Total applicants who passed in '{first_major_name}': {len(all_passed)}")

input("Press Enter to close the browser...")
driver.quit()



