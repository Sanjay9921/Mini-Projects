from art import *
from functions import *

end = False

print(logo)
while not end:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operation: '+', '-', '*' or '/': ")

    sc = SimpleCalculator(a,b)
    result = None
    if op=="+":
        result = sc.add()
    elif op=="-":
        result = sc.subtract()
    elif op=="*":
        result = sc.multiply()
    else:
        result = sc.divide()

    print(f"{a} {op} {b} = {result}")

    choice = input("Do you wish to continue ? 'Y' or 'N'").casefold()
    if choice=="n":
        print("Thank you for using our software !")
        end = True