# Leep year
"""
year % 4 == 0 &
year % 100 != 0 /
year % 400 == 0
"""


def isleepyear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False


year = int(input("Enter the year : "))

if isleepyear(year):
  print('{} this year is a leep year.'.format(year))
else:
  print('{} this year is not a leep year.'.format(year))
