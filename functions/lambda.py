# lambda function is used for only single statement argument/expression ,
# it doesnt take more than one argument/expression
# lambda function is also called anonymous function


# example 1
single_func = lambda x, y: print(x + y)

"""
Conversion of lambda function to normal function would be 

def single_func(x, y):
    return x + y

"""
single_func(34, 93)

# example 2 is just for analysis ,after defining print( ) inside the function,the function is not returning any value , as a result of which the print function in the calling statement will print NONE

single_func = lambda x, y: print(x + y)

print(single_func(34, 93))


