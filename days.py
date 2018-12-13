import calendar

cal = calendar.Calendar()
count = []

for month in range(1, 13):
    count.append([0, 0])
    for day in cal.itermonthdays2(2019, month):
        if day[0] and day[1] < 5:
            count[month-1][day[0]//16] += 1

print(count)