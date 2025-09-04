legs = str(input("Does it have legs [y/n]: "))

if legs == "n":
    land = str(input("Does it live on land [y/n]: "))
    if land == "n":
        print("It's a shark!")
    else:
        print("It's a snake!")
else:
    fluffy = str(input("Is it fluffy [y/n]: "))
    if fluffy == "n":
        print("It's a gator!")
    else:
        print("It's a cat!")
    