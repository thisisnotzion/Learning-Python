#Python Tip Calculator Project
print("Welcome to Tip Calculator!")
tip = int(input("How much tip would you like to give 10 12 15?"))
bill_split = int(input("How many people to split the bill?"))
bill = int(input("what is the total bill?"))
our_tip = tip / 100 * bill
total_bill = tip + bill / bill_split
print(total_bill)

# rollcoaster height check