list1=['hello','hello','this','is','a','list',420,2.5]
list2=['a','b','c']
list3=['x','y','z']

# print(list1.count('hello')) # counts a particular substring inside a string
"""
# Insert & extend & append

list1.extend(list2)  # adds the elements of other list as the element of current string but at the end
print(list1)

list1.insert(0,'my dear')  # inserts a substring at a particular location
print(list1)

list1.insert(0,list2)  # inserts anything but like a element ex:here the whole list has been inserted as an element of list1
print(list1)

list1.append(list3)  # append() adds the elements at the end of a list ex:here the whole list has been inserted as an element of list1
print(list1)

list1.append('ends here')
print(list1)
"""
'''
print(list1)

value=list1.pop(3)  # pop removes element by index (from a desired place) irrespective of their value in a list and returns it.
print(list1)
print(f"The value of element popped out is '{value}' ")

list1.remove(list1[3])  # removes element by value irrespective of their index
print(list1)
# slicing is not supported in remove

list1.remove('hello')  # removes value from list depending on first matching value
print(list1)

del list1[:3]
print(list1)

var2 = min(list1)  # finds the minimum among the elements in the list and returns it (values are calculated according to its ASCII value)
print(var2)
var3 = max(list1)  # finds the maximum among the elements in the list and returns it (values are calculated according to ASCII Value)
print(var3)
'''
print(list2.index('c'))  # finds the index of the element in the list
#print(list2.index('d')) # it will give value error as the value is not in the list

print(list3.count('hello'))
print(list1.count('hello')) # counts the element mentioned inside the list

list1.reverse() # used to reverse the elements of the list
print(list1)

list2.sort(reverse=True)  # used to sort the elements in the ascending order. sort(reverse) is used to sort in descending order.
print(list2)










