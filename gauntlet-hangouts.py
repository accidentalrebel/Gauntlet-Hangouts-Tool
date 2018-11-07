from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

EVENTS_URL = 'https://gauntlet-hangouts.firebaseapp.com/events'
EVENTS_INFO_URL = "https://gauntlet-hangouts.firebaseapp.com/all-events-info"
HEADER_TITLES = ['Title', 'Event Creator', 'Start Time', 'All Access Time', 'Percent RSVP', 'Max Users', 'RSVPs', 'Waitlist']

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

    tr_elements = driver.find_elements_by_tag_name('tr')
    for tr_element in tr_elements:
        #print(element.text)
        td_elements = tr_element.find_elements_by_tag_name('td')

        index = 0

        for td_element in td_elements:
            header = HEADER_TITLES[index]
            print(header + ': ' + td_element.text)
            
            index = index + 1

        print('')

    print('-- Process Complete --')
            
load_events_info()
