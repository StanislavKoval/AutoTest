#Тестовая проверочная заметка
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import First_time.StartWorking
import First_time.Locators
from selenium.common.exceptions import NoAlertPresentException
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import First_time.StartWorking
import First_time.Actions
import First_time.Locators
import selenium
from selenium.common.exceptions import NoAlertPresentException
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


class Actions(First_time.StartWorking.Runner):
    """Простые Actions (обертки)"""

    def open_site(self):
        print('Открытие браузера')
        self.driver.maximize_window()
        self.driver.get(First_time.Locators.Page_adresses.LOGIN_PAGE)

    def close_site(self):
        print('Закрытие браузера')
        self.driver.quit()

    def refresh_the_page(self):
        print('Обновление страницы')
        self.driver.refresh()

    def add_text_to_the_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def clean_the_field(self, locator):
        field_to_clean = self.driver.find_element(*locator)
        field_to_clean = field_to_clean.clear()

    def add_text_to_the_field(self, locator, text):
        field_to_add = self.driver.find_element(*locator)
        field_to_add = field_to_add.send_keys(text)

    def click_the_button(self, locator):
        field_to_click = self.driver.find_element(*locator)
        field_to_click = field_to_click.click()

    def save_counter_meaning(self, locator):
        meaning_int = self.driver.find_element(*locator)
        meaning_int = meaning_int.text

        meaning_int = meaning_int.replace(' ', '')
        if meaning_int.isdigit() == True:
            meaning_int = int(meaning_int)
            return meaning_int

    def save_string(self, locator):
        meaning_str = self.driver.find_element(*locator)
        meaning_str = meaning_str.text
        return meaning_str

    def wait_time(self, time_to_wait):#выбрал самый плохой вариант
        time.sleep(time_to_wait)

    #неявная задержка
    def implicit_time(self, time_to_wait=60):
        self.driver.implicitly_wait(time_to_wait)

    def accept_alarm(self):
        self.driver.switch_to_alert().accept()

    # Проверка на существование элемента по локатору
    def verify_existence(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    # Проверка на наличие alarm на странице
    def verify_alert_existence(self):
        try:
            self.driver.switch_to_alert()
            return True
        except NoAlertPresentException:
            return False


    """Составные Actions с прописанными локаторами"""
    #по идее это нужно будет раскидать по класам локаторов

    def Autorization(self, Login=First_time.Locators.LOGIN, Password=First_time.Locators.PASSWORD):
        Actions.open_site(self)
        Actions.add_text_to_the_field(self,
                                      locator=First_time.Locators.Login_Page_Locators.LOGIN_FIELD,
                                      text=Login)
        Actions.wait_time(self,
                          time_to_wait=1)
        Actions.add_text_to_the_field(self,
                                      locator=First_time.Locators.Login_Page_Locators.PASSWORD_FIELD,
                                      text=Password)
        Actions.wait_time(self, time_to_wait=1)
        Actions.click_the_button(self,
                                 locator=First_time.Locators.Login_Page_Locators.ENTER_BUTTON)
        Actions.wait_time(self, time_to_wait=2)

        # Проверка
        if self.driver.current_url == First_time.Locators.Page_adresses.CASES_PAGE:
            print('Успешная авторизация')
        else:
            print("Авторизация не удалась")

    def Create_case(self, Case_number, Case_name, delete=False):

        if self.driver.current_url == First_time.Locators.Page_adresses.CASES_PAGE:
            Actions.click_the_button(self, locator=First_time.Locators.Case_Page_Locators.ADD_CASE_BUTTON)
            Actions.add_text_to_the_field(self, locator=First_time.Locators.Case_Page_Locators.NUMBER_FIELD,
                                          text=Case_number)
            Actions.add_text_to_the_field(self, locator=First_time.Locators.Case_Page_Locators.NAME_FIELD,
                                          text=Case_name)
            Actions.click_the_button(self, locator=First_time.Locators.Case_Page_Locators.ADD_BUTTON)
            Actions.wait_time(self, time_to_wait=1)

            # остановился тут
            if Actions.verify_alert_existence(self) == True:
                if self.driver.switch_to_alert().text =='Данное дело уже существует':
                    return print('Данное дело уже существует')

            # Задержка на время создания
            #Actions.implicit_time(self)
            Actions.wait_time(self, time_to_wait=10)

            # перед тем как выводить лог сделать проверку + учесть счетчик
            print('Дело создано')

            if delete == True:
                print('Удаляем созданное тестовое дело')
                Actions.click_the_button(self, locator=First_time.Locators.Case_Page_Locators.THREE_DOT_BUTTON)
                Actions.click_the_button(self, locator=First_time.Locators.Case_Page_Locators.DELETE_CASE_BUTTON)
                Actions.accept_alarm(self)
                Actions.wait_time(self, time_to_wait=5)
                print('Удалено')

        else:
            print("Пользователь не находится на странице /cases")

    def Create_person(self, Surname, Name, delete=False):

        if self.driver.current_url == First_time.Locators.Page_adresses.PERSONS_PAGE:
            Actions.click_the_button(self, locator=First_time.Locators.Person_Page_Locators.ADD_PERSON_BUTTON)
            Actions.add_text_to_the_field(self, locator=First_time.Locators.Person_Page_Locators.SURNAME_FIELD,
                                          text=Surname)
            Actions.add_text_to_the_field(self, locator=First_time.Locators.Person_Page_Locators.NAME_FIELD,
                                          text=Name)
            Actions.click_the_button(self, locator=First_time.Locators.Person_Page_Locators.ADD_BUTTON)
            # Задержка на время создания персоны
            Actions.wait_time(self, time_to_wait=10)

            #перед тем как выводить лог сделать проверку
            print('Персона создана')

            if delete == True:
                print('Удаляем созданную тестовую персону')
                Actions.click_the_button(self, locator=First_time.Locators.Person_Page_Locators.THREE_DOT_BUTTON)
                Actions.wait_time(self, time_to_wait=1)
                Actions.click_the_button(self, locator=First_time.Locators.Person_Page_Locators.DELETE_PERSON_BUTTON)
                Actions.wait_time(self, time_to_wait=5)
                Actions.accept_alarm(self)
                Actions.wait_time(self, time_to_wait=7)
                print('Удалено')

        else:
            print("Пользователь не находится на странице /persons")

    #применения фильтра категории
    def Apply_filter(self,):#наверное лучше будет потом преобразовать его как применение фильтра категории #,checkbox_i_need, counter_i_need)
        if self.driver.current_url == First_time.Locators.Page_adresses.WORKSPACE_PAGE:
            all_elements = Actions.save_counter_meaning(self,First_time.Locators.Workspace_Page_Locators.MAIN_ELEMENT_COUNTER)
            #print(all_elements)
            Actions.click_the_button(self,First_time.Locators.Workspace_Page_Locators.OPEN_CATEGORIES_BUTTON)#поиграть с локаторами так чтобы сделать их зависисмыми от порядкого номера
            Actions.click_the_button(self,First_time.Locators.Workspace_Page_Locators.CATEGORIES_FILES_CHECKBOX)
            elements_in_filter =  Actions.save_counter_meaning(self,First_time.Locators.Workspace_Page_Locators.CATEGORIES_FILES_COUNTER)
            #print(elements_in_filter)

            # Применяем фильтр
            Actions.click_the_button(self,First_time.Locators.Workspace_Page_Locators.APPLY_FILTER_BUTTON)

            #Ожидание результата применения фильтра
            Actions.wait_time(self, time_to_wait=40)
            print('Фильтр применен')


            elements_after_filtration = Actions.save_counter_meaning(self,First_time.Locators.Workspace_Page_Locators.MAIN_ELEMENT_COUNTER)
            #print(elements_after_filtration)
            print('Проверка счетчиков')

            if elements_in_filter == elements_after_filtration:
                #Нажимаем кнопку сбросить
                Actions.click_the_button(self, First_time.Locators.Workspace_Page_Locators.RESET_BUTTON)

                # Ожидание результата после сброса фильтра
                Actions.wait_time(self, time_to_wait=15)

                all_elements_after_filtration = Actions.save_counter_meaning(self,First_time.Locators.Workspace_Page_Locators.MAIN_ELEMENT_COUNTER)

                if all_elements_after_filtration == all_elements:
                    print('Счетчики исправны')
                    Actions.wait_time(self, time_to_wait=3)
                    print('Фильтр успешно применен')
                    Actions.close_site(self)

                else:
                    # неплохо вставить скриншот
                    print('Счетчики сломаны!')
                    Actions.close_site(self)

            else:
                #неплохо вставить скриншот
                print('Счетчики сломаны!')
                Actions.close_site(self)

        else:
            print('Пользователь не находится на странице /workspace')

        #Нужно понять как удобно свести все else к одному удобному списку

    def Apply_search_description(self,text_to_the_field):
        if self.driver.current_url == First_time.Locators.Page_adresses.WORKSPACE_PAGE:

            all_elements = Actions.save_counter_meaning(self,locator=First_time.Locators.Workspace_Page_Locators.MAIN_ELEMENT_COUNTER)
            Actions.clean_the_field(self,locator=First_time.Locators.Workspace_Page_Locators.DESCRIPTION_SEARCH_FIELD)
            text_to_the_field_check=text_to_the_field
            Actions.add_text_to_the_field(self,locator=First_time.Locators.Workspace_Page_Locators.DESCRIPTION_SEARCH_FIELD,text=text_to_the_field)#почему-то после применения данного метода значение вводимое в поле текст изменяется
            Actions.click_the_button(self, First_time.Locators.Workspace_Page_Locators.APPLY_FILTER_BUTTON)

            # Ожидание результата применения фильтра
            Actions.wait_time(self, time_to_wait=60)
            print('Фильтр "Поиск по описанию" применен')

            #нужно написать алгоритм, который будет пробегать через конкретный параметр
            elem_of_grid = Actions.save_string(self,locator=("xpath","//div[@class='app-mailBox-contentTab']/div[1]//div[@class='app-mailBox-item-link']//div[1]//div[2]//div[1]"))
            # //div[@class='app-mailBox-contentTab']/div[@class='app-mailBox-item table-success']//div[@class='app-mailBox-item-link']//div[1]//div[2]//div[1]
            #div 8  это параметр
            #//div[@class='app-mailBox-contentTab']/div[8]//div[@class='app-mailBox-item-link']//div[1]//div[2]//div[1]

            Actions.wait_time(self, time_to_wait=20)
            print(elem_of_grid)

            #приведение к нижнему регистру
            elem_of_grid = elem_of_grid.lower()
            text_to_the_field = text_to_the_field.lower

            if elem_of_grid.find(text_to_the_field_check)!=-1:
                print("В первом элементе есть слово из фильтра")
            else:
                print("В первом элементе нет слова из фильтра")
        else:
            print('Пользователь не находится на странице /workspace')












    """Переходы на страницы"""

    def Go_to_Cases(self, time_to_wait=3):

        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.CASE_BUTTON)
        Actions.wait_time(self, time_to_wait=time_to_wait)
        #проверка
        if self.driver.current_url == First_time.Locators.Page_adresses.CASES_PAGE:
            print('Переход на страницу Дела')
        else:
            print('Переход на страницу Дела не удался')

    def Go_to_Workspace(self, time_to_wait=3):
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.WORKSPACE_BUTTON)
        Actions.wait_time(self, time_to_wait=time_to_wait)
        # проверка
        if self.driver.current_url == First_time.Locators.Page_adresses.WORKSPACE_PAGE:
            print('Переход на страницу Рабочее пространство')
        else:
            print('Переход на страницу Рабочее пространство не удался')

    def Go_to_Devices(self, time_to_wait=3):
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.LIBRARY_BUTTON)
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.DEVICES_BUTTON)
        Actions.wait_time(self, time_to_wait=time_to_wait)
        if self.driver.current_url == First_time.Locators.Page_adresses.DEVICES_PAGE:
            print('Переход на страницу Устройства')
        else:
            print('Переход на страницу Устройства не удался')

    def Go_to_Persons(self, time_to_wait=3):
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.LIBRARY_BUTTON)
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.PERSONS_BUTTON)
        Actions.wait_time(self, time_to_wait=time_to_wait)
        if self.driver.current_url == First_time.Locators.Page_adresses.PERSONS_PAGE:
            print('Переход на страницу Персоны')
        else:
            print('Переход на страницу Персоны не удался')

    def Go_to_Dictionaries(self, time_to_wait=3):
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.LIBRARY_BUTTON)
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.DICTS_BUTTON)
        Actions.wait_time(self, time_to_wait=time_to_wait)
        if self.driver.current_url == First_time.Locators.Page_adresses.DICTIONARY_PAGE:
            print('Переход на страницу Словари')
        else:
            print('Переход на страницу Словари не удался')

    def Go_to_Tags(self,time_to_wait=3):
        print('Переход на страницу Теги')
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.LIBRARY_BUTTON)
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.TAGS_BUTTON)
        Actions.wait_time(self, time_to_wait=time_to_wait)
        if self.driver.current_url == First_time.Locators.Page_adresses.TAGS_PAGE:
            print('Переход на страницу Теги')
        else:
            print('Переход на страницу Теги не удался')






