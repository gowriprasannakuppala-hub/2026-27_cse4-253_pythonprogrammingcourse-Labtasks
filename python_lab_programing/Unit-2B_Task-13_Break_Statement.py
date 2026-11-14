
# Demonstrate break statement using for loop

for i in range(1, 11):
    if i == 6:
        break
    print(i)

print("Loop terminated")


# Demonstrate break statement using while loop

i = 1

while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1

print("Loop terminated")
