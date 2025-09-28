from calculator import add, subtract, multiply, divide

def test_add():       assert add(2,3) == 5
def test_subtract():  assert subtract(5,3) == 2
def test_multiply():  assert multiply(4,3) == 12
def test_divide_ok(): assert divide(10,2) == 5
def test_divide_zero(): assert divide(10,0) == "Error: division by zero"

# Extra test added for zero-division case (#2)
