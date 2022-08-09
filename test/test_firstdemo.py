import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    d = webdriver.Chrome()  # 启动浏览器
    print("浏览器已启动")
    yield d
    # 将浏览器给测试用例使用
    d.quit()  # 退出浏览器
    print("浏览器已经关闭")


def test_qq(driver):
    driver = webdriver.Chrome()
    driver.get('https://www.qq.com')

    print(driver.title)  # 获取页面数据
    assert "百度" in driver.title  # 断言，这里一定失败

    driver.get_screenshot_as_file("b.png")  # 记录当前页面为png图片


def test_baidu(driver):
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')

    print(driver.title)  # 获取页面数据
    assert "百度" in driver.title  # 断言

    driver.get_screenshot_as_file("a.png")  # 记录当前页面为png图片
