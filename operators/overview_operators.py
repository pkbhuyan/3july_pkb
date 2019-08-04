"""
Various operators:

1. Arithmatic Operators
2. Comparision(relational) Operators
3. Assignment Operators
4. Identity Operators
5. Logical Operators
6. Membership Operators
7. Bitwise Operators

1. Arithmatic Operators

+
-
*
/
%
//


var1 = 'Text1'
var2 = 'text2'
num1 = 50
num2 = 100
# Addition
print(var1+var2)
print(f"addition of Numbers {num1+num2}")

# Substraction
# print(var1-var2) Substraction is not supported
print(f"substraction of Numbers {num1-num2}")

# multiplication
# print(var1*var2) # not supported
print(f"multiplication of Numbers {num1*num2}")

# Division
# print(var1/var2) # Not Supported
print(f"Division of Numbers {num1/num2}") # Quotient is picked

# Modulus
print(f"Modulus of Numbers {num1%num2}") # remainder is picked before making the quotient float.

# floor division
print(f"Floor Division of Numbers {num1//num2}") # Quotient value before putting the decimal point

"""

"""
2. Relational operators

<
>
==
!=
<=
>=

var1 = 'Text1'
var2 = 'text2'
var3 = 'Text1'

num1 = 50
num2 = 100
NUM3 = 50

list1=[1,2,3]
list2=[5,6,7]
list3=[1,2,3]


# ==  # Matches By Value
print(f"The Operator == of var1 and var2 is {var1==var2}")
print(f"The Operator == of var1 and var3 is {var1==var3}")
print(f"The Operator == of num1 and num2 is {num1==num2}")
print(f"The Operator == of num1 and NUM3 is {num1==NUM3}")
print(f"The Operator == of list1 and list2 is {list1==list2}")
print(f"The Operator == of list1 and list3 is {list1==list3}")
print(f"The Operator == for tuples are {tuple(list1)==tuple(list3)}")
print(f"The Operator == for tuples are {tuple(list1)==tuple(list2)}")

# !=
print(f"The Operator != of var1 and var2 is {var1!=var2}")
print(f"The Operator != of var1 and var3 is {var1!=var3}")
print(f"The Operator != of num1 and num2 is {num1!=num2}")
print(f"The Operator != of num1 and NUM3 is {num1!=NUM3}")
print(f"The Operator != of list1 and list2 is {list1!=list2}")
print(f"The Operator != of list1 and list3 is {list1!=list3}")
print(f"The Operator != for tuples are {tuple(list1)!=tuple(list3)}")
print(f"The Operator != for tuples are {tuple(list1)!=tuple(list2)}")


"""




