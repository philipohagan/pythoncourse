def fahrenheit(celsius):
    return celsius * 9/5 + 32

temperature = int(raw_input("Enter Temperature: "))
if temperature < -273.15:
    print ("Too cold")
else:
    print (fahrenheit(temperature))
