import praw
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

from dotenv import load_dotenv
load_dotenv()

# env vars
CLIENT_ID= os.getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET= os.getenv('REDDIT_CLIENT_SECRET')
USERNAME= os.getenv('REDDIT_USERNAME')
PASSWORD= os.getenv('REDDIT_PASSWORD')
PATH_TO_DRIVER = os.getenv('PATH_TO_FIREFOX_DRIVER')
INDEX_HTML = os.getenv('PATH_TO_INDEX_FILE')
REDDIT_UTL = 'https://www.reddit.com'

# praw instance
reddit = praw.Reddit(
  client_id=CLIENT_ID,
  client_secret=CLIENT_SECRET,
  user_agent='Saved posts scraper by /u/' + USERNAME,
  username=USERNAME,
  password=PASSWORD
)

# get all saved content
saved_content = reddit.user.me().saved(limit=None)

# define firefox profile
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")

# run in headless mode
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

# loop through each and save
for saved in saved_content:
  # TODO remove if not needed # subreddit = saved.subreddit.display_name
  url = REDDIT_UTL + saved.permalink

  # load the url
  input_field = driver.find_element(By.ID, 'url')
  input_field.clear()
  input_field.send_keys(url)

  # click the export button
  export_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
  export_button.click()

  # wait for export to finish
  time.sleep(5)

  # download the md file
  download_button = driver.find_element(By.CLASS_NAME, 'btn-success')
  download_button.click()

  # unsave the post after downloaded
  saved.unsave()

driver.quit()