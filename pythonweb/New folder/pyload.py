from selenium import webdriver
from bs4 import BeautifulSoup


edgeDriver= ".\msedgedriver.exe"
driver = webdriver.Edge()

driver.get("https://merolagani.com")
stock= driver.find_element_by_id("ct100_AutoSuggest1_txtAutoSuggest")
stock.clear()
#send keys (input a value)
stock.send_keys("ADBL")