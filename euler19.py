#!/usr/bin/python



def is_leap(year):
    """ Return true if year is leap """
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def day_in_year(year):
    """ Return day count for a given year """
    if is_leap(year):
        return 366
    else:
        return 365

def day_in_month(month, year):
    """ Return day count for a given month and year """
    feb = 28
    if is_leap(year):
        feb = 29
    m = {1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return m[month]

def get_dow(day_from_1900):
    """ return the day of week for a given day from 1900 
        0=sunday, 1=monday..."""
    return day_from_1900 % 7


def get_date(day_from_1900):
    year = 1900
    month = 1
    dom = 1 # day of month
    dow = get_dow(day_from_1900)
   
    # compute year 
    while (day_from_1900 > day_in_year(year)):
        day_from_1900 -= day_in_year(year)
        year += 1
    
       
    # compute month
    while (day_from_1900 > day_in_month(month, year)):
        day_from_1900 -= day_in_month(month, year)
        month += 1
    
    # remaning days
    dom = day_from_1900
    d = {'year':year, 'month':month, 'dom':dom, 'dow':dow}
    return d
    


assert is_leap(2400)
assert day_in_year(1901) == 365
assert day_in_year(1600) == 366

# 01/01/1901 (tuesday)
assert get_date(366)['year'] == 1901, get_date(366)
assert get_date(366)['month'] == 1, get_date(366)
assert get_date(366)['dom'] == 1, get_date(366)
assert get_date(366)['dow'] == 2, get_date(366)

assert get_date(1)['year'] == 1900, get_date(566)
assert get_date(1)['month'] == 1, get_date(366)
assert get_date(1)['dom'] == 1, get_date(366)

# compute days in century
dic = 0
for i in range(1900, 2001):
    diy = day_in_year(i)
    print "Year: %s, Days: %s" % (i, diy)
    dic += diy

print "Days in century: ", dic 

# execice resolution
current_day = 1
sundays_fst = 0
while (current_day < dic):
    if current_day % 7 == 0:
        d = get_date(current_day)
        if d['dom'] == 1 and d['year'] != 1900:
            print "%(dom)s/%(month)s/%(year)s was a sunday :%(dow)s" % d
            sundays_fst +=1

    current_day += 1
print "Response ", sundays_fst
