get_year=int(input("Enter the year you want to check="))

if (get_year % 400 == 0) or (get_year % 4 == 0 and get_year % 100 != 0):
    print("It is a leap year")
else:
    print('It is not a leap year')