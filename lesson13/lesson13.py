# input
day = int(input("Day:"))
month = int(input("Month:"))

if month == 2:
    if day > 18:
        print("The date is after February 18")
    elif day < 18:
        print("The date is before February 18")
elif month > 2:
    print("The date is after February 18")
elif month < 2:
    print("The date is before February 18")
else:
    print("Today is February 18!")