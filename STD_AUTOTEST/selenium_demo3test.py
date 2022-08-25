from time import sleep


from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver(executable_path="chromedriver")
driver.get("https://www.baidu.com")

el = driver.find_element("id","kw")
el.send_keys("111")

el = driver.find_element("id","su").click


sleep(5)
# 这里引用的是time库中的sleep函数

driver.quit()




