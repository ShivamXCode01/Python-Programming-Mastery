Get_password=input("Enter your password=")
get_length_password=len(Get_password)

if get_length_password < 6 and get_length_password > 0 :
    print(f" Your passworks length is {get_length_password} so it is Weak")
elif get_length_password >= 6 and get_length_password < 10 :
    print(f" Your passworks length is {get_length_password} so it is Medium")
elif get_length_password >= 10  and get_length_password < 100 :
    print(f" Your passworks length is {get_length_password} so it is Strong")
else:
    print("You are shit bull!!")