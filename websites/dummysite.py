from selenium import webdriver
from selenium.webdriver.chrome.service import Service
"""
Credit: https://www.scrapingbee.com/blog/selenium-python/ 
Issues with opening chromedriver (macOS Malicious Software Alert)?
https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de
"""

DRIVER_PATH = "../drivers/chromedriver-mac-arm64/chromedriver"
service = Service(executable_path=DRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://google.com')

driver.quit()

