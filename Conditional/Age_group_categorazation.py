get_age = int(input("Enter the age of the person="))

if get_age < 0 :
    print("Enter a valid age.")
if  get_age > 0 and get_age < 13:
    print("You are a child.")
elif get_age >= 13 and get_age <= 19:
    print("You are a teenager.")
elif get_age >= 20 and get_age < 60:
    print("You are an adult.")
elif get_age >= 60:
    print("you are a senior.")

print("Thankyou!!")