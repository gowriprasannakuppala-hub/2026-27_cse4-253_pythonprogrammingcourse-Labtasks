# Read a string from the user
string = input("Enter a string: ")

# Initialize counters
vowels = 0
consonants = 0
digits = 0
spaces = 0

# Check each character
for ch in string:
    if ch.isalpha():
        if ch.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == ' ':
        spaces += 1

# Display the results
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)