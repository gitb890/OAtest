from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver(executable_path="chromedriver")

driver.get("http://www.baidu.com")

# id
# driver.find_element('id','kw').send_keys('selenium')
# name
# driver.find_element('name','wd').send_keys('selenium')
# link text
# driver.find_element('link text','新闻').click()
# partial link text
# driver.find_element('partial link text','新闻').click()
# tag name
# el = driver.find_elements('tag name','input')
# for i in el:
#     print(i)
#
# sl = driver.find_element('tag name','input')
# print('--'*30)
# print(sl)
# class name
# driver.find_element('class name','s_ipt').send_keys('selenium')
# css selector
# driver.find_element('css selector','#kw').send_keys('css selector')
# xpath
driver.find_element('xpath','//input[@id="kw"]').send_keys('xpath')