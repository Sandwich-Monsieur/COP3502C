def print_backwards(string):
    if string == "":
        return
    print(string[-1], end = "")
    print_backwards(string[:-1])

def format_names(name_list):
    if not name_list:
        return []
    name = name_list[0]
    if "," in name:
        formatted = name
    else:
        split_name = name.split()
        if len(split_name) == 2:
            formatted = split_name[1] + ", " + split_name[0]
    return [formatted] + format_names(name_list[1:])

def sum_a(dictionaries):
    if not dictionaries:
        return 0
    first = dictionaries[0]
    rest = dictionaries[1:]
    return first.get("a", 0) + sum_a(rest)

def process_list(num_list, count = 0):
    if count >= len(num_list):
        return []
    list1 = []
    list2 = []
    if len(num_list) % 2 == 0:
        if count % 2 == 0:
            list1 += [str(num_list[count])] + process_list(num_list, count + 1)
        else:
            list2 += process_list(num_list, count + 1) + [num_list[len(num_list)-count]*10]
        return list1 + list2
    if len(num_list) % 2 == 1:
        if count % 2 == 0:
            list1 += [str(num_list[count])] + process_list(num_list, count + 1)
        else:
            list2 += process_list(num_list, count + 1) + [num_list[len(num_list)-1-count]*10]
        return list1 + list2
