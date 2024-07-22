age = 21

if(age >= 18):
    print("can vote & apply for license")
    print("can drive")


light = "green"

if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")

print("End of code.")

num = 5

if(num>2):
    print("greater than 2")
if(num>3):  #if statement can be written multiple times and all will be checked
    print("greater than 3")
elif(num>4):  #if if statement is true then elif statement will not be checked
    print("greater than 4") 
    #elif can also be written multiple time but first their should be one if statement

light = "blue"

if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")

age = 14

if(age >= 18):
    print("can vote") #"indentation" means 4 spaces or tab before print
else:
    print("cannot vote") # in pyhton indentation is used instead of {}


# For Example

# marks>=90, grade = "A"
# 90>marks>=80, grade = "B"
# 80>marks>=70, grade = "C"
# 70>marks, grade = "D"

marks = int(input("enter students marks : "))

if(marks>=90):
    grade = "A"
elif(marks>=80 and marks<90):
    grade = "B"
elif(marks>=70 and marks<80):
    grade = "C"
else:
    grade = "D"

print("garde of the student ->", grade)

#nesting

age = 95

if(age>=18):
    if(age>=80):
        print("cannot drive")
    print("can drive")
else:
    print("cannot drive")