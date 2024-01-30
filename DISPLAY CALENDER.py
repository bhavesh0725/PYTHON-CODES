import calendar

year= int(input("Enter the year you want to see: "))
month= int(input("Enter the month you want to see: "))

result= calendar.month(year, month)
print(result)
