from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time, random

def run():
    link = 'https://mining.freebitco.in/mining.html?userid=5503720&auth=fa47e70dc1292abbe296da2cf67366e1ddcaafbcd8fbbbc7b5b0d5e0f118f160'

    chrome = webdriver.Chrome('chromedriver.exe')
    chrome.get(link)

    actions = ActionChains(chrome)
    actions.send_keys(Keys.END).perform()
    time.sleep(2)
    chrome.find_element_by_id('start_mining_button').click()
    time.sleep(2)
    actions.send_keys(Keys.TAB).send_keys(Keys.RETURN).perform()
    input('press any key')




