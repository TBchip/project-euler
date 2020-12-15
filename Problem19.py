months_30_days = [4, 6, 9, 11]
months_31_days = [1, 3, 5, 7, 8, 10, 12]

sundays = 0

year = 1901
month = 0
days_past = 7
while year < 2001:
    month += 1

    if month == 13:
        month = 0
        year += 1
        continue

    if days_past % 7 == 0:
        sundays += 1

    if month in months_30_days:
        days_past += 30
    elif month in months_31_days:
        days_past += 31
    else:
        if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
            days_past += 29
        else:
            days_past += 28

print(sundays)
print()
print(year)
print(month)
print(days_past)
