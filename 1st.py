print('Hello from python')
# """
# Python Indentation
# Indentation refers to the spaces at the beginning of a code line.
# Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
# Python uses indentation to indicate a block of code.
# """

if 5 > 2:
  print("Five is greater than two!") #use 3  spaces to indent (number not really important as long as it's more than 1, BUT MUST BE THE SAME NUMBER EACH TIME)

#   python variables: in python variables are created when you assign a value to it
x = 5 #int
y = 'Hello, World!' #str str variables can be written with single  or double quotes
z = 3.0 #float

#you can get the data type of a variable with the type() function

a = 5 
b = "John"

print(type(a)) #class int
print(type(b)) #class str


#variable names are case-sensitive. age and Age and AGE are NOT the same
#variable names must start with letter or underscore, cannot start with number but can contain number
#can contain only alphanumeric characters and underscores 
#no kebab case,
#  can use camel case myVariable, pascal case MyVariable, snakecase my_variable_name


#python allows you to assign multiple variables in one line
d, e, f, = 'orange', 'banana', 'cherry'
print(d)
print(e)
print(f)

#python also allows you to assign the same value to multiple variables in one line
g = h = i = 'pineapple'
print(g)
print(h)
print(i)

fruits = ['kiwi', 'strawberry', 'watermelon']
j, k, l = fruits
print(j)
print(k)
print(l)