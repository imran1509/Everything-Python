a = (1, 2, 5, 6, "Imran", False, "Rohan")
print(a)
print(type(a))

# a.count (5): a.count (5) will return number of times 5 occurs in `a`

no = a.count(5)
print(no)

# a.index (1) will return the index of first occurrence of 1 in `a`.

i = a.index(1)
print(i)

i = a.index("Imran")
print(i)

print(len(a))