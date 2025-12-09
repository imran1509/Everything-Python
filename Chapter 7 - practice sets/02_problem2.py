'''
Write a program to greet all the person names stored in a list ‘l’ and which starts
with S.
l = ["Imran", "Soham", "Sachin", "Rahul"]
'''

l = ["Imran", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")