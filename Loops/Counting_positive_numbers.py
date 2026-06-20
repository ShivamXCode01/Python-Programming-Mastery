n = int(input("Enter length: "))
list = []

for i in range(n):
    x = int(input(f"Enter element {i}: "))
    list.append(x)

print(list)

list_2=[0,-3,9,-4,-3,-2,8,0,4,-3]
count_Positive_number = 0 
count_Negative_number =0
for i in list_2:
    if(i > 0):
        count_Positive_number +=1
    elif(i<0):
        count_Negative_number += 1
print("number of positive numbers in the list=")
print(count_Positive_number)
print("number of negative number in a list=")
print(count_Negative_number)