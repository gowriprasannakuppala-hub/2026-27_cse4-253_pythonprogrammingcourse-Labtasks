n = int(input("Enter a number: "))

reverse = 0
num = abs(n)

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if n < 0:
    reverse = -reverse

print("Reversed number =", reverse)