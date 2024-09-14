from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, argparse

parser = argparse.ArgumentParser(usage='Usage:\n%(prog)s [arguments]')
parser.add_argument('-v', '--video')
args = parser.parse_args()

# ---

# Configurations
geckodriver_path = "/usr/local/bin/geckodriver"
firefox_profile_path = "/home/cyrusop/.mozilla/firefox/5m1hacmd.reelAutomate"
file_to_upload = args.video  # Update this path to your file

# ---

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

# ---

# Set up Firefox options and service
options = Options()
service = FirefoxService(executable_path=geckodriver_path)
# Load Firefox profile
profile = FirefoxProfile(firefox_profile_path)
options.profile = profile
# Initialize the WebDriver
driver = webdriver.Firefox(service=service, options=options)

# Open Instagram
driver.get("https://www.instagram.com")

action = ActionChains(driver)

# ---

# Wait for the 'New Post' button and click it
wait = WebDriverWait(driver, 15)
new_post_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class*='x9f619'] svg[aria-label='New post']")))
action.click(new_post_button).perform()
print('Clicked new post button')

# Wait for the file input to be present and upload the file
file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
file_input.send_keys(file_to_upload)
print('File uploaded')

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
print('Clicked next button')

# Wait for the caption box to appear, click it, and paste the caption
caption_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-placeholder='Write a caption...']")))
caption_box.click()
action.send_keys(caption_text).perform()
print('Pasted Caption')

# Wait for the 'Share' button and click it
share_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Share']")))
share_button.click()
print('Clicked Share button')
