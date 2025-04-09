# calculator.py

import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator(choice, num1, num2):
    if choice == '1':
        return add(num1, num2)
    elif choice == '2':
        return subtract(num1, num2)
    elif choice == '3':
        return multiply(num1, num2)
    elif choice == '4':
        return divide(num1, num2)
    else:
        return "Invalid operation"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <choice> <num1> <num2>")
        sys.exit(1)

    choice = sys.argv[1]
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Invalid number input")
        sys.exit(1)

    result = calculator(choice, num1, num2)
    print(f"The result is: {result}")

