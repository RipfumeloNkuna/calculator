# simple_calculator.py

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    print("Type 'q' to quit.")

    while True:
        op = input("\nEnter operation (+, -, *, /): ")

        if op.lower() == 'q':
            print("Goodbye!")
            break

        if op not in ['+', '-', '*', '/']:
            print("Invalid operation. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero.")
                continue
            result = num1 / num2

        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
