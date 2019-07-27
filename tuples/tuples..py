# tuples is an immutable object that means items present inside cannot be reassigned.
# represented with ( )

# various ways of Creating tuples.

tup1 = ( )
print(tup1, type(tup1),len(tup1))

tup2 = (1,) # comma has to be incorporated otherwise it will be treated as integer.
print(tup2, type(tup2))

tup3 = 1,
print(tup3)

tup4 = 44, 55, 66, 77, 88
print(tup4)

tup7="""a""","""b""","""z"""
print(tup7)

tup8='''x''','''y''','''bang'''
print(tup8)

tup5 = tup1 + tup2, "Hello",50,3.6  #concatenation is done of two tuples and added to another tuple as an element
print(tup5,type(tup5))
print(tuple(enumerate(tup5))) # used to print the tuple elements index wise

# tup4[2]= 99 # No item assignment
# print(tup4)

# del tup4[3] # tuple doesnt support item deletion
# print(tup4)

# list will be taken as tuple and tuple will be taken as list.
# conversion

list1 = ['hello','Python','world',4.7 ,'$']
print(list1)
tup6=tuple(list1)
print(tup6) # list converted to tuple

list2=list(tup6)
print(f"The list after convesion :{list(list2)}")

print(min(tup4)) # min value among the tuple
print(max(tup4)) # max value among the tuple

print(len(tup6)) # length of the tuple

print(tup4[:3]) # slicing


# strings,tuples are immutable object
# list and dictionaries are mutable object




