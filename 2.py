def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def next_anniversary(date):
    day, month, year = map(int, date.split('/'))
    year += 1
    while True:
        if month == 2 and day == 29 and not is_leap_year(year):
            year += 1
        else:
            break
    return f"Next Anniversary Date: {day}/{month}/{year}"

def previous_anniversary(date):
    day, month, year = map(int, date.split('/'))
    year -= 1
    while True:
        if month == 2 and day == 29 and not is_leap_year(year):
            year -= 1
        else:
            break
    return f"Previous Anniversary Date: {day}/{month}/{year}"

if __name__ == "__main__":
    date = input("Enter Date: ")
    year = int(date.split('/')[2])
    
    if is_leap_year(year):
        print("Given Anniversary Year: Leap Year.")
        print(next_anniversary(date))
    else:
        print("Given Anniversary Year: Non Leap Year.")
        print(previous_anniversary(date))

