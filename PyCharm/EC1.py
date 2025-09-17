movie_A = "12 Strong"
movie_B = "Coco"
movie_C = "The Post"
adult_tickets = 0
kid_tickets = 0

def tickets(adult, kid):
    adult = 0
    kid = 0
    while True:
        adult = int(input("Adult tickets: "))
        if (adult + kid) > 30:
            print("Invalid option; please restart app...")
            break
        kid = int(input("Kid tickets: "))
        if (adult + kid) > 30:
            print("Invalid option; please restart app...")
            break
        break
    return adult, kid

print("Available movies today:")
print(f"A) {movie_A}:\t1)2:30\t 2)4:40\t 3)7:50\t 4)10:50")
print(f"B) {movie_B}:\t\t1)12:40\t 2)3:45")
print(f"C) {movie_C}:\t1)12:45\t 2)3:35\t 3)7:05\t 4)9:55")

choice = str(input("Movie choice: "))

if choice == "A":
    time = int(input("Showtime: "))
    if time > 4:
        print("Invalid option; please restart app...")
    elif time <= 4:
        adult_tickets, kid_tickets = tickets(adult_tickets, kid_tickets)
        if (adult_tickets + kid_tickets) <= 30:
            total = adult_tickets * 12.45 + kid_tickets * 9.68
            print(f"Total cost: ${total:.2f}")
elif choice == "B":
    time = int(input("Showtime: "))
    if time > 2:
        print("Invalid option; please restart app...")
    elif time == 2:
        adult_tickets, kid_tickets = tickets(adult_tickets, kid_tickets)
        if (adult_tickets + kid_tickets) <= 30:
            total = adult_tickets * 12.45 + kid_tickets * 9.68
            print(f"Total cost: ${total:.2f}")
    elif time == 1:
        adult_tickets, kid_tickets = tickets(adult_tickets, kid_tickets)
        if (adult_tickets + kid_tickets) <= 30:
            total = adult_tickets * 11.17 + kid_tickets * 8.00
            print(f"Total cost: ${total:.2f}")
elif choice == "C":
    time = int(input("Showtime: "))
    if time > 4:
        print("Invalid option; please restart app...")
    elif time == 1:
        adult_tickets, kid_tickets = tickets(adult_tickets, kid_tickets)
        if (adult_tickets + kid_tickets) <= 30:
            total = adult_tickets * 11.17 + kid_tickets * 8.00
            print(f"Total cost: ${total:.2f}")
    elif time > 1:
        adult_tickets, kid_tickets = tickets(adult_tickets, kid_tickets)
        if (adult_tickets + kid_tickets) <= 30:
            total = adult_tickets * 12.45 + kid_tickets * 9.68
            print(f"Total cost: ${total:.2f}")

else:
    print("Invalid option; please restart app...")