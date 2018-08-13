from selenium import webdriver

from selenium import webdriver

##打开chrome

driver = webdriver.Chrome('/usr/local/bin/chromedriver');
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('Selenium')
#模拟点击事件
driver.find_element_by_id('su').click()
