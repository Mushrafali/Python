#List
marks = [91.5,92.6,95.8,65.6,48.9]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
print(len(marks))

student = ["karan", 95.5, 17, "delhi"]
print(student[0])
student[0] = "arjun" #allowed in python
# Lists -> mutable (changes can be done) while str -> unmutable
print(student)
# print(student[5]) #it will return error bc list index out of range

#List Slicing
#similar to string slicing

marks = [87,64,33,95,76]
print(marks[1:4])
print(marks[:4]) #[0:4]
print(marks[1:]) #[1:len(marks)]
print(marks[-3:-1]) #is [33, 95]

#List Methods (Functions)
# list = [2,1,3]
# list.append(4) #adds one element at the end   [2,1,3,4]
# list.sort() #sorts in ascending order  [1,2,3]
# list.sort( reverse = True )  #sorts in descending order [3,2,1]
# list.reverse() #reverses list  [3,1,2]
# list.insert( idx, el )  #insert element at index
# list.remove(1) #removes first occurrence of element  [2,3]
# list.pop( idx ) #removes element at idx

list = [2,1,3]
print(list.append(4)) #it will make the changes but will show NONE will not return anything
print(list)
list.sort() #print(list.sort) -> NONE
print(list)

list = ["banana","litchi", "apple"]
list.sort(reverse=True)  #["litchi", "banana", "apple"]
print(list)

list = ["b", "f", "a", "j", "l", "u"]
list.sort()  #['a', 'b', 'f', 'j', 'l', 'u']
list.reverse()  #['u', 'l', 'j', 'f', 'b', 'a']
print(list)

list = [2, 1, 3]
list.insert(1, 5)  #will insert 5 on 1st index [2, 5, 1, 3]
print(list)

list.remove(1)  #removes 1 from the list [2, 5, 3]
list.pop(2)  #delete the index [2, 5]
print(list)

# search python documentation on google for more..

#Tuples in python
# A built-in data type lets us create immutable sequences of values.

# tup = (87, 64, 33, 95, 76)  #tup[0], tup[1]..
# tup[0] = 43  #not allowed in pyhton

tup = (2, 1, 3, 1)
print(type(tup))
print(tup[0])

tup = ()
print(tup)  # we can also print empty tuple
print(type(tup))

tup = (1,)
print(tup)  # in single value tuple "," must be added else it will count in integer
print(type(tup))