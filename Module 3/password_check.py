correct_password = "python123"
name = raw_input("Enter Name: ")
surname = raw_input ("Enter Surname: ")
password = raw_input ("Enter password: ")

while correct_password != password:
    password = raw_input ("Wrong Password! Enter again:")

message = "Hi %s %s, you are logged in" %(name,surname)
print(message)
