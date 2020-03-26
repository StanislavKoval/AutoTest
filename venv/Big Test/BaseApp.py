from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/NewUser/Desktop/New folder/webdriver/chromedriver.exe")
        self.base_url = "https://ya.ru/"

    def find_element(self, locator,time=2):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),message="Can't find element by locator {locator}")

    def find_elements(self, locator,time=2):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),message="Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)