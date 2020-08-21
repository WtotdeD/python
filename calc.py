#Some calculations
print( 1 + 2)
print(7 ** 2)
print( 7 *2)
print(11 % 2) 

#Some operators
helloworld = "hello" + "" + "World"
print(helloworld)

#working with lists and operators
even = [2,4,6,8,10]
uneven = [1,3,5,7,9,11]
all_number = even + uneven
print(all_number)
#you can multiplyl lists
print(all_number * 3)

#strings formatting, even tough 29 is integer it needs to formatted as string %s
name = "Wouter"
age = 29
print("His name is %s and he is %s years old." % (name,age))
print("His name is %s and he is %d years old."  % (name,age))


#Unfortunately, this kind of formatting isn’t great because it is verbose and leads to errors, 
#like not displaying tuples or dictionaries correctly. Fortunately, there are brighter days ahead

#Better method is to use string format for readabillity
name = "Wouter"
age = 29
print("His name is {} and he is {} years old.".format(name,age))
print("His name is {name} and he is {age} years old.".format(name=name,age=age))

#Also called “formatted string literals,” f-strings are string literals that have an f at the beginning 
#and curly braces containing expressions that will be replaced with their values.
#Cleanest way to do this
print(f"His name is {name} and he is {age} years old.")


#Now some basic operation with
astring = "12345678!"
print(astring.index("1"))
print(astring.count("l"))
#slicing
print(astring[3:7])
print(astring[:3])
print(astring[7:])
print(astring[3:7:2])
print(astring[1:15:2])
print(astring[::-1])
print(astring[::-2])
print(astring[5::-2])