while True:
    print("-------MENU---------\n1.Green\n2.Yellow\n3.Brown\n")
    get_condition=input("Enter your Banana condtion from above menu=").lower()

    if get_condition=='green':
        print("unripe is banana")
        break
    elif get_condition == 'yellow':
        print("Banana is ripe")
        break
    elif get_condition == 'brown':
        print("banana is overripe")
        break
    else:
        print("Error!!, Enter a valid option from menu.")
        break