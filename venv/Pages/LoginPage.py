'''
1.импорты
1.1 значение, которое будет в полях
2.набор методов
3.методы, которые можно реализовывать на данной странице
'''

import time
from selenium import webdriver

class LoginPage:

    driver = webdriver.Chrome(executable_path='C:/Users/NewUser/Desktop/New folder/webdriver/chromedriver.exe')
    #xpath ссылки
    #def __init__(self):


    def find_by_name(webdriver,name):
        driver.find_element_by_name(name)
























