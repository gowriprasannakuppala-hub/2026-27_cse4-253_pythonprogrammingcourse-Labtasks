# Example solution: count lines, words, characters
filename = "sample.txt"
with open(filename, "r") as file:
    text = file.read()

line_count = len(text.splitlines()) if text else 0
word_count = len(text.split())
char_count = len(text)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)