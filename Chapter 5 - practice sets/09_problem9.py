# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}

# No, you cannot put a list inside a set so you cannot change its values either.

# ❌ Why?

# In Python:

# Set elements must be immutable (hashable).

# Lists are mutable, so they are not hashable.

# Therefore, something like this will throw an error: