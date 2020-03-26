import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Учетная запись для входа
LOGIN = "staskovall"
PASSWORD = "Tom2bread"

class Page_adresses:
    LOGIN_PAGE="http://192.168.4.222/login"
    CASES_PAGE="http://192.168.4.222/cases"
    DEVICES_PAGE = "http://192.168.4.222/devices"
    PERSONS_PAGE="http://192.168.4.222/persons"
    DICTIONARY_PAGE = "http://192.168.4.222/dicts"
    TAGS_PAGE = "http://192.168.4.222/tags"
    WORKSPACE_PAGE="http://192.168.4.222/workspace"
    FILES_PAGE="http://192.168.4.222/workspace/1"
    MAPS_PAGE="http://192.168.4.222/workspace/0"

class Login_Page_Locators:
    LOGIN_FIELD = (By.NAME, 'UID')
    PASSWORD_FIELD = (By.NAME, "PWD")
    ENTER_BUTTON = (By.NAME, "OK")
    ALARM_INVALID_LOGIN_OR_PASSWORD = (By.XPATH, "//div[@class='alert alert-danger mt-2']")

#вверхний бар
class Navigation_Locators:
    CASE_BUTTON  = (By.XPATH,"//a[@class='app-header-content-topMenu-ul-li-link active']")
    WORKSPACE_BUTTON = (By.XPATH,"//a[@class='app-header-content-topMenu-ul-li-link']")
    LIBRARY_BUTTON = (By.XPATH,"//div[@class='app-header-content-topMenu-ul-li-link']//span[@class='app-header-content-topMenu-ul-li-link-label']")
    DEVICES_BUTTON = (By.XPATH,"//li[@class='app-header-content-topMenu-ul-li topMenu-li']//li[1]//span[1]")
    PERSONS_BUTTON = (By.XPATH,"//li[@class='app-header-content-topMenu-ul-li topMenu-li']//li[2]//span[1]")
    DICTS_BUTTON = (By.XPATH,"//li[@class='app-header-content-topMenu-ul-li topMenu-li']//li[3]//span[1]")
    TAGS_BUTTON = (By.XPATH,"/html[1]/body[1]/div[1]/wa-root[1]/wa-cases[1]/div[1]/wa-header[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]/div[2]/nav[1]/li[4]/span[1]")
    SYS_JOURNAL_BUTTON = (By.XPATH,"//li[5]//span[1]")

class Case_Page_Locators:
    CASE_COUNTER = (By.XPATH,"//span[@class='app-content-title-count']")
    ADD_CASE_BUTTON = (By.XPATH, "//div[@class='dataTableSort-addTrigger']")
    QUICKFILTER_FIELD = (By.XPATH, "//input[@id='flt']")

    PERSON_COUNTER = (By.XPATH,"//div[@class='app-contentPage-sideBarSubTitle']")
    NUMBER_FIELD = (By.XPATH,"//input[@id='editableNumber']")
    NAME_FIELD = (By.XPATH,"//input[@id='editableName']")
    ADD_BUTTON = (By.XPATH,"//button[@id='btn-case']")
    PERSON_TAB = (By.XPATH,"//div[@class='app-contentPage']//li[2]//span[1]")
    CASE_TAB = (By.XPATH,"//li[@class='active']//span[@class='c-tab__link']")
    THREE_DOT_BUTTON = (By.XPATH,"//div[@class='barMenu-trigger']")
    FROM_CASES_TO_WORKSPACE_BUTTON = (By.XPATH, "//div[@class='barMenu-window barMenu--open']/button[1]")
    FROM_CASES_TO_FILES_BUTTON = (By.XPATH, "//div[@class='barMenu-window barMenu--open']/button[2]")
    DELETE_CASE_BUTTON = (By.XPATH, "//div[@class='barMenu-window barMenu--open']/button[3]")

class Person_Page_Locators:
    PERSON_COUNTER = (By.XPATH, "//span[@class='app-content-title-count']")
    ADD_PERSON_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-case-persons[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")
    DEVICE_COUNTER = (By.XPATH, "//div[@class='dataTableSort-addTrigger']")
    SURNAME_FIELD = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-case-persons[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/wa-edit-card[1]/div[1]/wa-field-editor[1]/div[1]/input[1]")
    NAME_FIELD = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-case-persons[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/wa-edit-card[1]/div[2]/wa-field-editor[1]/div[1]/input[1]")
    ADD_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-case-persons[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/button[1]")
    DEVICE_TAB = (By.XPATH, "//div[@class='app-contentPage']//li[2]//span[1]")
    THREE_DOT_BUTTON = (By.XPATH, "//div[@class='barMenu-trigger']")
    FROM_PERSONS_TO_WORKSPACE_BUTTON = (By.XPATH, "//div[@class='sidebarHead']//button[1]")
    FROM_PERSONS_TO_FILES_BUTTON = (By.XPATH, "//body//button[2]")
    DELETE_PERSON_BUTTON = (By.XPATH, "//div[@id='barMenuWindow']/button[3]")
    ADD_DEVICE_BUTTON = (By.XPATH, "//div[@class='app-tabContent tabs active']//button[@class='btn btn-primary']")

class Workspace_Page_Locators:
    RESET_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/button[2]")
    DESCRIPTION_SEARCH_FIELD = (By.XPATH, "//input[@id='searchInput']")
    FROM_DATE_FIELD = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]")
    TO_DATE_FIELD = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[2]/input[1]")
    OPEN_CATEGORIES_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/span[1]")

    CATEGORIES_FILES_CHECKBOX = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
    CATEGORIES_FILES_COUNTER = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/div[4]")

    APPLY_FILTER_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[2]/button[1]")

    MAIN_ELEMENT_COUNTER = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/ws-datagrid[1]/div[1]/div[1]/span[1]")



    #чекбоксы
    #/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]/div[поиграть с счетчиком, может будет бегать по всем фильтрам]/div[1]/div[1]/div[1]/input[1]




##(By.XPATH, "")


