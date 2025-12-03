def main():
    highest_level = 0
    winner = ""
    pakuri_set = set()

    with open("contest.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            candidate_trainer = parts[0]

            for pakuri_data in parts[1:]:
                if "-" in pakuri_data:
                    species, level_str = pakuri_data.split("-")
                    level = int(level_str)
                    pakuri_set.add(species)

                    if level > highest_level:
                        highest_level = level
                        winner = candidate_trainer

    with open("winner.txt", "w") as win_file:
        win_file.write(winner + "\n")

    with open("pakuri.txt", "w") as pakuri_file:
        for species in sorted(pakuri_set):
            pakuri_file.write(species + "\n")

if __name__ == "__main__":
    main()
