# temp_conversion_tool.py
FAHRENHEIT_TO_CELSIUS_FACTOR = 9 / 5    
CELSIUS_TO_FAHRENHEIT_FACTOR= 5 / 9 

def convert_to_celsius(fahrenheit): 
    """Convert temperature from Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    try:
        # Input temperature value
        temperature = float(input("Enter the temperature to convert: "))
        # Input temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_celsius}°C")
        elif unit == 'C':
            converted_fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_fahrenheit}°F")
        else:
            print("Invalid input. Please enter 'C' or 'F'.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
