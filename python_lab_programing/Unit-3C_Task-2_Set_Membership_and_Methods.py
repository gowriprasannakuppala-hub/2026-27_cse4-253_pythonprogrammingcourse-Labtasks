
# Set Membership Testing and Methods

# Create a set
my_set = {10, 20, 30, 40, 50}

print("Original Set:", my_set)

# Membership Testing
print("Is 20 present in set?", 20 in my_set)
print("Is 60 present in set?", 60 in my_set)

# Add an element
my_set.add(60)
print("After add(60):", my_set)

# Remove an element
my_set.remove(30)
print("After remove(30):", my_set)

# Discard an element
my_set.discard(40)
print("After discard(40):", my_set)