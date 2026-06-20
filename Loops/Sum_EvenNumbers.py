User_input=int(input("Enter your number="))

Sum = 0 

for i in range(User_input+1):
    if i%2==0:
        Sum += i
    
print("Sum of Even numbers in your given Range=")
print(Sum)