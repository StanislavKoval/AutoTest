import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/NewUser/Desktop/New folder/webdriver/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.maximize_window()#Открывает окно браузера на полную
driver.get('https://meduza.io/')



#one=driver.find_element_by_xpath('//div[@class="App-root"]//div[1]//div[2]//article[1]//div[1]//div[1]//div[2]//h2[1]//a[1]').text
#Путин сказал, что он настоящий. «Удмурта» и «Банкетного» не существует
#one=driver.find_element_by_xpath('//section[1]//div[2]//div[3]//article[1]//div[2]//div[1]//div[2]//h2[1]//a[1]').text
two=driver.find_element_by_css_selector("div.App-root div.App-container div.App-header header.Header-root div.Header-nav nav.Header-menu span.Header-item.Header-isItemActive a.Link-root").text

#print(one)
print(two)



time.sleep(2)
driver.quit()





















