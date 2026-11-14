
# Remove Duplicates from a List Using Sets

# Create a list
my_list = [10, 20, 30, 20, 40, 10, 50, 30]

print("Original List:", my_list)

# Convert list into a set
unique_set = set(my_list)

# Convert set back into a list
new_list = list(unique_set)

# Display the result
print("List after removing duplicates:", new_list)

