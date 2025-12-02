friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends)

# list.append(8): adds "Imran" at the end of the list 
friends.append("Imran")
print(friends)

l1 = [1, 23, 62, 2, 6, 11]

# list.sort(): updates the list in ascending order
l1.sort()
print(l1)

# list.reverse(): updates the list in descending/reverse order
l1.reverse()
print(l1)

# list.insert(3,4444): This will add 4444 at 3 index
l1.insert(3, 4444)
print(l1)

# list.pop(2): Will delete element at index 2 and return its value.
l1.pop(2)
print(l1)

# list.remove(23): Will remove a particular value, 23 from this list
l1.remove(23)
print(l1)