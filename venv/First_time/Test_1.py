import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

import First_time.StartWorking
import First_time.Actions
import First_time.Locators

# создали экземпляр класса

bb = First_time.Actions.Actions()
bb.Autorization()
bb.Go_to_Workspace()
#bb.

"""Создать, удалить дело"""
def first_test(object):
    print('Тест1 начат')
    object.Autorization()
    object.Create_case(Case_number='Test_Number', Case_name='Test_Name', delete=True)
    object.close_site()
    print('Тест1 завершен')

#first_test(bb)#cломалась кнопка удалить дело

"""Создать, удалить персону"""
def second_test(object):
    print('Тест2 начат')
    object.Autorization()
    object.Go_to_Persons()
    object.Create_person(Name='Test_Name', Surname='Test_Surname', delete=True)
    object.close_site()
    print('Тест2 завершен')

#second_test(bb)

"""Применить фильтр 'Поиск по содержимому'"""
def third_test(object):
    print('Тест3 начат')
    object.Autorization()
    object.Go_to_Workspace()
    object.Apply_search_description(text_to_the_field='привет')
    object.close_site()
    print('Тест3 завершен')

#third_test(bb)

'''
bb.Autorization()
bb.Go_to_Workspace()
bb.Apply_filter()
bb.Go_to_Cases()
#str=bb.save_string(('xpath',"//div[@class='app-mailBox-item table-success']//div[@class='app-mailBox-item-link']//div[@class='app-mailBox-item-link-desc app-mailBox-desc']/div[@class='app-mailBox-item-link-desc-item']//div[@class='app-mailBox-item-link-desc-item-info']/div[@class='app-mailBox-item-link-desc-item-info-text']"))
#print(str)
bb.close_site()
'''
#driver.findElement(By.xpath("//div[@class='app-mailBox-item table-success']//div[@class='app-mailBox-item-link']//div[1]//div[2]//div[1]"))

'''
Нужно изучить:
-задержки о готовности
-Логи нормально сформировать
-последовательный запуск тестов
-как пробегать по html в гриде и последовательных списках


Решить проблему с переходами 

Идеи для тестов:
'''