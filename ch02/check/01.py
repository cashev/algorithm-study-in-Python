def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False

for year in range(1950, 2051):
    if isLeapYear(year):
        print(year, end=' ')
