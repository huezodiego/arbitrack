from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

DRIVER_PATH = "../drivers/chromedriver-mac-arm64/chromedriver"
service = Service(executable_path=DRIVER_PATH)

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.oddstrader.com')
participant_containers = driver.find_element(By.CLASS_NAME, "participant")
#name_containers = driver.find_element(By.XPATH, '/html/body/div/oddsGridRowContainer oddContainer lastOddContainer')
print(participant_containers.text)
driver.quit()

