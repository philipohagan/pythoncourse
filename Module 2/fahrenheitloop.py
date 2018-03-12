def fahrenheit(celsius):
    if celsius < -273.15:
        return ("Too cold")
    else:
        f = (celsius * 9/5 + 32)
        return f
temperatures=[10,-20,-289,100]

for t in temperatures:
    print (fahrenheit(t))
