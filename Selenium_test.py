from selenium import webdriver
import time
driver = webdriver.Chrome(
    '/Users/MWalzenbach/Documents/chromedriver/chromedriver.exe')
driver.get('https://www.msn.com/')
messageField = driver.find_element_by_xpath(
    '//*[@id="q"]')
messageField.send_keys('Inspirational Quotes')
showMessageButton = driver.find_element_by_xpath(
    '//*[@id="sb_form_go"]')
showMessageButton.click()
time.sleep(10)
