from itertools import count


def to_hex_string(data):
    hex_digits = "0123456789abcdef"
    hex_string = ""
    for value in data:
        if value < 16:
            hex_string += hex_digits[value]
        else:
            hex_string += hex_digits[value // 16] + hex_digits[value % 16]
    return hex_string

def count_runs(flat_data):
    num = 1
    runs = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1]:
            num += 1
            if num > 15:
                runs += 1
                num = 1
        else:
            runs += 1
            num += 1
    return runs

def encode_rle(flat_data):
    rle = []
    flat_data = flat_data + [""]
    runs = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1]:
            runs += 1
            if runs > 15:
                rle.append(15)
                rle.append(flat_data[i - 1])
                runs = 1
        else:
            rle.append(runs)
            rle.append(flat_data[i - 1])
            runs = 1
    return rle

def get_decoded_length(rle_data):
    decoded_rle = []
    for i in range(0, len(rle_data), 2):
        count = rle_data[i]
        value = rle_data[i + 1]
        for i in range(count):
            decoded_rle.append(value)
    return len(decoded_rle)

def decode_rle(rle_data):
    decoded_rle = []
    for i in range(0, len(rle_data), 2):
        count = rle_data[i]
        value = rle_data[i + 1]
        for i in range(count):
            decoded_rle.append(value)
    return decoded_rle

def string_to_data(data_string):
    hex_dict = {
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'a': 10, 'b': 11,
    'c': 12, 'd': 13, 'e': 14, 'f': 15
    }
    data = []
    for value in data_string:
        data.append(hex_dict[value])
    return data
