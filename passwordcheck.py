'''
START

a program to check the strength of a password 

IF a user 

'''
enter_password = input("Enter a password ")
print(len(enter_password))

enter_password = int(enter_password)

if enter_password >= 8:

    print("password length \t ", "Strength" )

elif enter_password <= 8:

    print("Less than 8 \t ", "Very weak" )

elif enter_password == 8:

    print("is equal to 8 \t", "weak")

elif enter_password <= 8 and enter_password <= 16:
    print("is between 8 and 16\t", "Strong")

elif (enter_password >= 16):
    print("above 16 \t ", "Very strong")   

else:
    print("wrong input")


