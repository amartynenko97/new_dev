from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import constants as const

class AuthorizationFacebook():

    def __init__(self, email, password, driver_path, logger):
        self.email = email
        self.password = password
        self.logger = logger
        self.init_driver(driver_path)
        self.wait = WebDriverWait(self.driver, timeout=30)
        
    def init_driver(self, driver_path):
        try:
            chrome_options = Options()
            chrome_options.binary_location = driver_path
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_argument('--no-sandbox') # bypass OS security model
            chrome_options.add_argument('--disable-dev-shm-usage') # overcome limited resource problems
            chrome_options.add_argument('--disable-notifications')
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        except Exception as e:
            self.logger.error("There's some error in initialization driver for chrome. " + str(e))
            self.driver.close()
            self.driver.quit()
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")

    def facebook_login(self):
        try:
            self.driver.get(const.LOGIN_URL)
            time.sleep(3)
            email_element = self.driver.find_element(By.XPATH, const.LOCATOR_TO_EMAIL_ELEMENT)
            email_element.send_keys(self.email)
            time.sleep(3)
            password_element = self.driver.find_element(By.XPATH, const.LOCATOR_TO_PASSWORD_ELEMENT)
            password_element.send_keys(self.password)
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, const.LOCATOR_TO_LOGIN_BUTTON_ELEMENT)))
            login_button.click()
        except Exception as e:
            self.logger.error("There's some error in log in. " + str(e))
            self.driver.close()
            self.driver.quit()
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")