print("=== Welcome to the TIP CALCULATOR ===")
bill = float(input("What was the total bill? $"))

tip = float(input("What percentage tip would you like give? 10, 12, or 15? "))
total_tip = (tip / 100) * bill

head_count = int(input("How many people to split the bill? "))

total_bill = round((bill + total_tip) / head_count, 2)

print(f"Each person should pay: ${total_bill}")
