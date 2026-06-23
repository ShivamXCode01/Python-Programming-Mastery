try:
    a = int(input("Enter a="))
    b = int(input("enter b="))
    c=a/b
    print("Your program start.")
    print('Your ouptut =',c)
except ValueError:
    print("enter a Valid integer.")
except ZeroDivisionError:
    print("You can't divide by zero.")
except Exception:
    print("Invaild,Error Occur")
finally:
    print("Your Program ended")

