get_number = int(input("Enter your number for factorial="))
Factorial=1
while (get_number > 0):
    Factorial *= get_number
    get_number -= 1

print("factorail of number is=",Factorial)