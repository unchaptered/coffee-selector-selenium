from selenium import webdriver
from selenium.webdriver.common.by import By

from env import DRIVER_PATH

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome(DRIVER_PATH, options=options)

driver.implicitly_wait(10)
driver.get('https://www.nespresso.com/kr/ko/grands-crus-coffee-range#!/by-range')

card_group = driver.find_elements(By.CSS_SELECTOR, '#coffee-selector > div > div > div > ul > li')

try:
    for card_vertical in card_group:
        if card_vertical is not None:
            card_horizon = card_vertical.find_elements(By.CSS_SELECTOR, 'li')
            for card in card_horizon:
                if card is not None:
                    capsule_title = card.find_element(By.CSS_SELECTOR, 'h4')
                    if capsule_title is not None:
                        print(capsule_title.text)
                    capsule_strong = card.find_element(By.CSS_SELECTOR, 'span')
                    if capsule_strong is not None:
                        print(capsule_strong.text)
except:
    print('에러')