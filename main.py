from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def typing_race(type_interval: float):
    # Create WebDriver instance
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, timeout=25)

    try:
        # Navigate to the main page
        driver.get("https://play.typeracer.com/")

        # Disagree to cookies
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'DISAGREE')]"))).click()

        # Enter a typing race
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Enter a Typing Race')]"))).click()

        # Wait until time remaining element is visible
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@title='Time remaining']")))

        # Read typing text
        text_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@unselectable='on']")))
        race_text = race_text = ''.join(i.text for i in text_elements[:-1]) + " " + text_elements[-1].text

        # Find input field
        input_field = driver.find_element(By.XPATH, "//input[@class='txtInput']")

        # Type the text with specified interval
        for char in race_text: 
            input_field.send_keys(char)
            sleep(type_interval)
    
    finally:
        # Ensure WebDriver instance is closed
        driver.quit()

# Call the function with specified typing interval
typing_race(0.08)
