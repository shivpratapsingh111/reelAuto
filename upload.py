from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


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

# Configurations
downloads_folder = os.path.expanduser("~/Downloads")
log_file_path = os.path.join(downloads_folder, "uploaded_reels.log")
# Initialize the WebDriver
driver = webdriver.Firefox(service=service, options=options)

# Consts
caption_text = """
The BMW M4 Coupe is a high-performance vehicle developed by BMW’s motorsport division, BMW M, and has been in production since 2014. It features a powerful straight six-cylinder engine with a maximum power output of 390 kW at 6,250 rpm.

The M4 Coupe is part of the BMW 4 Series and offers various design variants and special editions, such as the M4 Competition Package, which boosts power output to 331 kW and enhances handling with revised suspension components.

The car is known for its athletic design and dynamic flair, with options for additional sporty equipment like carbon fiber exterior and interior enhancements.

The BMW M4 Coupe comes with different powertrain options, including the M4 CSL with 551 hp and 650 Nm of torque, the M4 Competition Coupe with 510 hp and 650 Nm of torque, and the standard M4 Coupe with 480 hp and 550 Nm of torque. The vehicle offers a combination of rear-wheel drive and a manual 6-speed transmission for a dynamic driving experience.

In terms of dimensions, the M4 Coupe has a height ranging from 1397mm to 1398mm and a width of 1887mm.Overall, the BMW M4 Coupe is a high-performance sports car that combines power, agility, and luxury, making it a desirable choice for enthusiasts seeking a thrilling driving experience.

#reels
#reelsinstagram
#reelsvideo
#reelsitfeelit
#reelsindia
#holareels
#reelsinsta
#instagramreels
#viralvideos
#instareels
#reelsofinstagram
#viralvideos
#reelsvideos
#reelsexplore
#reelsforyou
#reelsviralvideo
#reelsoftheday
#reelslove
#reelsvideo
#reelsindiaofficial
"""


# Set up logging
if not os.path.exists(log_file_path):
    open(log_file_path, 'w').close()

def has_uploaded(video_name):
    with open(log_file_path, 'r') as log_file:
        uploaded_videos = log_file.read().splitlines()
    return video_name in uploaded_videos

def log_uploaded(video_name):
    with open(log_file_path, 'a') as log_file:
        log_file.write(video_name + '\n')


# Open Instagram
driver.get("https://www.instagram.com")

action = ActionChains(driver)

# Loop to upload a single video
uploaded = False
for video_file in os.listdir(downloads_folder):
    if video_file.endswith('.mp4'):
        video_path = os.path.join(downloads_folder, video_file)
        
        # Check if the video has already been uploaded
        if has_uploaded(video_file):
            print(f'Skipping already uploaded video: {video_file}')
            continue

        # Proceed with uploading the video
        try:
            # Wait for the 'New Post' button and click it
            wait = WebDriverWait(driver, 15)
            new_post_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class*='x9f619'] svg[aria-label='New post']")))
            action.click(new_post_button).perform()
            print(f'Clicked new post button for {video_file}')

            # Wait for the file input to be present and upload the file
            file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
            file_input.send_keys(video_path)
            print(f'File uploaded: {video_file}')

            # Wait for the OK button (if present) and click it
            try:
                ok_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._acan._acap._acaq._acas._acav._aj1-._ap30")))
                ok_button.click()
                print('Clicked OK button')
            except Exception as e:
                print(f"No OK button found: {e}")

            # Wait for the next button to be clickable and click it
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.x1f6kntn:nth-child(1)")))
            next_button.click()
            print('Clicked next button main')

            # Wait for the final next button to appear and click it
            final_next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "html._9dls._ar44.js-focus-visible._aa4d.__fb-dark-mode body._ar45.system-fonts--body div.x1n2onr6.xzkaem6 div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.xippug5.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.x71s49j.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6 div.xs83m0k.x1sy10c2.x1h5jrl4.xieb3on.xmn8rco.x1iy3rx.x1n2onr6 div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe div div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div._ap97 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x1qjc9v5.x78zum5.xdt5ytf div._ac76._ar86 div._ac7b._ac7d div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xyamay9.x1pi30zi.x1l90r2v.x1swvt13.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37")))
            final_next_button.click()
            print('Clicked final next button')

            # Wait for the caption box to appear, click it, and paste the caption
            caption_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-placeholder='Write a caption...']")))
            caption_box.click()
            action.send_keys(caption_text).perform()
            print('Pasted Caption')

            # Wait for the 'Share' button and click it
            share_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Share']")))
            share_button.click()
            print('Clicked Share button')
            # Wait for the confirmation message

            def wait_for_confirmation_message(driver, timeout=300):
                """
                Waits for the confirmation message to become visible.
                Repeats the check every 5 seconds until the element is found or timeout is reached.

                :param driver: The Selenium WebDriver instance.
                :param timeout: Maximum time to wait for the element (in seconds).
                """
                end_time = time.time() + timeout
                while time.time() < end_time:
                    try:
                        # Check for the confirmation message
                        confirmation_message = WebDriverWait(driver, 5).until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, "html._9dls._ar44.js-focus-visible._aa4d.__fb-dark-mode body._ar45.system-fonts--body div.x1n2onr6.xzkaem6 div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.xippug5.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.x71s49j.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6 div.xs83m0k.x1sy10c2.x1h5jrl4.xieb3on.xmn8rco.x1iy3rx.x1n2onr6 div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe div div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.xdl72j9.x1iyjqo2.xs83m0k.x15wfb8v.x3aagtl.xqbdwvv.x6ql1ns.x1cwzgcd div.x6s0dn4.x78zum5.x5yr21d.xl56j7k.x1n2onr6.xh8yej3 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x6s0dn4.x1oa3qoh.xl56j7k div div span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.x1ms8i2q.xo1l8bm.x5n08af.x2b8uid.x4zkp8e.xw06pyt.x10wh9bi.x1wdrske.x8viiok.x18hxmgj")))
                        print('Confirmation message found:', confirmation_message.text)
                        return confirmation_message

                    except Exception:
                        print(f'Element not found yet. Checking again in 5 seconds...:')
                        time.sleep(5)

                print("Timeout reached. Confirmation message not found.")
                return None

            try:
                # time.sleep(180)
                confirmation_message = wait_for_confirmation_message(driver)

                print('Confirmation message found')

                # Wait for 3 seconds before exiting
                # Log the uploaded video
                log_uploaded(video_file)
                print(f'Logged uploaded video: {video_file}')

                # Delete the video file after successful upload
                os.remove(video_path)
                print(f'Deleted video file: {video_file}')

                # Set uploaded flag and exit the loop
                uploaded = True
                time.sleep(3)
                break

            except Exception as e:
                print(f'Error waiting for confirmation message: {e}')


        except Exception as e:
            print(f'Error uploading {video_file}: {e}')
            continue

# Exit if no videos were uploaded
if not uploaded:
    print('No valid videos to upload. Exiting.')

# Close the driver
driver.quit()


