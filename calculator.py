
""" 
Creating a calculator using the def function
To carry out 7 basic arithmetic operations.
addition, subtraction, multiplicatin, division, modulus, power, floor-division.
"""

# using def function

def add(a,b):                # ADDITION
    return a + b 

def subtract(a,b):           # SUBTRACTION
    return a - b

def multiply(a,b):           # MULTIPLICATION
    return a * b

def divide(a,b):             # DIVISION
    return a / b

def modulus(a,b):            # MODULUS
    return a % b

def power(a,b):              # EXPONENTIATION
    return a ** b

def floordivision(a,b):      # FLOOR DIVISION
    return a // b  


print('SELECT OPERATOR')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('5. Modulus')
print('6. Power')
print('7. Floordivision')


# Accept input from user
choice = input('Enter your choice (1/2/3/4/5/6/7): ')
num_1 = float(input('Enter first number: '))
num_2 = float(input('Enter second number: '))

if choice == '1':
    print(num_1, "+", num_2, "=", add(num_1,num_2))
elif choice == '2':
    print(num_1, "-", num_2, "=", subtract(num_1,num_2))
elif choice == '3':
    print(num_1, "*", num_2, "=", multiply(num_1,num_2))
elif choice == '4':
    print(num_1, "/", num_2, "=", divide(num_1,num_2))
elif choice == '5':
    print(num_1, "%", num_2, "=", modulus(num_1,num_2))
elif choice == '6':
    print(num_1, "**", num_2, "=", power(num_1,num_2))
elif choice == '7':
    print(num_1, "//", num_2, "=",floordivision(num_1,num_2))
else:
    print('Invalid')
        

    
    