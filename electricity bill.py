units = int(input("Enter amount of units consumed here:"))

if units < 50:
    amount = units * 1.00
    surcharge = 10
elif units <= 100:
    amount = units * 1.50
    surcharge = 15
elif units <= 200:
    amount = units * 2.00
    surcharge = 20
else:
    amount = units * 2.00
    surcharge = 25

total = amount + surcharge
print("Your total is:", total)