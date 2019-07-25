
# Methods related to upper case and letter case
'''
print(code1.capitalize()) # capitalise the first word of a string
print(code1.upper()) # Capitalise each and every letter of a string
print(code2.lower()) # Make all the upper case letter lower
print(code1.swapcase()) # Make the capital letters small and small letters capital
print(code2.swapcase()) # Make the capital letters small and small letters capital
print(code1.title()) # Make the first letter for all the words of a string capital
print(code1.isupper()) # returns true or false
print(code2.islower()) # returns true or false
'''

# Methods
"""
print(code2.isdigit()) # checks whether the string is a number or not
print(code3.isdigit()) # true
print(code3.isdecimal()) # checks whether the unicode string is decimal or not
# unicode is declared by prefixing the string with the letter u
print(code3.isnumeric()) # applies on unicode string
#need to find out the difference between isnumeric( ) and isdigit()
#isdigit() only recognises digits(0-9) and nothing else
#isnumeric() recognises digits(0-9) and digits from other languages also like numerics from chinese,arabic etc .So its better to stick to 
isdigit() for english digits only. 
#fractions will be accepted by numeric and by no other function
print('-123'.isnumeric()) #False
print(u'123.123'.isdecimal()) #false because it is a floating point ,isdecimal()returns true if the string is purely decimal.
# isdecimal()returns true if string is purely decimal
print('123**3'.isdecimal()) #power function will not be accepted as decimal.
print(code1.find('world')) # find the index of a desired sub-string inside a string
print(code1.find('hello')) # returns -1 if the string is not present instead of giving error



print(code1.index('coding')) # gives error if the substring is not present in the main string
print(code1.rindex('coding')) # gives highest index of the subsring same like rfind()
# difference between the index and find is one gives error and the other returns -1
#print(code2.index('WORLD'))
"""
code1 = "welcome to coding world of coding"
code2 = "CODING WORLD"
code3 = "     420    "
code4= "     @420@   "
code5= "this is a program written in pycharm using a Macbook Air \n" \
       "Written by Praveen Kumar Bhuyan \n" \
       "sitting inside a room \n" \
       "located in Ghana" \
       "far from home" \
       "staying alone" \
       "enjoying his bhusi chia seeds drink"


print(code1.rfind('coding')) # returns highest index of the substring
print(code1.find('coding')) # returns index of the first occurrence of the substring
print(code1.replace('world','Duniya')) # replaces old string with desired string
print(code1.count('o')) # counts the total number of occurrences of substring inside a main string
print(code2.ljust(len(code2)+5,'@')) # ljust inserts at the right
print(code2.rjust(len(code2)+5,'@')) # rjust inserts at the left

print(len(code3))
print(len(code3.strip())) # removes extra spaces and any character if specified
print(code4.strip('0')) # removes either spaces or characters that are present on either side of the string
print(len(code3.lstrip()))
print(len(code3.rstrip()))

print(code2.split())
print(code1.split('o')) # splits the string based on the character provided or splits by space by default and returns a list
print(code1.rsplit('o',2)) # splits from the right hand side but only for first 2 occurrences of the char mentioned
print(code5.splitlines()) # split the lines based upon the newline escape character
