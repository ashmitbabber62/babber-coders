# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid



headPhone = "999"
smartWatch = "1599"
ps5 = "1299"
iPad = "599"


productName = input("Enter Product Name: ")


quantity = int(input("Enter the Quantity of the Product: ")) #bug   #We have added the data type int, The(int) was missing here. 


if productName == "headPhone":
    totalPrice = headPhone * quantity

elif productName == "smartWatch":
    totalPrice = smartWatch * quantity

elif productName == "ps5":
    totalPrice = ps5 * quantity

elif productName == "iPad":
    totalPrice = iPad * quantity


print(f"Total Amount To Be Paid: " , totalPrice);