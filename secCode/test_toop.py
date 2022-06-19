import pytest

@pytest.mark.weibo()
def test_weibo():
    print("test weibo")

@pytest.mark.zijie()
def test_zijie():
    print("test zijie")

@pytest.mark.weixin()
def test_weixin():
    print("test weixin")

@pytest.mark.xinlang()
class TestClass:
    def test_xinlang(self):
        print("test xinlang")

def test_nomark():
    print("not have mark`s task")