def parse_student(string):
    student_id = int(string[:8])
    birth_month = string[-4:-2]
    birth_year = string[-2:]
    name = string[8:-4]
    return {'id': student_id, 'name': name, 'birthdate': str(birth_month) + "/" + str(birth_year)}

def count_items(list):
    dictionary = {}
    for item in list:
        dictionary[item] = dictionary.get(item, 0) + 1
    return dictionary

def list_fighters(battle_data):
    fighters = set()
    for pokemon, result in battle_data.items():
        fighters.add(pokemon)
        fighters.update(result["win"])
        fighters.update(result["loss"])
    players = list(fighters)
    players.sort()
    return players
