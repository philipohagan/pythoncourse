def word_length (user_input):
    if type(user_input) == int:
        print("Sorry integers don't have length")
    elif type(user_input) == float:
        print("Sorry floats don't have length")
    else:
        return len(user_input)

user_input = input("Enter a string: ")
print (word_length(user_input))
