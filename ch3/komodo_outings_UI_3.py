from komodo_outings import Outing

outings = []

while True:
    print(
"""
Please choose an option:
1. To enter an outing
2. List all events
3. List the dollar total of all events
4. Subtotal of the dollar amount of event
5. Exit
""")
    choice = input("Which option > ") 
    if choice == "1":
        print("Adding new Outing")
        ed = input("Date of event:")
        ev = input("Event type: ").lower()
        c = int(input("Cost:"))
        p = int(input("Number of people:"))
        cp = c / p
        new_outing = Outing(ed, ev, c, p, cp)
        outings.append(new_outing)
        print(outings)
    elif choice == "2":
        print ("Event Date        Type of Event            Total Cost      # of people         Cost per person")
        for e in outings:
            print(e)

    elif choice == "3":    
        total = 0
        for e in outings:
            total += e.costofevent
        print(f"The total cost of all events {total}")

    elif choice == "4":
        t_total = 0
        print (outings)
        event = input("What event total are you interested in: ").lower()
        for e in outings:
            if e.eventtype == event:
                t_total += e.costofevent
        print(f"The cost of {event} events is {t_total}")
    elif choice == "5":
        exit()
    else:
        print("invalid option")