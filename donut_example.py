price=int(input("Enter the price of the donut: Rs. "))

quantity=int(input("Enter the no. of donuts: "))

amt=price*quantity

if amt>1000:
    print("Yah 10% discount is there!")
    discount=amt*10/100
    amt=amt-discount

else:
    print("A discount of 5% is applicable!")
    discount=amt*5/100
    amt=amt-discount

print("Total amount is: Rs. ",amt)         
