import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Locators


def Open_browser():
    driver = webdriver.Chrome(executable_path='C:/Users/NewUser/Desktop/New folder/webdriver/chromedriver.exe')
    driver.maximize_window()
    driver.get('http://192.168.4.222/login');
    return driver

def Authorization(driver):
    driver.find_element(*LOGIN_FIELD).send_keys(LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*ENTER_BUTTON).click()



#СЕЙЧАС ОПИСЫВАЕМ ФУНКЦИИ, КОТОРЫЕ НЕОБХОДИМЫ В АВТОТЕСТАХ
#ОСНОВНЫЕ ДЕЙСТВИЯ


def clean_the_field(driver,locator):
    field_to_clean = driver.find_element(*locator)
    field_to_clean = field_to_clean.clear()
    return field_to_clean

def add_text_to_the_field(driver,locator,text):
    field_to_add = driver.find_element(*locator)
    field_to_add = field_to_add.send_keys(text)
    return field_to_add

def click_the_button(driver,locator):
    field_to_click = driver.find_element(*locator)
    field_to_click = field_to_click.click()
    return field_to_click

def save_counter_meaning(driver,locator):
    meaning_int = driver.find_element(*locator)
    meaning_int = meaning_int.text

    meaning_int = meaning_int.replace(' ', '')
    if meaning_int.isdigit()==True:
        meaning_int = int(meaning_int)
        return meaning_int

def save_string(driver,locator):
    meaning_str = driver.find_element(*locator)
    meaning_str = meaning_str.text
    return meaning_str

def refresh_the_page(driver):
    driver.refresh()

def wait_time(time):
    time.sleep(time)



#создали класс у которого есть 1 характеристика driver со значением хром
#Это начало и его нужно перенести в отдельный py
class StartWorking:
    #чтобы везде не тащить driver превратим его в параметр self
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/NewUser/Desktop/New folder/webdriver/chromedriver.exe")

    """Описываем методы класса"""
    def Open_site(self):
        self.driver.maximize_window()
        self.driver.get("http://192.168.4.222/login");

    def clean_the_field(self, locator):
        field_to_clean = self.find_element(*locator)
        field_to_clean = field_to_clean.clear()
        return field_to_clean

#тест
#создали объект bb принадлежащий классу StartWorking
bb = StartWorking()
bb.Open_site()






