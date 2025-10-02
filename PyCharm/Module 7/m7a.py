def bin(digit):
    if digit == 0:
        return "0"
    binary = ""
    while digit > 0:
        binary = str(digit % 2) + binary
        digit //= 2
    return binary

def capitalize(string):
    string += " "
    exceptions = ["o","u","s","n","d"]
    output = []
    word = ""
    output_string = ""
    for char in string:
        word += char.lower()
        if char == " ":
            output.append(word)
            word = ""
    for word in output:
        if word[0] in exceptions:
            output_string += word

        else:
            word = word[0].capitalize() + word[1:]
            output_string += word
    return output_string[:-1]

def partition(list, size):
    new_list = []
    count = 0
    for num in list:
        count += 1
    partitions = int(count/size)

    for i in range(1, partitions+1):
        new_list.append(list[i*size-size:i*size])
    extra = count % size
    if count/size != int(count/size):
            new_list.append(list[(count-extra):count])
    return new_list
