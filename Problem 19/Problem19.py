# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

year = 1900
month = 1
dotMonth = 1
dotWeek = 0 # monday

firstSundayCount = 0

while year < 2001:
  monthLength = 0

  # if month == 1:
  #   print(f"year: {year}")
  # print(f"month: {month}")

  if month in [4, 9, 6, 11]: # 30 days
    monthLength = 30
  elif month == 2: # 28 / 29 days
    if year % 100 == 0:
      if year % 400 == 0:
        monthLength = 29
      else:
        monthLength = 28
    elif year % 4 == 0:
      monthLength = 29
    else:
      monthLength = 28
  else: # 31 days
    monthLength = 31

  # print(f"monthLength: {monthLength}")

  if dotMonth == 1 and dotWeek == 6 and year >= 1901:
      firstSundayCount += 1

  dotWeek = (dotWeek + monthLength) % 7
  
  if month == 12:
    year += 1
    month = 1
  else:
    month += 1

print(firstSundayCount)
  
  
