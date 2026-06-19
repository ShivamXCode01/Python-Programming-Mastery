Customer_age = int(input("Enter the age of customer="))
Day_name=input("Enter the today day name=").lower()

while True:
    if Day_name == 'wednesday':
        print("Your ticket price is $2 for everyone.")
        break
    else :
        if Customer_age >= 18:
            print("You are adult so, your ticket price is $12.")
            break
        elif Customer_age < 18 and Customer_age > 0:
            print("Your are children so, your ticket price is $8.")
            break

print("Thankyou for visiting!!") 