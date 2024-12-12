# Unit-Conversion-tool

import time

from length import *
from area import *
from volume import *
from weight import *
from temperature import *
from t_ime import *


# Function ot get a valid input
def valid_input(prompt, valid_choice):
    """
    Prompt the user for input and validate it against a set of valid choices.

    Parameters:
        prompt (str): The message to display when asking for input.
        valid_choice (iterable): A collection of valid input choices.

    Returns:
        str: The user input if it is in the valid_choice collection.

    Raises:
        Exception: If the user input is not in the valid_choice collection, an error message is printed,
                   and the user is prompted again until a valid input is provided.
    """
    while True:
        try:
            user_input = input(prompt)
            if user_input not in valid_choice:
                raise Exception("Invalid Choice! Try again.")
            return user_input
        except Exception as e:
            print(e)

def conversion_unit_tool():
    """
        A simple unit conversion tool that guides the user through a series of menus to select the desired category and specific conversion within that category.

        The tool handles conversions for:

        - Length: Meters, kilometers, miles, yards
        - Area: Square meters, square kilometers, acres, square feet, hectares
        - Volume: Liters, milliliters, kiloliters, centiliters
        - Weight: Kilograms, grams, milligrams, pounds
        - Temperature: Celsius, Kelvin, Fahrenheit
        - Time: Seconds, minutes, hours

        The user interface is designed to be intuitive and user-friendly, providing clear prompts and error handling for invalid inputs.
        """

    # Choosing the Category
    print("""
    Select Category for Conversion: 
    |================================|
    |1. Length                       |
    |================================|
    |2. Area                         |
    |================================|
    |3. Volume                       |
    |================================|
    |4. Weight                       |
    |================================|
    |5. Temperature                  |
    |================================|
    |6. Time                         |
    |================================|
    """)
    while True:
            category_choice = valid_input("Select the category for conversion (1, 2, 3, 4, 5, 6): ",
                                          ["1", "2", "3", "4", "5", "6"])

            match category_choice:
                case "1":
                    print("You have chosen 'Length'")
                    print("""
                    Select the conversion in 'Length' category:
                    a. meters <-> kilometers
                    b. kilometers <-> miles
                    c. yards <-> meters
                    """)

                    conversion_choice = valid_input("Select conversion (a, b, c): ",
                                                    ["a", "b", "c"])

                    match conversion_choice:
                        case "a":
                            print("""
                            Select source:
                            1. meters     
                            2. kilometers
                            \n""")
                            source_target = valid_input("Your choice (1, 2): ",
                                                            ["1", "2"])

                            while True: # retry for a
                                try:
                                    if source_target == "1":
                                        meters = float(input("Enter number in meters: "))
                                        kilometers = meter_to_kilometer(meters)
                                        print(f"{meters} meter is {round(kilometers, 2)} kilometer.")
                                        break

                                    elif source_target == "2":
                                        kilometers = float(input("Enter unit (km): "))
                                        meters = kilometer_to_meter(kilometers)
                                        print(f"{kilometers} kilometer is {round(meters, 2)} meter.")
                                        break
                                except ValueError:
                                    print("Error: Invalid Input!.")



                        case "b":
                            print("""
                            Select source:
                            1. kilometers
                            2. miles
                            \n""")

                            source_target = valid_input("Your choice (1, 2): ",
                                                                ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        kilometers = float(input("Enter number in kilometers: "))
                                        miles = kilometer_to_miles(kilometers)
                                        print(f"{kilometers} kilometers is {round(miles, 2)} miles.")
                                        break

                                    elif source_target == "2":
                                        miles = float(input("Enter number in miles: "))
                                        kilometers = mile_to_kilometer(miles)
                                        print(f"{miles} miles is {round(kilometers, 2)} kilometers.")
                                        break

                                except ValueError:
                                    print("Error: Invalid Input!.")


                        case "c":
                            print("""
                                Select source:
                                1. yards
                                2. meters
                                \n""")
                            source_target = valid_input("Your choice (1, 2): ",
                                                                ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        yards = float(input("Enter number in yards: "))
                                        meters = yard_to_meter(yards)
                                        print(f"{yards} yards is {round(meters, 2)} meters.")
                                        break

                                    elif source_target == "2":
                                        meters = float(input("Enter number in meters: "))
                                        yards = mile_to_kilometer(meters)
                                        print(f"{meters} meters is {round(yards, 2)} yards.")
                                        break

                                except ValueError:
                                    print("Error: Invalid Input!!")

                case "2":
                    print("You have chosen 'Area'")
                    print("""
                    Select the conversion in 
                    'Area' Category:
                    a. meter square <-> kilometer square
                    b. acre <-> square foot
                    c. hectare <-> meter square
                    """)

                    conversion_choice = valid_input("Select conversion (a, b, c): ",
                                                    ["a", "b", "c"])

                    match conversion_choice:
                        case "a":
                            print("""
                            Select source:
                            1. meter square
                            2. kilometer square
                            \n""")

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        meter_square = float(input("Enter number (m^2): "))
                                        kilometer_square = square_meter_to_square_kilometer(meter_square)
                                        print(f"{meter_square} m^2 is {round(kilometer_square, 2)} km^2.")
                                        break

                                    elif source_target == "2":
                                        kilometer_square = float(input("Enter number (km^2): "))
                                        meter_square = square_kilometer_to_square_meter(kilometer_square)
                                        print(f"{kilometer_square} km^2 is {round(meter_square, 2)} m^2")
                                        break

                                except ValueError:
                                    print("Error: Invalid Input!!")

                        case "b":
                            print("""
                            Select source:
                            1. acre
                            2. square foot
                            \n""")

                            source_target = valid_input("Your choice (1, 2): ",
                                                         ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        acre = float(input("Enter number (acre): "))
                                        square_foot = acre_to_square_foot(acre)
                                        print(f"{acre} acres is {round(square_foot, 2)} ft^2.")
                                        break

                                    elif source_target == "2":
                                        square_foot = float(input("Enter number (ft^2): "))
                                        acre = square_foot_to_acre(square_foot)
                                        print(f"{square_foot} ft^2 is {round(acre, 2)} acres.")
                                        break

                                except ValueError:
                                    print("Error: Number expected!")

                        case "c":
                            print("""
                            Select source:
                            1. hectare
                            2. meter square
                            """)

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        meter_square = float(input("Enter number (m^2): "))
                                        hectare = square_meter_to_hectare(meter_square)
                                        print(f"{meter_square} m^2 is {round(hectare, 2)} ha.")
                                        break

                                    elif source_target == "2":
                                        hectare = float(input("Enter number (ha): "))
                                        meter_square = hectare_to_square_meter(hectare)
                                        print(f"{hectare} ha is {round(meter_square, 2)} m^2")
                                        break

                                except ValueError:
                                    print("Error: Invalid Input!!")



                case "3":
                    print("You have chosen 'Volume")
                    print("""
                    Select conversion in
                    'Volume' category:
                    a. liter <-> milliliters
                    b. kiloliter <-> liter
                    c. centiliter <-> milliliter
                    \n""")

                    conversion_choice = valid_input("Select conversion (a, b, c): ",
                                                    ["a", "b", "c"])

                    match conversion_choice:
                        case "a":
                            print("""
                            Select source:
                            1. liter
                            2. milliliter
                            \n""")

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        liter = float(input("Enter number (l): "))
                                        milliliter = l_to_ml(liter)
                                        print(f"{liter} l is {round(milliliter, 2)} ml.")
                                        break

                                    elif source_target == "2":
                                        milliliter = float(input("Enter number (km^2): "))
                                        liter = ml_to_l(milliliter)
                                        print(f"{milliliter} ml is {round(liter, 2)} l")
                                        break

                                except ValueError:
                                    print("Error: Invalid Input!!")

                        case "b":
                            print("""
                            Select source:
                            1. kiloliter
                            2. liter
                            \n""")

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        kiloliter = float(input("Enter number (kl): "))
                                        liter = kl_to_l(kiloliter)
                                        print(f"{kiloliter} kl is {round(liter, 2)} l.")
                                        break

                                    elif source_target == "2":
                                        liter = float(input("Enter number (l): "))
                                        kiloliter = l_to_kl(liter)
                                        print(f"{liter} l is {round(kiloliter, 2)} kl.")
                                        break

                                except ValueError:
                                    print("Error: Number expected!")

                        case "c":
                            print("""
                            Select source:
                            1. centiliter
                            2. milliliter
                            """)

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        centiliter = float(input("Enter number (m^2): "))
                                        milliliter = cl_to_ml(centiliter)
                                        print(f"{centiliter} cl is {round(milliliter, 2)} ml.")
                                        break

                                    elif source_target == "2":
                                        milliliter = float(input("Enter number (ha): "))
                                        centiliter = ml_to_cl(milliliter)
                                        print(f"{milliliter} ml is {round(centiliter, 2)} cl")
                                        break

                                except ValueError:
                                    print("Error: Invalid Input!!")

                case "4":
                    print("You have chosen 'Weight")
                    print("""
                        Select conversion in
                        'Weight' category:
                        a. kilograms <-> grams
                        b. grams <-> milligrams
                        c. pounds <-> kilograms
                        \n""")

                    conversion_choice = valid_input("Select conversion (a, b, c): ",
                                                    ["a", "b", "c"])

                    match conversion_choice:
                        case "a":
                            print("""
                                Select source:
                                1. kilograms
                                2. grams
                                \n""")

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        kilograms = float(input("Enter number (kg): "))
                                        grams = kg_to_g(kilograms)
                                        print(f"{kilograms} kg is {round(grams, 2)} g.")
                                        break

                                    elif source_target == "2":
                                        grams = float(input("Enter number (g): "))
                                        kilograms = g_to_kg(grams)
                                        print(f"{grams} g is {round(kilograms, 2)} kg.")
                                        break

                                except ValueError:
                                    print("Error: Invalid Input!!")

                        case "b":
                            print("""
                                Select source:
                                1. grams
                                2. milligrams
                                \n""")

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        grams = float(input("Enter number (g): "))
                                        milligrams = g_to_mg(grams)
                                        print(f"{grams} g is {round(milligrams, 2)} mg.")
                                        break

                                    elif source_target == "2":
                                        milligrams = float(input("Enter number (mg): "))
                                        grams = mg_to_g(milligrams)
                                        print(f"{milligrams} mg is {round(grams, 2)} g.")
                                        break

                                except ValueError:
                                    print("Error: Number expected!")

                        case "c":
                            print("""
                                Select source:
                                1. pounds
                                2. kilograms
                                """)

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        pounds = float(input("Enter number (lb): "))
                                        kilograms = lb_to_kg(pounds)
                                        print(f"{pounds} lb is {round(kilograms, 2)} kg.")
                                        break

                                    elif source_target == "2":
                                        kilograms = float(input("Enter number (kg): "))
                                        pounds = kg_to_lb(kilograms)
                                        print(f"{kilograms} kg is {round(pounds, 2)} lb")
                                        break

                                except ValueError:
                                    print("Error: Invalid Input!!")
                case "5":
                    print("You have chosen 'Temperature")
                    print("""
                        Select conversion in
                        'Temperature' category:
                        a. celsius <-> kelvin
                        b. celsius <-> fahrenheit
                        c. kelvin <-> fahrenheit
                        \n""")

                    conversion_choice = valid_input("Select conversion (a, b, c): ",
                                                    ["a", "b", "c"])

                    match conversion_choice:
                        case "a":
                            print("""
                                Select source:
                                1. celsius
                                2. kelvin
                                \n""")

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        celsius = float(input("Enter temperature (℃): "))
                                        kelvin = celsius_to_kelvin(celsius)
                                        print(f"{celsius} ℃ is {round(kelvin, 2)} K.")
                                        break

                                    elif source_target == "2":
                                        kelvin = float(input("Enter temperature (K): "))
                                        celsius = kelvin_to_celsius(kelvin)
                                        print(f"{kelvin} K is {round(celsius, 2)} ℃.")
                                        break

                                except ValueError:
                                    print("Error: Invalid Input!!")

                        case "b":
                            print("""
                                Select source:
                                1. celsius
                                2. fahrenheit
                                \n""")

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        celsius = float(input("Enter temperature (℃): "))
                                        fahrenheit = celsius_to_fahrenheit(celsius)
                                        print(f"{celsius} ℃ is {round(fahrenheit, 2)} ℉.")
                                        break

                                    elif source_target == "2":
                                        fahrenheit = float(input("Enter temperature (℉): "))
                                        celsius = fahrenheit_to_celsius(fahrenheit)
                                        print(f"{fahrenheit} ℉ is {round(celsius, 2)} ℃.")
                                        break

                                except ValueError:
                                    print("Error: Number expected!")

                        case "c":
                            print("""
                                Select source:
                                1. kelvin
                                2. fahrenheit
                                """)

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        kelvin = float(input("Enter number (K): "))
                                        fahrenheit = lb_to_kg(kelvin)
                                        print(f"{kelvin} K is {round(fahrenheit, 2)} ℉.")
                                        break

                                    elif source_target == "2":
                                        fahrenheit = float(input("Enter number (kg): "))
                                        kelvin = fahrenheit_to_kelvin(fahrenheit)
                                        print(f"{fahrenheit} ℉ is {round(kelvin, 2)} K")
                                        break

                                except ValueError:
                                    print("Error: Invalid Input!!")

                case "6":
                    print("You have chosen 'Time")
                    print("""
                        Select conversion in
                        'Time' category:
                        a. second <-> minute
                        b. minute <-> hour
                        c. second <-> hour
                        \n""")

                    conversion_choice = valid_input("Select conversion (a, b, c): ",
                                                    ["a", "b", "c"])

                    match conversion_choice:
                        case "a":
                            print("""
                                Select source:
                                1. second
                                2. minute
                                \n""")

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        second = float(input("Enter time (s): "))
                                        minute = second_to_minute(second)
                                        print(f"{second} seconds is {round(minute, 2)} minutes.")
                                        break

                                    elif source_target == "2":
                                        minute = float(input("Enter time (min): "))
                                        second = minute_to_second(minute)
                                        print(f"{minute} minutes is {round(second, 2)} seconds.")
                                        break

                                except ValueError:
                                    print("Error: Invalid Input!!")

                        case "b":
                            print("""
                                Select source:
                                1. minute
                                2. hour
                                \n""")

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        minute = float(input("Enter time (min): "))
                                        hour = minute_to_hour(minute)
                                        print(f"{minute} minutes is {round(hour, 2)} hours.")
                                        break

                                    elif source_target == "2":
                                        hour = float(input("Enter time (hrs): "))
                                        minute = hour_to_minute(hour)
                                        print(f"{hour} hours is {round(minute, 2)} minutes.")
                                        break

                                except ValueError:
                                    print("Error: Number expected!")

                        case "c":
                            print("""
                                Select source:
                                1. second
                                2. hour
                                """)

                            source_target = valid_input("Your choice (1, 2): ",
                                                        ["1", "2"])
                            while True:
                                try:
                                    if source_target == "1":
                                        second = float(input("Enter number (K): "))
                                        hour = second_to_hour(second)
                                        print(f"{second} seconds is {round(hour, 2)} hours.")
                                        break

                                    elif source_target == "2":
                                        hour = float(input("Enter number (kg): "))
                                        second = hour_to_second(hour)
                                        print(f"{hour} hours is {round(second, 2)} seconds")
                                        break

                                except ValueError:
                                    print("Error: Invalid Input!!")

            convert_again = valid_input("Do you want to perform another conversion? (y/n): ", ["y", "n"])
            if convert_again.lower() == "n":
                print("Thank you for using the Unit Converter!")
                print("Quitting.....")
                time.sleep(0.3)
                quit()


if __name__ == "__main__":
    conversion_unit_tool()