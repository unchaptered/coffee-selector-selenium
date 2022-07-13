from selenium import webdriver
from selenium.webdriver.common.by import By

from modules.env import DRIVER_PATH, MONGO_URL, DATABASE_NAME, COLLECTION_CAPSULE
from modules.database import getMongoClient

# database = getMongoClient(MONGO_URL)[DATABASE_NAME]

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome(DRIVER_PATH, options=options)

driver.implicitly_wait(10)
driver.get('https://www.nespresso.com/kr/ko/grands-crus-coffee-range#!/by-range')

card_group = driver.find_elements(By.CSS_SELECTOR, '#coffee-selector > div > div > div > ul > li')

capsule_list = []
for card_vertical in card_group:

    if card_vertical is not None:

        card_horizon = card_vertical.find_elements(By.CSS_SELECTOR, 'li')

        for card in card_horizon:

            if card is not None:

                card.find_element(By.CSS_SELECTOR, 'a').click()

                capsule_title = card.find_element(By.CSS_SELECTOR, 'h4')
                capsule_strong = card.find_element(By.CSS_SELECTOR, 'span')

                if capsule_title is not None and capsule_strong is not None:

                    print(capsule_title.text, capsule_strong.text)
                    capsule_list.append({
                        'capsule_title': capsule_title.text,
                        'capsule_strong': int(capsule_strong.text)
                    })

print(capsule_list)
# database[COLLECTION_CAPSULE].insert_many(capsule_list)