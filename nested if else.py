medical_cause = input("Valid medical excuse? Enter Yes or No:")
attendance = int(input("Number of classes attended:"))

if medical_cause == "Yes":
    print("Can take test.")
else:
    if attendance >= 75:
        print("Can take test.")
    else:
        print("Cannot take test.")