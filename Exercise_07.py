

def celsius_to_fahrenheit(celsius_temperature):
    return celsius_temperature * (9 / 5) + 32


temperature = int(input('Enter a temperature in degrees Celsius: '))

print(f"The inserted temperature equals to {celsius_to_fahrenheit(temperature)} degrees Fahrenheit.")
