from src.main import add, substract

def test_add_function():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(5, 5) == 10

def test_substract_function():
    assert substract(5, 3) == 2
    assert substract(0, 0) == 0
    assert substract(10, 5) == 5