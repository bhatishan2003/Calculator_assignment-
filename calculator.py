class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Number cannot be divided by 0")
        return a / b
    
    def exponential(self , a ,b):
        return a**b
    
    def modulo(self , a ,b):
        return a % b

calc = Calculator()

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")

    choice = input("Enter choice from (1-7): ")

    if choice == '7':
        print("Exiting...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(f"Result: {calc.add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {calc.subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {calc.multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {calc.divide(num1, num2)}")
    elif choice == '5':
        print(f"Result: {calc.exponential(num1, num2)}")
    elif choice == '6':
        print(f"Result: {calc.modulo(num1, num2)}")
    else:
        print("Invalid input. Please choose a number between 1 and 7.")

