import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Runner:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/NewUser/Desktop/New folder/webdriver/chromedriver.exe")
