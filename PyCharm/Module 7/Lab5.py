def hex_char_decode(digit):
    list = ['0','1','2','3','4','5','6','7','8','9', 'a', 'b', 'c', 'd', 'e', 'f']
    values = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    num = 0
    for i in values:
        if list[i] == (str(digit)).lower():
            num = i
            break
    return num

def hex_string_decode(hex):
    sum = 0
    if hex[0:3] == '0x':
        str = hex[2:]
        for i in range(0,len(str)):
            num = hex_char_decode(hex[i]) * 16**(len(hex)-i-1)
            sum += num
    else:
        for i in range(0,len(hex)):
            num = hex_char_decode(hex[i]) * 16**(len(hex)-i-1)
            sum += num
    print("Result:", int(sum))

def binary_string_decode(binary):
    sum = 0
    if binary[0:2] == '0b':
        str = binary[2:]
        for i in range(0, len(str)):
            if str[len(str)-i-1] == '1':
                num = 2**i
                sum += num
    else:
        for i in range(0, len(binary)):
            if binary[len(binary)-i-1] == '1':
                num = 2**i
                sum += num
    return sum

def binary_to_hex(binary):
    while len(binary) % 4 != 0:
       binary = "0" + binary
    times = int(len(binary)/4)
    list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hex = ""
    for i in range(1,times+1):
        str = binary[i*4-4:i*4]
        num = binary_string_decode(str)
        hex = hex + list[num]
    return hex

while True:
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")
    option = input("Please enter an option: ")
    if option == "1":
        hex = str(input("Please enter the numeric string to convert: "))
        hex_string_decode(hex)
    elif option == "2":
        binary = str(input("Please enter the numeric string to convert: "))
        sum = binary_string_decode(binary)
        print("Result:", sum)
    elif option == "3":
        binary = str(input("Please enter the numeric string to convert: "))
        sum = binary_to_hex(binary)
        print("Result:", sum)
    elif option == "4":
        print("Goodbye!")
        break
    else: print("Invalid option")
