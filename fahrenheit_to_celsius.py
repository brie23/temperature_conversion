def temperature_conversion():
    print("This program will convert Fahrenheit to Celsius.")
    print("Please enter the temperature in degrees Fahreneheit: ")
    fahrenheit = int(input())
    celsius = (fahrenheit - 32) * 5 / 9
    print("This converts to approximately " + str(celsius) + " degrees Celsius.")

temperature_conversion()