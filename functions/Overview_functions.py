# Normal Function

def func1():
    print("This is Function 1")
    return


func1()
print("Ending of function1")


# function with required length Argument
def func2(arg1):
    print(f"The value passed onto Function 2 is {arg1}")
    return


func2(999)

# function with Keyword argument
"""
# The Function Arguments has to be same name to that of calling arguments
def func3(group, position): 
    print("Company : %s " % company, end='\n')
    print("Title : %s" % title)


func3(title="stallion Group", company="IT MANAGER")

"""


def func3(company, title):
    print("Company : %s " % company, end='\n')
    print("Title : %s" % title)


print("In function 3")
t1 = "IT Officer"
c1 = "MICROSOFT"
func3(title="stallion Group", company="IT MANAGER")
# func3(title="stallion Group", "IT MANAGER") # Will give error as the value without
# keyword argument has to be passed first.
func3("DANO Group", "IT Assistant")  # will take the arguments without any keyword
# but has to be passed in the same order.
func3(c1, t1)

print("function 3 end")

# function with unlimited/variable length arguments

print("Function 4 Start")
def func4(title, *name):
    print("beginning of func4", end='\n')
    print(" \n")
    for k in name:
        # print(f"Part {k} of names: {name[k]}") # here K itself is the value
        # but we are trying to take the k as index, that's why the error is generating
        print(f"The value passed at index {name.index(k, 0, len(name))} is {k}")
    print("ending of func4", end='\n')
    return


func4('BUNCH OF FOLKS', 'Praveen', 'Gaurav', 'Rajiv', 'Ali')
print('\nThats it')
print("Function 4 End")


# function with default arguments

def func5(name, net_worth="less than 1 Cr"):
    print("function 5 started")
    print(f"The networth of {name} is {net_worth}")
    return


# func5(input('Enter your name'),input("Net worth")) # in this case the default argument will not be printed as
func5(input('Enter your name'))
print("function 5 end")

# function with variable keyword arguments
print("Function 6 started")
def func6(title, **name):
    print("beginning of func6", end='\n')
    print(" \n")
    print(name)
    for k in name:
        print(f"The value passed at index {k} is {name[k]}") # In this case the passed values are stored as key-value pair(as a dictionary ,
        # so no indexes, k is acting as key
    print("ending of func4", end='\n')
    return


func6('BUNCH OF FOLKS', rank1='Praveen',rank2='Gaurav', rank3='Rajiv',rank4='Ali')
print('\nThats it')
print("Function 6 End")

