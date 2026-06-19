while True:
    print("-------MENU---------\n1.Sunny\n2.Rainy\n3.Snowy\n")
    get_weather=input("Enter the weather from the menu=").lower()

    if get_weather == 'sunny':
        print("Go for a walk")
    elif get_weather=='rainy':
        print("Read a book")
        
    elif get_weather=='snowy':
        print("Build a snowman")
    else:
        print("Enter a valid choice from Menu.")