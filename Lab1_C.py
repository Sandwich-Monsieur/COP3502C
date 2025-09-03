year1 = int(input('Enter the year for date 1: '))
month1 = int(input('Enter the month for date 1: '))
day1 = int(input('Enter the day for date 1: '))
year2 = int(input('Enter the year for date 2: '))
month2 = int(input('Enter the month for date 2: '))
day2 = int(input('Enter the day for date 2: '))

yearDiff = year2 - year1
monthDiff = month2 - month1
dayDiff = day2 - day1

totalMonths = yearDiff * 12  + monthDiff
totalDays = abs(totalMonths * 30 + dayDiff)

print(f"The difference between {month1}/{day1}/{year1} and {month2}/{day2}/{year2} is {totalDays} days!")