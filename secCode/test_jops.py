import pytest


@pytest.fixture()
def login(request):
    name = request.param
    print(f"== 账号是：{name} ==")
    return name


data=["Jhon","wang"]
ids = [f"login_test_name is:{name}" for name in data]


@pytest.fixture()
def logins(request):
    param = request.param
    print(f"账号是：{param['username']}，密码是：{param['password']}")
    return param

datas=[
    {"username":"Jhon wang","password":"testing"},
    {"username":"Shangjun yu","password":"testing"}
]




@pytest.mark.parametrize("login", data, ids=ids, indirect=True)
def test_name(login):
    print(f" 测试用例的登录账号是：{login} ")

@pytest.mark.parametrize("logins",datas,indirect=True)
def test_names(logins):
    print(f"账号：{logins['username']},密码是：{logins['password']}")

# 多个参数
@pytest.fixture(scope="module")
def input_user(request):
    user = request.param
    print(f"user:%s"%user)
    return user

@pytest.fixture(scope="module")
def input_psw(request):
    psw = request.param
    print(f"password:%s"%psw)
    return psw

datar = [
    ("wang","junjie"),
    ("yu","shuangjun")
]

@pytest.mark.parametrize("input_user,input_psw", datar, indirect=True)
def test_more_fixture(input_user, input_psw):
    print("fixture返回的内容:", input_user, input_psw)


# 多个fixture
@pytest.fixture(scope="function")
def input_user(request):
    user = request.param
    print("登录账户：%s" % user)
    return user


@pytest.fixture(scope="function")
def input_psw(request):
    psw = request.param
    print("登录密码：%s" % psw)
    return psw


name = ["name1", "name2"]
pwd = ["pwd1", "pwd2"]


@pytest.mark.parametrize("input_user", name, indirect=True)
@pytest.mark.parametrize("input_psw", pwd, indirect=True)
def test_more_fixture(input_user, input_psw):
    print("fixture返回的内容:", input_user, input_psw)