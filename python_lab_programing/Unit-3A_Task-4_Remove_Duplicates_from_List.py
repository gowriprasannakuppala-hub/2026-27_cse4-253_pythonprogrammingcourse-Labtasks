
# Matrix Operations using Nested Lists

# Read number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Read first matrix
print("Enter elements of first matrix:")
A = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    A.append(row)

# Read second matrix
print("Enter elements of second matrix:")
B = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    B.append(row)

# Matrix Addition
addition = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    addition.append(row)

# Matrix Subtraction
subtraction = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] - B[i][j])
    subtraction.append(row)

# Matrix Multiplication (element-wise)
multiplication = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] * B[i][j])
    multiplication.append(row)

# Display matrices
print("\nFirst Matrix:")
for row in A:
    print(row)

print("\nSecond Matrix:")
for row in B:
    print(row)

print("\nMatrix Addition:")
for row in addition:
    print(row)

print("\nMatrix Subtraction:")
for row in subtraction:
    print(row)

print("\nElement-wise Matrix Multiplication:")
for row in multiplication:
    print(row)
