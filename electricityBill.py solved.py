# Electricity Bill Calculator
# Write a program that calculates the electricity bill based on units consumed using different rates for different slabs.

# 100 and below = 3
# 100-200 = 5
# 200-300 = 7
# 300 above = 10


# Taking Units Consumed as Input
units = int(input("Enter Units Consumed: ")) #The Int was missing, which it was not giving an output  #bug


# Calculating Bill Based on Slabs
if units == 100:   
    totalBill = units * 3   

elif units == 200:
    totalBill = 300 + units-100*5

elif units == 300:
    totalBill = 300 + 500 + units-200*7

else:
    totalBill = 300 + 500 + 700 + units-300*10  #The Expression were expanding, Not a bug but it would be easier if we write the direct expression

# Displaying the Final Bill
print(f"Total Electricity Bill: {totalBill}");