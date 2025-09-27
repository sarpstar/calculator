def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error"

if __name__ == "__main__":
    print("Toplama:", add(5,3))
    print("Çıkarma:", subtract(5,3))
    print("Çarpma:", multiply(5,3))
    print("Bölme:", divide(5,3))
