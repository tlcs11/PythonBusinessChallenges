from komodo_claim import Claim
claims = []

# ClaimID   Type    Description             Amount      DateOfAccident  DateOfClaim      IsValid
# 1          Car    Car accident on 465.     $400.00     4/25/18         4/27/18          True
# 2          House  House fire in kitchen.   $4000.00    4/26/18         4/28/18          True
# 3          Theft  Stolen pancakes.         $4.00       4/27/18         6/01/18          False
# 1          Car     Car Accident on 464.    $400.00     4/25/18         4/27/18          True
# Do you want to deal with this claim now(y/n)?  y

# When the agent presses 'y', the claim will be pulled off the top of the queue. If the agent presses 'n', it will go back to the main menu.
while True:
    print("""
    Choose a menu item:
    1. See all claims
    2. Take care of next claim
    3. Enter a new claim
    4. Exit
    """)
    choice = input("Which option > ") 

    if choice == "1":
        print("ClaimID    Type             Amount      DateOfAccident  DateOfClaim      IsValid     Description")
        for entry in claims:                                      #always (1)for (2) entry (3) in (4) the name of the list (5) :
            print(entry) 
    elif choice == "2":
        if claims:
            next_claim = claims[0]
            print("ClaimID    Type             Amount      DateOfAccident  DateOfClaim      IsValid     Description")
            print(next_claim)
            resp = input("Handel Claim? Y/N")
            if resp == "Y":
                claims.remove(next_claim)
                print("The claim has been resolved")
        else:
            print("There are no claims")

    elif choice == "3":
        u_claimid = input("ID: ")
        u_type = input("Type: ")
        u_amount = input("Cost: ")
        u_date_of_accident = input("Date of Accident: ")
        u_claim_date = input("Today's date: ")
        days_ago = int(input("Days since event: "))
        if days_ago > 30:
            u_vaild = False
        else:
            u_vaild = True
        u_des = input("Details: ")
        new_claim = Claim(u_claimid, u_type, u_des, u_amount, u_date_of_accident, u_claim_date, False)   #new_claim is a claim object
        claims.append(new_claim)

    elif choice == "4":
        exit()
    else:
        print("Choice was not valid!!")



# new_claim = Claim(1, "auto", "car crash", 500.50, "3-5-18", "6-4-19", False)
# print(new_claim)