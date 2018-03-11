def calculate_age(year):
    age = 2018 - year
    return age

year = int(raw_input("Enter year of birth: "))

print(calculate_age(year))
