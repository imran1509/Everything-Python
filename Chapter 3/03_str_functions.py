name = "Imran is"

# len () function – This function returns the length of the strings.
print(len(name) )

# String.endswith("rry") – This function_ tells whether the variable string ends with
# the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends
# with rry
print(name.endswith("ana"))
print(name.startswith("im"))

# string.count("c") – counts the total number of occurrences of any character.
count = name.count("r")
print(count)

# the first character of a given string.
print(name.capitalize())

# string.find(word) – This function friends a word and returns the index of first
# occurrence of that word in the string.
index = name.find("is")
print(index)

# string.replace (old word, new word ) – This function replace the old word with
# new word in the entire string.
replaced_string = name.replace("I","i")
print(replaced_string)