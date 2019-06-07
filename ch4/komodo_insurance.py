badges = {}                    #string for a key and empty list for input
                 
while True:
    print("1 to make badge",
            "2 to print all badges", "3 remove a door","4 to end" )
    op = input("> ")
    if op == "1":
        b_id = int(input("enter en id:"))
        add_door = input("Add a door to badge Y or N:  ")
        badges.update({b_id:[]})
        # input("Add a door to badge Y or N:  ")
        if add_door in ["Y", "y"]:
            b_doors = input("Door Num: " )
            badges[b_id].append(b_doors)
    elif op == "2":
        print(badges)

    elif op == "3":
        print (badges)
        b_id = int(input("Enter badge id:"))
        remove_door = input("ARE YOU SURE YOU WOULD LIKE TO REMOVE ACCESS? Please enter door #  ")
        y = b_id
        x = remove_door
        badges[b_id].remove(x)
    
    elif op == "4":
        exit()

    else:
        print("Invalid choice")


