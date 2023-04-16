import calendar

m,d,y=map(int,input().split())

day_nam=calendar.day_name[calendar.weekday(y,m,d)]

print(day_nam.upper())