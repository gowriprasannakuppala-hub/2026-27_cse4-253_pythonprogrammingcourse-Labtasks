def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Calling function with default rate
p = 10000
t = 2

print("Simple Interest with default rate:")
print(simple_interest(p, t))

# Calling function with explicit rate
print("Simple Interest with explicit rate:")
print(simple_interest(p, t, 10))