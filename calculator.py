# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display operation choices
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    if choice == '1':
        result = num1 + num2
        operator = '+'
    elif choice == '2':
        result = num1 - num2
        operator = '-'
    elif choice == '3':
        result = num1 * num2
        operator = '*'
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operator = '/'
        else:
            result = "Cannot divide by zero."
    
    print(f"{num1} {operator} {num2} = {result}")
else:
    print("Invalid input. Please enter a valid choice (1/2/3/4).")
