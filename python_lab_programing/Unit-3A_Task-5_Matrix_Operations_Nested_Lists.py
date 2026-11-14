
# Matrix Operations Using Nested Lists

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Read first matrix
print("Enter elements of first matrix:")
A = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

# Read second matrix
print("Enter elements of second matrix:")
B = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    B.append(row)

# Matrix Addition
add = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    add.append(row)

# Matrix Subtraction
sub = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] - B[i][j])
    sub.append(row)

# Matrix Multiplication (Element-wise)
mul = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] * B[i][j])
    mul.append(row)

# Display results
print("Matrix Addition:")
for row in add:
    print(row)

print("Matrix Subtraction:")
for row in sub:
    print(row)

print("Matrix Multiplication (Element-wise):")
for row in mul:
    print(row)
