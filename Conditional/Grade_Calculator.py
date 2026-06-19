get_marks= int(input('Enter your marks (0-100)='))

if get_marks <= 100 and get_marks >=90:
    print("Your grade is 'A' ")
elif get_marks < 90 and get_marks >= 80:
    print("Your grade is 'B'")
elif get_marks < 80 and get_marks >=70:
    print("Your grade is 'C'")
elif get_marks < 70 and get_marks >= 60:
    print("Your grade is 'D'")
elif get_marks < 60 and get_marks >=0:
    print("Your grade is 'F'")
else:
    print(" Error!! Enter a Valid Marks.")

print("A piece of paper Can't decide your future,Enjoy your life!!") 