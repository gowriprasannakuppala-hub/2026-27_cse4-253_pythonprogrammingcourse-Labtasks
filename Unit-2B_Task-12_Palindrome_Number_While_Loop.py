n = int(input("Enter a number: "))

original = n
reverse = 0
num = abs(n)

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original >= 0 and original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")