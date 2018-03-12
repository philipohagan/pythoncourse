def fahrenheit(celsius):
    return celsius * 9/5 + 32

temperature = int(input("Enter Temperature in Celsius: "))
if temperature < -273.15:
    print ("Too cold")
else:
    print (str(fahrenheit(temperature)) + " Fahrenheit")
