
print('Welcome to Tip Calculator!')

bill = float(input("What was your bill? \n$"))
tip_percent = float(input("What percentage tip would you like to give? 10, 15, or 20? \n"))
people = int(input("How many people to split the bill? \n"))


tip_amount = bill * (tip_percent/100)
total_bill = bill + tip_amount


per_person =total_bill/people20

print(f"Each person should pay: ${per_person:.2f}")
