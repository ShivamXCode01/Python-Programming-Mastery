Get_input = int (input("Enter a number="))

def Fibonacci (n):
    a = 0 
    b = 1 
    
    if n == 1 :
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a=b
            b=c
            print(c)


Fibonacci(Get_input)