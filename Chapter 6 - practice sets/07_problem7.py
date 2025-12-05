# Write a program to find out whether a given post is talking about “Imran” or not.

post = input("Enter the post: ")

if("Imran".lower() in post.lower()):
    print("This post is talking about Imran")

else:
    print("This post is not talking about Imran")

