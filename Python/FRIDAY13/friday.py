import calendar

object = calendar.Calendar()

def findFriday():
    for day in object.itermonthdays3(year, month):
        if day[2]==13 and calendar.weekday(*day):
            return True
        return False

if __name__ == "__main__":
    month = int(input("Type the number of a month: "))
    year = int(input("Type a year: "))
    print(findFriday())

