#List&Tuple

#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

movies = []
mov1 = (input("enter 1st movie : "))
mov2 = (input("enter 2st movie : "))
mov3 = (input("enter 3st movie : "))
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# movies = []
# mov = (input("enter 1st movie : "))
# movies.append(mov)
# mov = (input("enter 2st movie : "))
# movies.append(mov)
# mov = (input("enter 3st movie : "))
# movies.append(mov)
# print(movies)

# movies = []
# movies.append(input("enter 1st movie : "))
# movies.append(input("enter 2st movie : "))
# movies.append(input("enter 3st movie : "))


#WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
# palindrome means from starting or ending it will be same [1, 2, 3, 2, 1]  [1, "abc", "abc", 1]

list1 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")


#WAP to count the number of students with the "A grade in the following tuple."
  # ["C", "D", "A", "A", "B", "B", "A"]

grade = ["C", "D", "A", "A", "B", "B", "A"]
print(grade.count("A"))


#Store the above values in a list & sort them from "A" to "D".

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)