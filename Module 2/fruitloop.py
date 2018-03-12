fruitfile = open("fruits.txt")
fruits = fruitfile.read()
fruitfile.close()
fruits = fruits.splitlines()
for f in fruits:
    print(len(f))
