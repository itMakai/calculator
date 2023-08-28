def add(x, y):
    return x+y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def division(x, y):
    if y == 0:
        return "cannot divide by zero"
    return x / y
print("select operator: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operator = input("enter operator (1/2/3/4): ")
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

if operator == '1':
    print("your answer is: ", add(num1, num2))
elif operator == '2':
    print("your answer is: ", subtract(num1, num2))
elif operator == '3':
    print("your answer is: ", multiply(num1, num2))
elif operator == '4':
    if num2 !=0:
        print("your answer is: ", divide(num1, num2))
    elif num2 == 0:
           print("no division with zero")
else:
    print("invalid operator")
             
