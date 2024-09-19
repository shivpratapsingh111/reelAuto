import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

os.environ["DISPLAY"] = ":99"

# Path to GeckoDriver
geckodriver_path = "/usr/local/bin/geckodriver"

# Path to your Firefox profile
firefox_profile_path = "/root/.mozilla/firefox/49z3oup8.default-esr"

# Set up Firefox options and service
options = Options()
service = FirefoxService(executable_path=geckodriver_path, log_path="/tmp/geckodriver.log", service_args=["--log", "trace"])

# Load Firefox profile
options.add_argument("-profile")
options.add_argument(firefox_profile_path)
options.add_argument('--headless')

# Initialize the WebDriver
driver = webdriver.Firefox(service=service, options=options)

def wait_random_time(min_seconds=4, max_seconds=30):
    time.sleep(random.uniform(min_seconds, max_seconds))

def download_reel(reel_url):
    # Check if the download tool tab is already open
    if len(driver.window_handles) == 1:
        print("Opening download tool...")
        driver.execute_script("window.open('https://publer.io/tools/instagram-reel-downloader', '_blank');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
    else:
        # Switch to the existing download tool tab
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)

    print("Pasting the URL...")
    time.sleep(2)

    # Wait until the input element is available, then paste the URL
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='url']"))
    )
    input_element.clear()  # Clear any existing text in the input field
    time.sleep(3)
    input_element.send_keys(reel_url)
    time.sleep(1)

    print("Clicking download button...")
    time.sleep(2)
    download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    download_button.click()

    print("Waiting for download to be ready...")
    wait_for_save_button()

    print("Clicking save button...")
    time.sleep(3)
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.is-white.is-outlined"))
    )
    time.sleep(1)
    save_button.click()

    print("Waiting for download to complete...")

    # Switch back to the Instagram tab without closing the download tab
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])

def wait_for_save_button():
    while True:
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.button.is-white.is-outlined"))
            )
            break
        except:
            time.sleep(3)

def main():
    driver.get("https://instagram.com/reels")
    print('Opened browser')

    # Wait for Instagram page to load completely
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
    )

    for i in range(30):
        print(f"Processing reel {i + 1}...")

        # Scroll down to the next reel
        actions = ActionChains(driver)
        actions.send_keys(Keys.DOWN).perform()
        wait_random_time()

        # Get the current reel URL
        reel_url = driver.current_url
        print(f"Found reel URL: {reel_url}")

        # Download the reel
        download_reel(reel_url)

    driver.quit()

if __name__ == "__main__":
    main()
