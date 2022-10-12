#Numeric Data Types
var = 3
print("Data Type of var: ", type(var))

var = 4.5
print("Data Type of var: ", type(var))

var = 8 + 2j
print("Data Type of var: ", type(var))

#String Data Type
string_var = 'Hello World'
print(string_var)

string_var1 = "Hello World,"
string_var2 = "\nI would like to learn Python language"
string_var = string_var1 + string_var2
print(string_var)

string_var: str = 'Hello World'
print(string_var)

string_var: str = 'Hello World'
print(type(string_var))

string_var = string_var.split(' ')
print(string_var)
print(type(string_var))

#List Data Type
string_var: str = 'Hello World'
list_var: list = string_var.split(' ')
print(list_var)
print(type(list_var))

list_var1 = []
list_var2 = [1, 2, 3, 4]
list_var3 = ["Hello", "World"]
list_var = list_var1 + list_var2 + list_var3
print(list_var)

list_var = []
list_var.append(list_var3)
list_var.append(list_var2)
print(list_var)
