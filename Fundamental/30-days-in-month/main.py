def isLeap(year):
    """ Check if a year is Leap Year nor not and return True or False """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
          return True
    else:
      return False

def daysInMonth(year, month):
    """ Return how many days are in the specified month and year """
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if isLeap(year):
        monthDays[1] = 29
    return monthDays[month - 1]
    
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = daysInMonth(year, month)
print(days)







