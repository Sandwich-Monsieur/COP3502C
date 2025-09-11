cash = int(input("How much money do you have: "))


candy = cash/4
temp = candy
count = 0
while True:
    temp -= 3
    temp += 1
    count += 1
    if temp < 3:
        break
candy = candy + count

candy = int(candy)
print(f"You can purchase {candy} candy bars!")