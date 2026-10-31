#python program to calculate monthly income, total expenses and savings 
monthly_income=int(input("enter the monthly income:"))
rent=int(input("enter the rent:"))
food=int(input("enter the food:"))
travel=int(input("enter the travel:"))
expenses=rent+food+travel
savings=monthly_income-expenses
print(f"monthly_income={monthly_income}")
print(f"savings={savings}")
print(f"money spend on rent={rent}")
print(f"money spend on food={food}")
print(f"money spent on travel={travel}")
print(f"total expenses is={expenses}")





