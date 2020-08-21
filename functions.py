def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))


# Modify this function to return a list of strings as defined above
def list_benefits():
    pass

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    pass

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()