while True:
    print("1. Calculate Voltage, Joules (Current * Resistance)")
    print("2. Calculate Resistance, Ohms (Voltage / Current)")
    print("3. Calculate Current, Amps (Voltage / Resistance)")
    print("4. Calculate Wattage (Voltage * Current)")
    print("5. Calculate Milliamps (Amps * 1000)")
    print("6. Exit Program")
    number = int(input(">"))
    if (number == "1"):
        print("\n- Identifying Voltage -\n")
        i = float(input("Current: "))
        res = float(input("Resistence: "))
        volt = i * res
        print(f"Voltage =  {volt:.2f}\n")

    elif(number == "2"):
        print("\n- Identifying Resistance - \n")
        volt = float(input("Voltage: "))
        i = float(input("Current: "))
        res = volt / i
        print(f"Resistance = {res:.2fe}\n")

    elif(number == "3"):
        print("\n- Identifying Current -\n")
        volt = float(input("Voltage: "))
        res = float(input("Resistence: "))
        i = volt / res
        print(f"Current = {i:.2f}\n")

    elif(number == "4"):
        print("\n- Identifying Wattage -\n")
        volt = float(input("Voltage: "))
        i = float(input("Current: "))
        watt = volt * i
        print(f"Wattage = {watt:.2f}\n")

    elif(number == "5"):
        print("\n- Identifying Milliamps -\n")
        amps = float(input("Current: "))
        miliamp = amps * 1000
        print(f"Milliamps: {miliamp:.2f}\n")

    elif(number == "6"):
        break
    else:
        print("\nPlease choose a valid option.\n")



#Current aka Amperage (Net Flow)
#Voltage aka Joules per Coulomb (Pressure)
#Resistance aka Ohms

#1 Horsepower = 726 Watts
