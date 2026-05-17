month_dict = {1:31, 2:0, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
dates = {}
unclear = {}
counter = 0

for year in range(1, 100):
    for month in month_dict:
        if month == 2:
            if year % 4 == 0:
                days = 29

            else:
                days = 28

        else:
            days = month_dict[month]
            
        for day in range(1, days+1):
            date_str = str(day) + str(month) + str(year)
            if date_str in dates:
                dates[date_str] += 1

            else:
                dates[date_str] = 1


for date in dates:
    if dates[date] > 1:
        counter += dates[date]
        unclear[date] = dates[date]


print(counter)
print(len(unclear))