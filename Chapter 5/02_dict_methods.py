marks = {
    "Imran" : 100,
    "Shubham" : 56,
    "Rohan" : 23
}

print(marks, type(marks))
print(marks["Imran"])

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Imran": 99, "Manish": 69})
print(marks)

print(marks.get("Imran"))