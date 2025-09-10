movie_A = "12 Strong"
movie_B = "Coco"
movie_C = "The Post"



print("Available movies today:")
print(f"A) {movie_A}:\t1)2:30\t 2)4:40\t 3)7:50\t 4)10:50")
print(f"B) {movie_B}:\t\t1)12:40\t 2)3:45")
print(f"C) {movie_C}:\t1)12:45\t 2)3:35\t 3)7:05\t 4)9:55")

choice = str(input("Movie choice: "))

if choice == "A":
    time = int(input("Showtime: "))
    if time > 4:
        print("Invalid option; please restart app...")
    elif time == 3:





elif choice == "B":
    print(movie_B)
elif choice == "C":
    print(movie_C)
else:
    print("Invalid option; please restart app...")