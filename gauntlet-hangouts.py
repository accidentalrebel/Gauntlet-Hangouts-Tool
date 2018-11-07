from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

EVENTS_URL = 'https://gauntlet-hangouts.firebaseapp.com/events'
EVENTS_INFO_URL = "https://gauntlet-hangouts.firebaseapp.com/all-events-info"

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)

class element_has_css_class():
    def __init__(self, locator, css_class):
        self.locator = locator
        self.css_class = css_class

    def __call__(self, driver):
        elements = lambda: driver.find_elements_by_tag_name(self.css_class)
        print('ELEMENTS COUNT IS ' + str(len(elements())))
        if len(elements()) > 1:
            return elements()

        return False

def load_events():
    driver.get(EVENTS_URL)
    wait = WebDriverWait(driver, 60)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'event')))

    elements = driver.find_elements_by_class_name('event')
    for element in elements:
        print(str(element.get_attribute('outerHTML')))

def load_events_info():
    driver.get(EVENTS_INFO_URL)
    wait = WebDriverWait(driver, 60)

    # element = driver.find_element_by_tag_name('datatable-body')
    # driver.execute_script("arguments[0].setAttribute('style','height: 99999px')", element)

    driver.find_element_by_class_name('btn-black').click()

    elements = wait.until(element_has_css_class((By.TAG_NAME, 'tr'), "tr"))
    sleep(5) # This is needed to avoid getting a stale 'tr' with the next line of code

    elements = driver.find_elements_by_tag_name('tr')
    for element in elements:
        #print(element.text)
        print(str(element.get_attribute('innerHTML')))

load_events_info()
