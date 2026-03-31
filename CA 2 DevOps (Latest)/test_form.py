from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import time
import os

# ---------- Setup Chrome Driver ----------
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

# ---------- Open HTML File ----------
file_path = os.path.abspath("index.html")
driver.get("file:///" + file_path.replace("\\", "/"))
driver.maximize_window()

# ---------- Test Case 1: Page Opens Successfully ----------
print("Test Case 1: Checking page load...")
assert "Student Feedback Form" in driver.page_source
print("PASS: Form page opened successfully")

# ---------- Test Case 2: Valid Submission ----------
print("\nTest Case 2: Valid submission...")

driver.find_element(By.ID, "name").send_keys("John Doe")
driver.find_element(By.ID, "email").send_keys("john@gmail.com")
driver.find_element(By.ID, "mobile").send_keys("9876543210")

dropdown = Select(driver.find_element(By.ID, "department"))
dropdown.select_by_visible_text("Computer")

driver.find_element(By.XPATH, "//input[@value='Male']").click()

driver.find_element(By.ID, "comments").send_keys(
    "This feedback form is simple and easy to use for all students"
)

driver.find_element(By.XPATH, "//button[text()='Submit']").click()

time.sleep(2)

try:
    alert = Alert(driver)
    print("PASS: Valid form submitted successfully")
    alert.accept()
except:
    print("FAIL: Alert not shown")

# ---------- Test Case 3: Blank Mandatory Fields ----------
print("\nTest Case 3: Mandatory field validation...")

driver.refresh()
time.sleep(1)

driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(1)

error_text = driver.find_element(By.ID, "error").text
print("Validation Message:", error_text)

# ---------- Test Case 4: Invalid Email ----------
print("\nTest Case 4: Invalid email validation...")

driver.refresh()
time.sleep(1)

driver.find_element(By.ID, "name").send_keys("John")
driver.find_element(By.ID, "email").send_keys("john.com")
driver.find_element(By.XPATH, "//button[text()='Submit']").click()

time.sleep(1)

error_text = driver.find_element(By.ID, "error").text
print("Validation Message:", error_text)

# ---------- Test Case 5: Invalid Mobile ----------
print("\nTest Case 5: Invalid mobile validation...")

driver.refresh()
time.sleep(1)

driver.find_element(By.ID, "name").send_keys("John")
driver.find_element(By.ID, "email").send_keys("john@gmail.com")
driver.find_element(By.ID, "mobile").send_keys("1234")

driver.find_element(By.XPATH, "//button[text()='Submit']").click()

time.sleep(1)

error_text = driver.find_element(By.ID, "error").text
print("Validation Message:", error_text)

# ---------- Test Case 6: Dropdown Check ----------
print("\nTest Case 6: Dropdown selection...")

driver.refresh()
time.sleep(1)

dropdown = Select(driver.find_element(By.ID, "department"))
dropdown.select_by_visible_text("IT")

selected = dropdown.first_selected_option.text
print("Selected Department:", selected)

# ---------- Test Case 7: Reset Button ----------
print("\nTest Case 7: Reset button...")

driver.find_element(By.ID, "name").send_keys("Reset Test")
driver.find_element(By.XPATH, "//button[text()='Reset']").click()

time.sleep(1)

name_value = driver.find_element(By.ID, "name").get_attribute("value")

if name_value == "":
    print("PASS: Reset button working")
else:
    print("FAIL: Reset button not working")

# ---------- Close Browser ----------
print("\nAll test cases executed successfully")
time.sleep(2)
driver.quit()