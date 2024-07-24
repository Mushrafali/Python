#Dictionary in Python = unordered, mutable(changeable) & don't allow duplicate keys

info = {
    "name" : "Mushrafali",
    "subjects" : ["python", "C", "Java"],
    "topics" : ("dict", "set"),
    "age" : 24,
    "is_adult" : True,
    "marks" : 94.4,
    556.12 : 91
}

print(info)
print(type(info))
print(info["name"])
print(info["topics"])

info["name"] = "Ashraf"  #to change the value
info["surname"] = "Momin"  # to add new key and value pair
print(info)

null_dict = {}
null_dict["name"] = "Mushraf"
print(null_dict)


#Nested Dictionaries

student = {
    "name" : "Momin",
    "subjects" : {
        "phy" : 62,
        "chem" : 66,
        "math" : 95
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

#Dictionary Methods

# myDict.keys()  #returns all keys
# myDict.values()  #returns all values
# myDict.items()  #returns all (key, val) pairs as tuples
# myDict.get("key")  #returns the key according to value
# myDict.update(newDict)  #inserts the specified items to the dicrionaries