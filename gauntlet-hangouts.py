import json
import dateparser
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

EVENTS_URL = 'https://gauntlet-hangouts.firebaseapp.com/events'
EVENTS_INFO_URL = "https://gauntlet-hangouts.firebaseapp.com/all-events-info"
HEADER_TITLES = ['title', 'creator', 'start_time', 'all_access_time', 'rsvp_percent', 'max_users_count', 'rsvp_count', 'waitlist_count']

EVENTS_COUNT_LIMIT = 10

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
    sleep(3)
    print('Sleeping for a bit...\n')

    events = []
    tr_elements = driver.find_elements_by_tag_name('tr')

    events_count = 0
    for tr_element in tr_elements:
        if events_count > EVENTS_COUNT_LIMIT:
            break
        
        #print(element.text)
        td_elements = tr_element.find_elements_by_tag_name('td')

        event = {}        
        index = 0
        for td_element in td_elements:
            header = HEADER_TITLES[index]
            #print(header + ': ' + td_element.text)
            event[header] = td_element.text
            index = index + 1

        events.append(event)
        events_count = events_count + 1

    # Still a test
    # tr_element = tr_elements[5]
    # actions = ActionChains(driver)
    # actions.move_to_element(tr_element)
    # actions.click(tr_element)
    # actions.perform()
    # sleep(30)
    # end test
    
    print('-- Process Complete --')
    return events

def parse_date(date_string):
    date_string = date_string.replace(' pm', '')
    date_string = date_string.replace(' am', '')
    return dateparser.parse(date_string)

def filter_by_time(events):
    for event in events:
        print(str(event))

current_date = datetime.now()
parsed_date = parse_date('Friday, October 26, 2018, 20:00 pm')
if current_date.hour > parsed_date.hour:
    print('passed')
else:
    print('not passed')

print('Current: ' + str(current_date))    
print('Parsed: ' + str(parsed_date))


# events_info = load_events_info()
# filter_by_time(events_info)
