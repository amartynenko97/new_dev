from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
import time
import random
import constants as const

class ParseInfoFromFrendsList():

    def parse_links_from_frends_list(self, driver, wait, logger, collection_facebook, total_profiles):
        self.__move_to_friendslist(wait)
        friends_link = driver.find_elements(By.XPATH, const.LOCATOR_TO_FRENDS_LINK_ELEMENT)
        random.shuffle(friends_link)
        for index, friend in enumerate(friends_link):
            friend.click()
            time.sleep(random.randint(3, 4))
            try:
                collection_facebook['name'].append(driver.find_element(By.XPATH, const.LOCATOR_TO_NAME_ELEMENT).text)
                collection_facebook['link'].append(friend.get_attribute("href"))
                collection_facebook['location'].append(driver.find_element(By.XPATH, const.LOCATOR_TO_LOCATION_ELEMENT).text)
            except NoSuchElementException:
                logger.error(f"{collection_facebook['name'][index]} has no location information on his profile")      
                collection_facebook['location'].append(None)
            try:
                driver.find_element(By.XPATH, const.LOCATOR_TO_OPEN_PHOTO_ELEMENT).click()
                time.sleep(random.randint(2, 4))
                driver.find_element(By.XPATH, const.LOCATOR_TO_CLOSE_PHOTO_ELEMENT).click()
                time.sleep(random.randint(2, 4))
            except (NoSuchElementException, ElementNotVisibleException):
                logger.error(f"{collection_facebook['name'][index]}'s profile photo was not found")
                pass
            try:
                self.__find_and_collect_birthday_data(driver, collection_facebook, index, logger)
            except NoSuchElementException:
                continue
            if len(collection_facebook['name']) == total_profiles:
                break

    def __find_and_collect_birthday_data(self, driver, collection_facebook, index, logger):
        driver.execute_script(const.WINDOW_SCROLL_SCRIPT)
        time.sleep(random.randint(2, 4))
        driver.find_element(By.XPATH, const.LOCATOR_TO_INFO_BUTTON_ELEMENT).click()
        time.sleep(random.randint(2, 4))
        driver.find_element(By.XPATH, const.LOCATOR_TO_MAIN_INFO_ELEMENT).click()
        time.sleep(random.randint(2, 4))
        items = driver.find_elements(By.XPATH, const.LOCATOR_TO_DATE_FIELDS_ELEMENT)
        if len(items) == 2:
            collection_facebook['date_of_birth'].append(f"{items[0].text}, {items[1].text}")
        else:
            collection_facebook['date_of_birth'].append(None)
            logger.error(f"{collection_facebook['name'][index]}'s profile does not have any of the fields about the date of birth")    

    def __move_to_friendslist(self, wait):
        profile_button = wait.until(EC.element_to_be_clickable((By.XPATH, const.LOCATOR_TO_PROFILE_BUTTON_ELEMENT)))
        profile_button.click()
        time.sleep(random.randint(2, 4))
        button_friends = wait.until(EC.element_to_be_clickable((By.XPATH, const.LOCATOR_TO_FRENDS_BUTTON_ELEMENT)))
        button_friends.click()
        time.sleep(random.randint(2, 4))
        button_friends_list = wait.until(EC.element_to_be_clickable((By.XPATH, const.LOCATOR_TO_FRENDS_LIST_BUTTON_ELEMENT)))
        button_friends_list.click()
        time.sleep(random.randint(2, 4))