# Day 2 Project: Tip Calculator

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill?: "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, 15?: ")) / 100
num_people = int(input("How many people to split the bill?: "))

total_tip = bill * percentage_tip
total_bill = bill + total_tip
bill_for_one_person =  total_bill / num_people
final_amount = round(bill_for_one_person, 2)

print(f"Each person should pay: ${final_amount}")
