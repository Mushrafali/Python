str1 = "This is a string. we are creating it in a python."
str2 = 'this is a string.\nwritten in single quotes'  # \n is used to go in next line
str3 = """This is a string.\twritten in tripple quotes"""  #\t is used to tab

print(str1)
print(str2)
print(str3)

#concatenation
str1 = "Mushraf"
str2 = "ali"
print(str1 + str2)

#length of string
str1 = "Mushraf"
len1 = len(str1)
print(len1)
str2 = "ali"
len2 = len(str2)
print(len2)
MyName = str1 + " " + str2
print(MyName) # or print(str1 + str2)
print(len(MyName))

#indexing
str = "Mushraf Ali"
ch = str[2]
print(ch) #print(str[2])

#slicing
str = "Mushraf Ali"  #0to11
print(str[0:4])  #print(str[:4])
print(str[4:len(str)]) #print(str[4:]) 

str = "Apple"  #-1to-5
print(str[-3:-1])

#String Functions
str = "i am studying python from ApnaCollege."

print(str.endswith("ege.")) #returs true if string ends with substr

print(str.capitalize()) #their is no change in old string
print(str)
#to make change
str = str.capitalize() #capitalizes 1st char
print(str)

print(str.replace("o", "a")) #replaces all occurrences of old
print(str.replace("python", "javascript"))

print(str.find("o")) #returns 1st index of 1st occurrer
print(str.find("python"))
print(str.find("Q")) #if their is no such letter it will return -1

print(str.count("o")) #counts the occurrences of substr