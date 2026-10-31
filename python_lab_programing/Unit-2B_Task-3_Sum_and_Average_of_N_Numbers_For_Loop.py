total_input_numbers = int(input("Enter how many numbers: "))
total_sum = 0

for i in range(total_input_numbers):
    num = float(input("Enter a number: "))
    total_sum = total_sum + num

average = total_sum / total_input_numbers

print(f"Sum of {total_input_numbers} numbers is {total_sum}")
print(f"Average of {total_input_numbers} numbers (sum {total_sum}) is {average}")