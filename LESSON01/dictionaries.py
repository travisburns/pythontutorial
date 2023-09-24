band = {
    "vocals": "Plant",
    "guitar": "page"
}

band2 = dict(voals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

#Access items 
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#list of key/value pairs as tuples
print(band.items())

#varify a key exits 
print("guitar" in band)
print("triangule" in band)

#change values
band["vocals"] = "Coverdale"
band.update({"bass" : "JPJ"})

print(band)


#Remove items
print(band.pop("bass"))
print(band)


band["drums"] = "Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

#delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2 

#copy dictionaries 
# band2 = band # create a reference 
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band2 = dict(band)
print("Good copy!")


#NEsted dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}


band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])


# sets 

nums = { 1, 2, 3, 4 }

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#No duplicates allowed
nums = { 1, 2, 2, 3 }
print(nums)

# True is dupe of 1, False is a dupe of zero

nums = {1, True, 2, False, 3, 4, 0}
print(nums)
