from selenium import webdriver

from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver');
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('Selenium')
driver.find_element_by_id('su').click()
