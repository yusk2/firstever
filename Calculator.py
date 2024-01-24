def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print('Choose operation:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

while True:
    choice = input('Select your operation (1/2/3/4): ')

    if choice not in ('1', '2', '3', '4'):
        print('Invalid choice. Exiting.')  # Basically, if the user didn't input 1, 2, 3 or 4, the program would stop
        break                              # running.

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Invalid input. Please enter a number.")  # If the user did not input a valid number, the program would
        continue                                        # tell you to input a valid number.

    if choice == '1':
        print(num1, '+', num2, '=', add(num1, num2))
    elif choice == '2':
        print(num1, '-', num2, '=', subtract(num1, num2))
    elif choice == '3':
        print(num1, '*', num2, '=', multiply(num1, num2))
    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero.")  # if the second number was 0, the program would tell you it can't divide
        else:                                # by 0.
            print(num1, '/', num2, '=', divide(num1, num2))

    next_calculation = input('Do you want to perform another calculation? (yes/no): ')
    if next_calculation.lower() != 'yes':  # if you chose anything different from "yes", the program would stop working.
        break
