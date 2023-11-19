import random
import string

while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        if length > 0:
            break
        else:
            print("Please enter a positive integer for password length.")
    except ValueError:
        print("Please enter a valid integer for password length.")

print("Select complexity level:")
print("1. Letters (lowercase and uppercase)")
print("2. Letters and Digits")
print("3. Letters, Digits, and Punctuation")

while True:
    complexity = input("Enter complexity level (1/2/3): ")
    if complexity in ('1', '2', '3'):
        break
    else:
        print("Invalid complexity level. Please enter a valid choice (1/2/3).")

if complexity == '1':
    characters = string.ascii_letters
elif complexity == '2':
    characters = string.ascii_letters + string.digits
elif complexity == '3':
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid complexity level. Using default complexity.")
    characters = string.ascii_letters + string.digits

password = ''.join(random.choice(characters) for _ in range(length))

print(f"Generated Password: {password}")
