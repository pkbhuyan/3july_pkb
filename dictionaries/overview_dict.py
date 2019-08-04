
filename = {'firstname': 'Praveen', "MiddleName": "Kumar", 'LastName': "Bhuyan"}
qualif = {10: "Matriculation", 12: 'Intermediate', 16: "Engg"}

print(filename, qualif)

#  calling An element
print(filename['firstname'])  # elements inside the dictionaries are referred with the key name instead of the index value.

filename['middlename'] = 'k'  # instead of replaccing the value of Middlename , it inserted a new value as the key names were not matching
print(filename)

# del filename['middlename']  # particular element has been deleted.
print(filename)

filename['MiddleName'] = 'K'  # value updated
print(filename)

filename.update(qualif)  # both the dictionaries are merged inside dict filename
print(filename)

print(filename.keys())  # only keys of the dictionaries are called

print(filename.values())  # only values of the dictionaries are called

print(filename.items())  # all the items are displayed

print(dict(enumerate(filename)))  # each key of the dictionary is displayed with it its index

list1 = [1, "One", "its a list"]
print(dict.fromkeys(list1))  # A dictionary is created out of List with defualt values as none for every key

print(dict.fromkeys(list1, "YES"))  # dictionary created with default values as YES for every element of List

print(filename.setdefault(
    "firstname"))  # the function of setdefault is ir returns the value if the key is present in the dictionary
# otherwise ifthe ey is not there then it will return the default value mentioned in the method.
print(filename.setdefault('unknown_key', "unknown_value"))  # key was not there ,so it got created.
print(filename)

dict2 = filename.copy()  # the elements of Filename got copied to dict2
print(dict2, type(dict2))

dict.fromkeys(dict2, "Hello")
print(dict2.values())
print(dict2)

filename.clear()  # all the elements of the dictionary got cleared and the dictionary is empty now.
print(filename)
