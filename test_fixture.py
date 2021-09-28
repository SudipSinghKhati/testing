import pytest

'''
test using fixtures
Fixtures are functions, which will run before each test function to which it is applied.
 Fixtures are used to feed some data to the tests such as database connections, 
 URLs to test and some sort of input data. Therefore, instead of running the same code 
 for every test, we can attach fixture function to the tests and it will run and 
 return the data to the test before executing each test.
'''


@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 25
    return [a, b, c]


def test_method1(numbers):
    x = 15
    assert numbers[0] == x


def test_method2(numbers):
    y = 20
    assert numbers[1] == y


def test_method3(numbers):
    z = 25
    assert numbers[2] == z
