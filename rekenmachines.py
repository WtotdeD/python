#Methode

number1 = input("First number?\n")
number2 = input("Second number?\n")
Operator = input("What is the operator?\n")

number1 = float(number1)
number2 = float(number2)
out = None

if Operator == "*":
   out = number1 * number2

if Operator == "%":
   out = number1 % number2

if Operator == "/":
   out = number1 / number2

if Operator == "-":
   out = number1 - number2

if Operator == "+":
   out = number1 + number2


print("Answer is: " + str(out))


#option 2 is with eval
#Posseses scuirty risk 
#link https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html

calc = input("Type calculation:\n")
    
print("Answer: " + str(eval(calc)))



#Option 3
from operator import add, sub, truediv, mul, pow

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv 
}


def calculate(s):
   if s.isdigit():
      return float(s)
   for o in operators.keys():
      left, operator, right = s.partition(o)
   if operator in operators:
      return operators[operator](calculate(left),calculate(right))


reken = input("What is your calculation?:\n")
print("Answer is:" + str(calculate(reken)))