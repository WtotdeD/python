import re

number1 =""
number2 = ""
oper = ""



data=""
data = input("What is the calculation you want to execute: ")

print(data)

number1 = re.split('\+,-,/,^,%,\*', data)
print(number1)
