# Read a string from the user
string = input("Enter a string: ")

# Create an empty dictionary
frequency = {}

# Count the frequency of each character
for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# Display the character frequencies
print("Character frequencies:")
for ch, count in frequency.items():
    print(ch, ":", count)