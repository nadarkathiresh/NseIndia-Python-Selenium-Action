import json
import time

import chromedriver_autoinstaller
import requests
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from requests_toolbelt.utils import dump

display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

driver.get('https://nseindia.com')
print(driver.title)

seconds = time.time()
local_time = time.ctime(seconds)

with open('./GitHub_Action_Results.txt', 'w') as f:
    f.write(f"This was written with a GitHub action at {local_time} {driver.title}")
nse_cookies = driver.get_cookies()
print(nse_cookies)
json_data = json.dumps(nse_cookies)

response = requests.post('https://webhook.site/9d4aecc3-2195-432e-89e2-8336a578b145',
                         json=json_data, timeout=5)

# response = requests.post('https://delrique.issosolutions.com/nse_cookie.php',
#                          json=json_data, timeout=5)

data = dump.dump_all(response)

print(f"Text: {response.text}")
print(f"Status Code: {response.status_code}")
