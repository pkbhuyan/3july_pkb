"""
string1='Praveen'
Str2="Kumar"
sTr3=""This is a paragraph.Written in the Macbook Air.
Using the Text Editor Atom ""

print (string1)
print (Str2[0:5]) # this is called slicing
print (Str2[0:])
print (len(sTr3))
print (sTr3[-1:]) # Nothing got printed but its not an error also
print (sTr3[:-1]) # this is called right to left indexing and names a string character starting from -1
print (sTr3[-50:-1])
print (Str2 *3) #it will repeat the word 3 times

print (sTr3[::3]) # this will display the words skipping every 2 letters in between

"""
var1 = "hello"
var2 = "World"
print(f"This text {var1 +' '+ var2} is printed using format operator ") # Format operator is used along with concatenation
print("this text", (var1 + var2), "is printed using normal concatenation" ) # Normal Concatenation operator is used

print("the value of var1 is %s and value of var2 is %s " %(var1,var2)) # % is used to display a form of printing of strings and is one the operators.
# %s is genearlly used for strings and %d is generally used for decimal indications.






