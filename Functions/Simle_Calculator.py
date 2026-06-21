def Sum (number_1,number_2):
    return number_1+number_2
def Subtract (number_1,number_2):
    return number_1 - number_2
def Product (number_1,number_2):
    return number_1 * number_2
def Division (number_1,number_2):
    return number_1/number_2


print('---------------MENU----------------\n1.Sum\n2.Subtract\n3.Product\n4.Division')
Choice=int(input("Enter your choice according to menu="))
number_1 = int(input("Enter your first number="))
number_2 = int(input("Enter your second number="))
if Choice == 1 :
    print(Sum(number_1,number_2))
elif Choice == 2 :
    print(Subtract(number_1,number_2))
elif Choice == 3 :
    print(Product(number_1,number_2))
elif Choice == 4:
    print(Division(number_1,number_2))
else:
    print("Enter a valid option")
