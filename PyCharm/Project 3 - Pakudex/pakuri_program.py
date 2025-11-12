from pakudex import Pakudex

def display_menu():
    print()
    print("Pakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")
    print()
    option = (input("What would you like to do? "))
    return option

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity > 0:
                break
            else:
                print("Please enter a valid size.")
        except ValueError:
            print("Please enter a valid size.")
    print(f"The Pakudex can hold {capacity} species of Pakuri.")
    pakudex = Pakudex(capacity)
    while True:
        option = display_menu()
        if option == "1":
            species_list = pakudex.get_species_array()
            if species_list:
                print("Pakuri In Pakudex: ")
                for index, species in enumerate(species_list):
                    print(f"{index + 1}. {species}")
            else:
                print("No Pakuri in Pakudex yet!")
        elif option == "2":
            species = input("Enter the name of the species to display: ")
            stats = pakudex.get_stats(species)
            if pakudex.get_stats(species) is not None:
                print(f"Species: {species}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}")
            else:
                print("Error: No such Pakuri!")
        elif option == "3":
            if pakudex.get_size() < capacity:
                species = input("Enter the name of the species to add: ")
                if pakudex.add_pakuri(species):
                    print(f"Pakuri species {species} successfully added!")
                else:
                    if pakudex.get_size() >= pakudex.get_capacity():
                        print("Error: Pakudex is full!")
                    else:
                        print("Error: Pakudex already contains this species!")
            else:
                print("Error: Pakudex is full!")
        elif option == "4":
            species = input("Enter the name of the species to evolve: ")
            if pakudex.evolve_species(species):
                print(f"{species} has evolved!")
            else:
                print("Error: No such Pakuri!")
        elif option == "5":
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")
        elif option == "6":
            print("Thanks for using Pakudex! Bye!")
            break
        else:
            print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()