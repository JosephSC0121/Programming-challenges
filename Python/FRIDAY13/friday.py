import calendar

objCal = calendar.Calendar()

def findFriday():
    for day in objectCal.itermonthdays3(year, month):
        if day[2]==13 and calendar.weekday(*day)==4:
            return True
    return False

if __name__ == "__main__":
    month = int(input("Type the number of a month: "))
    year = int(input("Type a year: "))
    if findFriday():
        print("The 13th of the month is a Friday!")
    else:
        print("The 13th of the month is not a Friday.")

