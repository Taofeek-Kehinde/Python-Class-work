#BEGIN 
#
#A program that gives a customer a discount 
#based on the amount of product they purchase
#IF the purchased between 1,000 and 10,000 receive a 5% discoun
#ELSE purchased beween 10, 00 and 50,000 receive a 10% discoun
#ELSE urchased between 50,00 receive a 20% discount .using pyton
#
#END 

 #DEsign a program that applies discounts based on a customer'a total spending in a store.'  the greater the purchase amount , the higher the discount offered,
#
#
#purchased between 1,000 and 10,000 receive a 5% discount
#purchased beween 10, 00 and 50,000 receive a 10% discount
#purchased between 50,00 receive a 20% discount .using pyton
#
# ensure the program calculate 
#

discount_amount = int(input('Enter a purchased amount: '))

discount_amount = 1000
if(discount_amount <= 10000):
    print("receive 5% discount")
elif(discount_amount <= 50000 ):
    print("recive 10% discount")
elif(discount_amount >= 50000):
    print("recive 20% discount")
else:
    print("enter right option")
