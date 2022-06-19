import pytest

# 调用方式1
@pytest.fixture
def login():
    print("输入账号，密码先登录")

def test_s1(login):
    print("用例1：登录之后其他动作 111")

def test_s2():
    print("用例2，不用登录 2222")

# 调用方式2
@pytest.fixture
def login1():
    print("please input password")

@pytest.mark.usefixtures("login1","login")
def test_s11():
    print("用例2，不需要登录   333")

# 调用方式3
@pytest.fixture(autouse=True)
def login2():
    print("========login==============")

@pytest.mark.usefixtures("login2")
def loginss():
    print(1)

@pytest.fixture(scope="session")
def open():
    print("===打开浏览器===")

@pytest.fixture
# @pytest.mark.usefixtures("open") 不可取！！！不生效！！！
def login(open):
    # 方法级别前置操作setup
    print(f"输入账号，密码先登录{open}")