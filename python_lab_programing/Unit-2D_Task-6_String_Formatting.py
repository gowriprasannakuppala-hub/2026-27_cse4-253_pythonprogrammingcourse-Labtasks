# Student details
name = "Gowri"
age = 18
marks = 95.5

# Using format() method
print("Using format():")
print("My name is {} and my age is {}.".format(name, age))

# Using f-strings
print("\nUsing f-strings:")
print(f"My name is {name} and my age is {age}.")

# Using % operator
print("\nUsing % operator:")
print("My name is %s and my age is %d." % (name, age))

# Formatting floating-point number
print("\nMarks: {:.2f}".format(marks))
print(f"Marks: {marks:.2f}")
print("Marks: %.2f" % marks)