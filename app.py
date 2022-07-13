from selenium import webdriver
from selenium.webdriver.common.by import By

from env import DRIVER_PATH

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome(DRIVER_PATH, options=options)
driver.get('https://www.nespresso.com/kr/ko/order/capsules/vertuo')

cards = driver.find_elements(By.CSS_SELECTOR, '#PLPListContainer > div')
for card in cards:
    card_meta = card.find_element(By.CSS_SELECTOR, '.cn_card__content')
    card_title = card_meta.find_element(By.CSS_SELECTOR, '.cn_card__title').text
    card_text = card_meta.find_element(By.CSS_SELECTOR, '.cn_card__text').text

    print(card_title, card_text)