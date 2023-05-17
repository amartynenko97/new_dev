LOGIN_URL = 'https://www.facebook.com/'
LOGIN_INPUT_ID = 'email'
PASSWORD_INPUT_ID = 'pass'
LOGIN_PIN_NAME = 'login'
LOCATOR_TO_EMAIL_ELEMENT = "//input[@type = 'text']"
LOCATOR_TO_PASSWORD_ELEMENT = "//input[@type = 'password']"
LOCATOR_TO_LOGIN_BUTTON_ELEMENT = "//button[@name = 'login']"
LOCATOR_TO_PROFILE_BUTTON_ELEMENT = "//span[text() = 'Антон Мартиненко']"
LOCATOR_TO_FRENDS_BUTTON_ELEMENT = "//a[contains(@aria-label, 'Друзі')]"
LOCATOR_TO_FRENDS_LIST_BUTTON_ELEMENT = "(//div[@class = 'xw7yly9']//a[contains(@class, 'x1i10hfl x1qjc9v5')])[4]"
LOCATOR_TO_FRENDS_LINK_ELEMENT = "//div[@class = 'x135pmgq']//a[contains(@class, 'x1i10hfl x1qjc9v5')]"
LOCATOR_TO_NAME_ELEMENT = "(//h1[@class = 'x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz'])[2]"
LOCATOR_TO_LOCATION_ELEMENT = "//span[contains(@class, 'x193iq5w xeuugli') and contains(text(),'Живе у ')]//a//span/span"
LOCATOR_TO_OPEN_PHOTO_ELEMENT = "//div[@class ='x1jx94hy x14yjl9h xudhj91 x18nykt9 xww2gxu x1iorvi4 x150jy0e xjkvuk6 x1e558r4']//a"
LOCATOR_TO_CLOSE_PHOTO_ELEMENT = "(//div[contains(@aria-label, 'Закрити')])[1]"
LOCATOR_TO_INFO_BUTTON_ELEMENT = "(//div[@class = 'x1ey2m1c x9f619 xds687c x10l6tqk x17qophe x13vifvy']/a)[2]"
LOCATOR_TO_MAIN_INFO_ELEMENT = "//div[@class = 'x1e56ztr'][4]/a"
LOCATOR_TO_DATE_FIELDS_ELEMENT = "(//div[text()='Дата народження']/../../../../../../../../div/span)[1] | (//div[text()='Рік народження']/../../../../../../../../div/span)[1]"
WINDOW_SCROLL_SCRIPT = "scrollBy(0,500)"


CONFIG_FILE_NAME = "config.ini"
DICT_FOR_VALIDATION = { 'logger':     {'level'        : ('INFO', 'DEBUG', 'ERROR', 'CRITICAL', 'WARNING'),
                                       'log_file_name': 'logging.log'},
                                  
                        'driver':      {'path_driver': '/usr/bin/google-chrome'},

                        'credentials': {'email'   : '---логин---',
                                        'password': '---пароль---'},

                        'parser':      {'amount_of_friends': None}
                    }