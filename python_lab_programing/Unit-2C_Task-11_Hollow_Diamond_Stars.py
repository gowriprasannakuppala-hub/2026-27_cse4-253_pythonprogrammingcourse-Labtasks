
# Print a hollow diamond pattern of stars

rows = int(input("Enter the number of rows: "))

# Upper half of the diamond
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half of the diamond
for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
