from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Replace "https://www.example.com" with the actual URL of the website
driver = webdriver.Chrome()
driver.get("https://jobs.ashbyhq.com/ramp?departmentId=e9877d64-61b1-4b37-8518-65af0431cd09&employmentType=Intern")

# Find the dropdown element by its name or other suitable locator
dropdown_element = driver.find_element(By.NAME, "departmentId")

# Create a Select object to interact with the dropdown
select = Select(dropdown_element)

# Select the "Engineering" option by its value
select.select_by_value("e9877d64-61b1-4b37-8518-65af0431cd09")

# Submit the form (if needed)
select.send_keys(keys.RETURN)

submit_button.click()