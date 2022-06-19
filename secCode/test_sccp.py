import pytest

@pytest.fixture(autouse=True)
def login():
    print("====login======")

def test_case01():
    print("======first case=======")

@pytest.mark.skip(reason="skip this cases")
def test_case02():
    print("====this is secend case")

class Test1:
    def test_1(self):
        print("%%is test case 111111 %%")

    @pytest.mark.skip(reason="do not want to do this`s case")
    def test_2(self):
        print("%% this is secend case2222 %%")

@pytest.mark.skip(reason="skip class")
class Testcase:
    def test_1(self):
        print("%% not doing %%")