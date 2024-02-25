def calculator():
    mistakes = 0
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator_choice = input("Choose an operation (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            mistakes += 1
            continue

        if operator_choice not in ('+', '-', '*', '/'):
            print("Invalid operator. Please choose +, -, *, or /.")
            mistakes += 1
            continue

        if operator_choice == '+':
            result = num1 + num2
        elif operator_choice == '-':
            result = num1 - num2
        elif operator_choice == '*':
            result = num1 * num2
        elif operator_choice == '/':
            if num2 == 0:
                print("Error: Division by zero.")
                mistakes += 1
                continue
            result = num1 / num2

        print(f"The correct result of {num1} {operator_choice} {num2} is: {result}")

        another_attempt = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_attempt != 'yes':
            break

    print(f"Calculation Over! You made {mistakes} mistake{'s' if mistakes != 1 else ''}.")
if __name__ == "__main__":
    calculator()
