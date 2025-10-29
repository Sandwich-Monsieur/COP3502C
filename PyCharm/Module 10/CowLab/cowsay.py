import sys
from heifer_generator import get_cows



def list_cows(cows):
    names = [cow.get_name() for cow in cows]
    return names

def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None

def main():
    if sys.argv[1] == "-l":
        names = list_cows(get_cows())
        print("Cows available:", " ".join(names))

    elif sys.argv[1] == "-n":
        cow = find_cow(sys.argv[2], get_cows())
        message = sys.argv[3:]
        if cow is None:
            print("Could not find", str(sys.argv[2]), "cow!")
        else:
            print(message[0], " ".join(message[1:]))
            print(cow.get_image())

    else:
        message = sys.argv[1:]
        default_cow = find_cow("heifer", get_cows())
        print(message[0], " ".join(message[1:]))
        print(default_cow.get_image())


if __name__ == "__main__":
    main()