from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def typing_race(type_interval: float, error_probability=0):
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
        race_text = ''.join(i.text for i in text_elements[:-1]) + " " + text_elements[-1].text

        # Find input field
        input_field = driver.find_element(By.XPATH, "//input[@class='txtInput']")

        # Type the text with specified interval and error_rate
        error_counter, i = 0, 0
        while i < len(race_text):
            if random.random() < error_probability:
                input_field.send_keys(chr(ord(race_text[i])+1))
                error_counter += 1
            elif error_counter > 0:
                input_field.send_keys(Keys.BACK_SPACE)
                error_counter -= 1
            else:
                input_field.send_keys(race_text[i])
                i += 1
            sleep(type_interval)


    finally:
        # Ensure WebDriver instance is closed
        sleep(20)
        driver.quit()

# Call the function with specified typing interval ~ 100 wpm
typing_race(type_interval=0.08, error_probability=0.1)
