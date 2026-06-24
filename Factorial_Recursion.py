get_number = int(input("Enter a number to get facctorail of that number: "))

def Factorial(n):
    if n == 0 :
        return 1
    else :
        return n * Factorial(n-1)

print("Factoraial of your number =",end='')
print(Factorial(get_number))
