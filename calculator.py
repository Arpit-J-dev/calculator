def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    while True:
        print("\n--- Calculator ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            else:
                print("Invalid choice.")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
