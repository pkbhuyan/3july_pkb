# for integer  int() is used
# for floating point values float() is used

vari = 111
varf = 123.123
varn = -999.999
varr= 9+3j # complex variable generally used while doing predictions in the programs,
#this variable has two parts one is real and the other is imaginary part.
# Imaginary part of the Complex variables are always represented as j or J.
print( f"the varr is of type ",isinstance(varr,complex)) # isinstance method is a buit-in method to display whether the variable is complex or not.

print((type(vari))) # by default a value is defined as integer
print(int(vari))
print(float(vari))
fl=float(input()) # AS input value is received as string float method is applied for converting into float 
#and then typecasting is done with integer
print("the integer value of the float entered is %d" %(int(fl)))

import math
print(math.fabs(vari))
print(math.fabs(varn)) # returns absolute value 
print(math.ceil(varf)) # returns round up value
print(math.floor(varf)) # returns round down value
print(math.modf(varf)) # displays integer and fractional value seaparately in the form of tuple.
print(math.exp(2)) # e raised to the power of 2
print(math.sqrt(16)) #square root
print(math.pow(4,2)) # power value
print(4**2) # power vlaue



