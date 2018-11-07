from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

EVENTS_URL = 'https://gauntlet-hangouts.firebaseapp.com/events'
EVENTS_INFO_URL = "https://gauntlet-hangouts.firebaseapp.com/all-events-info"

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

class HasLoadedAllEntries():
    def __call__(self, driver):
        elements = driver.find_elements_by_tag_name('tr')
        if len(elements) > 1:
            return True

        return False

def load_events():
    driver.get(EVENTS_URL)
    wait = WebDriverWait(driver, 60)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'event')))

    elements = driver.find_elements_by_class_name('event')
    for element in elements:
        print(str(element.get_attribute('outerHTML')))

def load_events_info():
    print('Loading the page ' + EVENTS_INFO_URL + '...')
    driver.get(EVENTS_INFO_URL)

    # Click on the button "Excel Table" button
    driver.find_element_by_class_name('btn-black').click()
    print('Switched to Excel Table')

    print('Waiting for all entries to be loaded...')
    wait = WebDriverWait(driver, 60)
    wait.until(HasLoadedAllEntries())
    print('All entries loaded!')

    # This is needed to avoid getting a stale 'tr' with the next line of code
    sleep(1)
    print('Sleeping for a bit...\n')

    elements = driver.find_elements_by_tag_name('tr')
    for element in elements:
        #print(element.text)
        print(str(element.get_attribute('innerHTML')))

load_events_info()
