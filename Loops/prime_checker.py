get_input=int(input("Enter your number to check prime="))


if get_input < 2:
    print("Your number is Prime.")
else:
    for i in range (2,get_input):
        if (get_input % i == 0):
            print("Your number is not prime")
            break
        else:
            print("Your number is prime")
            break

    print("Thankyou!!!")