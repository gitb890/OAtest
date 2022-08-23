'''
通过selenium底层实现浏览器操作
'''
from selenium.webdriver.chrome.webdriver import WebDriver


# url = webdriver.Chrome()
from selenium.webdriver.common.by import By

driver = WebDriver(executable_path="chromedriver")
# 创建的是一个session对象，后续调用的都是这个对象

# url.get("https://www.baidu.com/")
driver.execute("get", {'url': "https://www.baidu.com/"})

# url = driver.find_element(By.NAME,'wd').send_keys('selenium')
#找到指定的元素id或name
# el = url.find_element(By.NAME,'wd').send_keys('selenium')

el = driver.execute("findElement",{
            'using': "xpath",
            'value': '//input[@id="kw"]'})['value']
#对元素进行文本的操作
# el.send_keys('selenium')

# print(el.get_attribute('value'))
el._execute("sendKeysToElement",
                      {'text': "selenium",
                       'value': ""})
# 执行一次文本框输入查询
# el = url.find_element(By.ID,'su').click()
el1 = driver.execute("findElement",{
            'using': "xpath",
            'value': '//input[@id="su"]'})['value']
el1._execute("clickElement")
