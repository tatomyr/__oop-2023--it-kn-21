def apply_operation(x, y, operation):
    return operation(x, y)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

result = apply_operation(5, 7, add)
print(result) # Виведе 12

result = apply_operation(5, 7, multiply)
print(result) # Виведе 35
