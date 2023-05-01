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

#concat
m = 'awesome'
print('python is ' + m)

n = 'python is '
o = 'awesome'
p = n + o
print(p)

#but in python + adds int
q = 5
r = 10
print(q + r)

#global variables are created outside of a function and can be used by everything inside and  outside of functions
s = 'intersting'
def myfunc():
  print('Python is ' + s)

myfunc()
#varible created inside of functions are only available in the function
#even if same name for two functions inside and outside of function, the one inside 
#the function can only be used inside the function and the global variable will remain as it was 
#with its original value
t = 'global'
def myfunc2():
   t = 'local'
   print('This variable is ' + t)

myfunc2()

print('This variable is ' + t)
