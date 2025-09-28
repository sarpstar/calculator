def _ensure_number(x):
    if not isinstance(x, (int, float)):
        raise TypeError("a ve b sayısal olmalı")

def add(a, b):
    _ensure_number(a); _ensure_number(b)
    return a + b

def subtract(a, b):
    _ensure_number(a); _ensure_number(b)
    return a - b

def multiply(a, b):
    _ensure_number(a); _ensure_number(b)
    return a * b

def divide(a, b):
    _ensure_number(a); _ensure_number(b)
    if b == 0:
        return "Error: division by zero"
    return a / b

if __name__ == "__main__":
    print("Toplama:", add(5,3))
    print("Çıkarma:", subtract(5,3))
    print("Çarpma:", multiply(5,3))
    print("Bölme:", divide(5,3))
