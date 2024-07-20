print("My name is  Mushrafali.", "I am 23 years old.")
print("This is my first program in python.")
print(23)
print(12+89)

# variables

name = "mushrafali"
age = 23
price = 99.9

print(price)
print(age)
print("My name is", name)

age2 = age

print(age2)


# datatypes

print(type(name))   #String
print(type(age))    #Integer
print(type(price))    #Float

a = False
b = None

print(type(a))   #Boolean
print(type(b))   #None

# arithmetic operators

a = 1000
b = 54

sum = a + b
diff = a - b
print(sum)
print(diff)
print(a / b)
print(a * b)
print(a % b) #reminder
print(a ** b) #a^b

# relational / comparison operators

print(a == b)  #False
print(a != b)  #True
print(a >= b)  #True
print(a > b)  #True
print(a <= b)  #False
print(a < b)  #False

# assignment operators

num = 20
num += 10 #num = num + 10 = 30
num -= 10 #num = num - 10 = 20
print("num :", num) 

num *= 10 #200
print("num :", num)

num /= 10 #20
print("num :", num)

num **= 10 #20
print("num :", num)

num %= 10
print(num) #0

# logical operators
a = 50
b = 30
print(not False) #True
print(not (a>b)) #False

val1 = True
val2 = False
val3 = True
print("AND operator :", val1 and val2) #False bc both are diff values
print("OR operator :", val1 or val2) #True bc one of them is true
print("OR operator :", (a == b) or ( a > b )) #True

# type conversion
a = 2
b = 4.23
print(a + b) #2.0 + 4.23 => 6.23

# type casting
a = int("2") #"2" is a string which cannot be added with float or int so we have to change its type first
b = 4.2
print(type(a))
print(a + b) #6.23

a = 3.14
a = str(a)
print(type(a))

#input
name = input("Enter your name :")
print("WELCOME ", name)

















# single line comments
"""
multiple 
line comments
"""