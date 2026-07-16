

print("Welcome to the tip calculator")
bill=int(input("What was the total bill? $"))
people=int(input("How many people will you like to split the bill with? "))
tip=float(input("How many percent will you like to give? 10 12 15"))
tip_as_percent=(tip /100)
bill_with_tip=(bill * tip_as_percent)
total_bill=bill+bill_with_tip
bill_per_person=total_bill / people
print(f"Each person should pay {bill_per_person} $")
