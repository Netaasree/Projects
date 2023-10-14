Weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = Weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = Weight / 0.45
    print(f"You are {converted} pounds")
