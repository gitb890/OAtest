from selenium import webdriver

# 启动浏览器
driver = webdriver.Chrome()
# 获取到网址
driver.get('https://www.baidu.com')
# 退出浏览器
driver.quit()