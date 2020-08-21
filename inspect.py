from operator import add, sub, truediv, mul, pow
import inspect

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv 
}


inspect.getdoc(dict)