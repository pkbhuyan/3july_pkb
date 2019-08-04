

str1 = "first set" # removes the duplicates and performs a set with different elements which is unordered
#print(set(str1))

# var1= 10203040 # set cannot be formed with integer value
# print(set(var1))

l1 = ['hello',19,3.5,'hello',19] # formation of set from list
#print(set(l1))

t1 = (890,'babu',920,'junior','babu') # formation of set from tuples
#print(set(t1))

d1 = {1:'one',2:'two',3:'three',4:'four',4:'four'} # formation of set from the dictionaries
# will only display the keys not values
#print(set(d1))

# methods of sets

set1= {'hello','this','is','my','world'}
set2= {'hello','Python','world',}
set3= {'hello'}
tuple1 = ('this_is_tuple','immutable_obj','hello')

print(set1.union(tuple1))
print(set1.intersection(set2))
print(set1.difference(set2)) # returns results similar to s1-s2
print(set1.issubset(set2)) # returns boolean if s1 is subset of s2
print(set1.issuperset(set3)) #returns boolean if s1 is superset of s3
print(set1.update(tuple1)) # values of set2 is merged with set1 ,update can take multiple elements.
print(set1)
print(set1.add('lonely_world')) # add can take only one element

# set1.discard(set1[2]) # doesnt Support slicing as the items are unordered.
set1.discard('hello') # element hello is discarded ,if item/member not found do nothing
print(set1)

print(set1.pop())
print(set1)

set1.remove('is') # remove an element if it is a member otherwise generate a key error
print(set1)

set4=set1.copy()
print(set4)

print(f'memory loc of set1 {id(set1)}')
print(f'memory loc of set4 {id(set4)}')

print(set1==set4) # matching the elements
print(set1 is set4) # matching memory location wise





