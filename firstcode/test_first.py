
def func(x):
    return x+1

def test_answer():
    assert func(3) == 4

def test_function():
    a = 3
    assert a%3 == 0,"判断a为奇数，当前数为%s"%a

class TestClass:
    def test_one(self):
        x = "this"
        print("hello -----------------------")
        assert "h" in x

    def test_two(self):
        x = "myworld"
        assert "o" in x