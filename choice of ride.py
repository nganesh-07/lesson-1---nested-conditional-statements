selection1 = "bike"
selection2 = "car"

selection = str(input("Choose a vehicle (bike or car):"))

if (selection) == selection1:
    biketype = str(input("What type of bike (motorcycle or bicycle)?"))
    bike1 = "motorcycle"
    bike2 = "bicycle"
    if biketype == bike1:
        print("motorcycle has been selected.")
    else:
        print("bicycle has been selected.")
elif (selection) == selection2:
    cartype = str(input("What type of car (merc or porsche)?"))
    car1 = "merc"
    car2 = "porsche"
    if cartype == car1:
        print("mercedes has been selected.")
    else:
        print("porsche has been selected.")
else:
    print("input is invalid. try again.")
