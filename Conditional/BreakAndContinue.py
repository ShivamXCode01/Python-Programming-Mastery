user_input = int (input("Enter your number for counting="))
print("Zero is skipped due to continue statement!!")
for i in range(1,user_input):
    print(i)
    if i == 0 :
        continue
        
        
    elif i == 7 :
        print("Thala for a reason!!")
        break
print("your code brak the loop due to brak statement at 7")
    