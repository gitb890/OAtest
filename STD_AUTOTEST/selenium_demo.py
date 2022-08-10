'''
selenium的第一个测试用例
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
#创建webdriver对象


url = webdriver.Chrome()

#指定访问的路径
url.get("https://www.baidu.com/")

#找到指定的元素id或name
el = url.find_element(By.NAME,'wd').send_keys('selenium')

#对元素进行文本的操作
# el.send_keys('selenium')

# print(el.get_attribute('value'))

# 执行一次文本框输入查询
el = url.find_element(By.ID,'su').click()

# 等待
sleep(5)

# 退出浏览器
url.quit()