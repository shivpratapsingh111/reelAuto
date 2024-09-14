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

# Path to GeckoDriver
geckodriver_path = "/usr/local/bin/geckodriver"

# Path to your Firefox profile
firefox_profile_path = "/home/cyrusop/.mozilla/firefox/5m1hacmd.reelAutomate"

# Set up Firefox options and service
options = Options()
service = FirefoxService(executable_path=geckodriver_path)

# Load Firefox profile
profile = FirefoxProfile(firefox_profile_path)
options.profile = profile

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

    # Wait until the input element is available, then paste the URL
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='url']"))
    )
    input_element.clear()  # Clear any existing text in the input field
    input_element.send_keys(reel_url)
    time.sleep(1)

    print("Clicking download button...")
    download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    download_button.click()

    print("Waiting for download to be ready...")
    wait_for_save_button()

    print("Clicking save button...")
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.is-white.is-outlined"))
    )
    save_button.click()

    print("Waiting for download to complete...")

    # Switch back to the Instagram tab without closing the download tab
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
