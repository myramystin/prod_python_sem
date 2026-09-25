import pytest 

@pytest.fixture(scope='function')
def numbers_f():
    return [1, 2, 3, 4, 5, 100, 200]
