def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDNG {a} / {b}")
    return a / b

print("Let's do some math with this functions!")

age = add(20, 4)
height = subtract(200, 30)
weight = multiply(12, 5)
iq = divide(200, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle...")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"That becomes: {what}. Can you do it by hand?")
