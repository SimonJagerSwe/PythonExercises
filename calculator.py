########## CALCULATOR ##########
int_a = int(input('Enter first integer: '))
operator = str(input('Enter operator: '))
int_b = int(input('Enter second integer: '))

##### FIRST VERSION #####
'''
def addition():
    return int_a + int_b

def subtraction():
    return int_a - int_b

def multiplication():
    return int_a * int_b

def division():
    return int_a / int_b

if operator == '+':
    print(addition())

elif operator == '-':
    print(subtraction())

elif operator == '*':
    print(multiplication())

elif operator == '/':
    print(division())
'''

##### SECOND VERSION #####
def calculator():
    if operator == '+':
        return int_a + int_b
    elif operator == '-':
        return int_a - int_b
    elif operator == '*':
        return int_a * int_b
    elif operator == '/':
        return int_a / int_b
    
print(calculator())