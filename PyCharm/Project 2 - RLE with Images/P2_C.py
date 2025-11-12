import console_gfx

#console_gfx.display_image(console_gfx.test_rainbow)

def display_menu():
    print("\nRLE Menu\n"
          "--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")
    print()
    option = int(input("Select a Menu Option: "))
    return option

def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    while True:
        option = display_menu()
        if option == 0:
            break
        elif option == 1:
            file_name = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(file_name)
        elif option == 2:
            image_data = console_gfx.test_image
            print("Test image data loaded.")
        elif option == 3:
            rle_string = input("Enter an RLE string to be decoded: ")
            rle_data = string_to_rle(rle_string)
            image_data = decode_rle(rle_data)
        elif option == 4:
            rle_hex_string = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(rle_hex_string))
        elif option == 5:
            data_hex_string = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(data_hex_string)
        elif option == 6:
            print("Displaying image...")
            console_gfx.display_image(image_data)
        elif option == 7:
            rle_data = encode_rle(image_data)
            print("RLE representation:", to_rle_string(rle_data))
        elif option == 8:
            rle_data = encode_rle(image_data)
            print("RLE hex values:", to_hex_string(rle_data))
        elif option == 9:
            print("Flat hex values:", to_hex_string(image_data))




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

def to_rle_string(rle_data):
    parts = []
    for run in range(0, len(rle_data), 2):
        count = rle_data[run]
        value = hex(rle_data[run + 1])[2:]
        parts.append(f"{count}{value}")
    return ':'.join(parts)

def string_to_rle(rle_string):
    rle_data = []
    runs = rle_string.split(":")
    for run in runs:
        count = int(run[:-1])
        value = int(run[-1], 16)
        rle_data.extend([count, value])
    return rle_data


if __name__ == "__main__":
    main()