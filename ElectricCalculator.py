while True:
    print("1. Calculate Voltage (Current * Resistance)")
    print("2. Calculate Resistance (Voltage / Current)")
    print("3. Calculate Current (Voltage / Resistance)")
    print("4. Calculate Wattage (Voltage * Current)")
    print("5. Exit Program")
    number = input("> ")
    if (number == "1"):
        print("- Calculating Voltage -")
        i = float(input("Current: "))
        res = float(input("Resistence: "))
        volt = i * res
        print(f"Voltage =  {volt:.2f}")

    elif(number == "2"):
        print("- Calculating Resistance -")
        volt = float(input("Voltage: "))
        i = float(input("Current: "))
        res = volt / i
        print(f"Resistance = {res:.2f}")

    elif(number == "3"):
        print("- Calculating Current -")
        volt = float(input("Voltage: "))
        res = float(input("Resistence: "))
        i = volt / res
        print(f"Current = {i:.2f}")

    elif(number == "4"):
        print("- Calculating Wattage -")
        volt = float(input("Voltage: "))
        i = float(input("Current: "))
        watt = volt * i
        print(f"Wattage = {watt:.2f}")

    elif(number == "5"):
        break
    else:
        print("Not an option, Try again")


#Wattage = Volts * Amps
#Amperage (Current) = Watts / Volts
#Amperage (Current) = Voltage / Resistance
#MilliAmps = Amps * 1000
#Voltage (Joules per Coulomb) = Current * Resistance
#Resistance (Ohms) = Voltage / Amperage (Current)

#1 Horsepower = 726 Watts
