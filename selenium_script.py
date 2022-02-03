from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
import time
import os
load_dotenv()

PATH_TO_DRIVER = os.getenv('PATH_TO_FIREFOX_DRIVER')
OUTPUT_DIR = os.getenv('PATH_TO_OUTPUT_DIR')
INDEX_HTML = os.getenv('PATH_TO_INDEX_HTML')

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", OUTPUT_DIR)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")

options = Options()
options.headless = True

driver = webdriver.Firefox(executable_path=PATH_TO_DRIVER, firefox_profile=profile, options=options)

# load the webpage
driver.get(INDEX_HTML)

# wait for page to load
try:
  WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'url')))
except:
  driver.quit()

# load links from file
linksFile = open('links.txt', 'r')
links = linksFile.read().splitlines()
links = [link.rstrip('/') for link in links]

# loop through links one at a time and download
for link in links:
  # load the link
  input_field = driver.find_element(By.ID, 'url')
  input_field.clear()
  input_field.send_keys(link)

  # click the export button
  export_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
  export_button.click()

  # wait for export to finish
  time.sleep(5)

  # download the md file
  download_button = driver.find_element(By.CLASS_NAME, 'btn-success')
  download_button.click()

driver.quit()