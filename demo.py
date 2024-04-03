from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Webdriver and WebDriverWait
driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=25)

# Navigate to the webpage
driver.get("https://play.typeracer.com/")

# Click the disagree cookies button
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'DISAGREE')]"))).click()

# Click the "Enter a Typing Race" button
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Enter a Typing Race')]"))).click()

# Wait until the time "remainig element" is visible 
wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@title='Time remaining']"))) 

# Find the elements containing the text to type
text_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@unselectable='on']")))

# Merge the text of the elements to a single string
race_text = race_text = ''.join(i.text for i in text_elements[:-1]) + " " + text_elements[-1].text

# Find input field
input_field = driver.find_element(By.XPATH, "//input[@class='txtInput']")

# Type the text 
for char in race_text: 
    input_field.send_keys(char)
