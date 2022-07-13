from selenium import webdriver
from env import DRIVER_PATH

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome(DRIVER_PATH, options=options)