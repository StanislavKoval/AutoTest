""""
Вопросы:
1.Есть ли .By в питон
2.
"""
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/NewUser/Desktop/New folder/webdriver/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.maximize_window()#Открывает окно браузера на полную
driver.get('http://192.168.4.222/login');
time.sleep(1) # Let the user actually see something!
#Autorization
driver.find_element_by_name("UID").send_keys("staskovall")#обращение по name
driver.find_element_by_name("PWD").send_keys("Tom2bread")
driver.find_element_by_name("OK").click()#найти по name и кликнуть
time.sleep(1)
driver.find_element_by_xpath("//span[text()='Рабочее пространство']").click()#обращение по xpath
time.sleep(1)
#driver.find_element_by_id("searchInput").send_keys("test")
#time.sleep(2)
#driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
#time.sleep(90)
#driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
#time.sleep(2)
#xpath селектор
#клик на уголок Дела
driver.find_element_by_xpath("//body/div[@class='app-wrapper']/wa-root/wa-workspace/div[@class='pageContainer wsPage']/div[@class='ws-marginTop']/ws-tab/div[@class='app-contentPage']/div[@class='b-leftSideBar']/div[@class='b-filter filter-workspace']/div[@class='b-filterBody']/div[@class='b-filterHeader filter-workspace']/div[@class='priorityFaset']/div[1]/div[1]/div[2]/span[1]").click()
time.sleep(1)
#css селектор
#клик на уголок Дела
#driver.find_element_by_css_selector("div.app-wrapper:nth-child(1) div.pageContainer.wsPage div.ws-marginTop:nth-child(3) div.app-contentPage div.b-leftSideBar div.b-filter.filter-workspace div.b-filterBody div.b-filterHeader.filter-workspace div.priorityFaset:nth-child(1) div.b-filterItem.dropdown:nth-child(2) div.b-filterItem_head.checkGroup div.b-filterItem_title > span.b-filterItem_arrow.f_chO").click()
#time.sleep(1)

one=driver.find_element_by_xpath("//span[contains(@class,'app-content-title-count')]").text
print(one)
print(type(one))
one=one.replace(' ','')
one=int(one)
print(one)
print(type(one))
time.sleep(2)
driver.quit()








