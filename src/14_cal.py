"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime
from datetime import date


def print_calendar(m, y):
  d = date.today()
  cal = calendar.TextCalendar(calendar.SUNDAY)
  output = None

  print("month", month)
  print("year", year)
  if not m and not y:
    output = cal.formatmonth(d.year, d.month)
    print(output)
  if m and not y:
    output = cal.formatmonth(d.year, int(m))
    print(output)
  if m and y:
    output = cal.formatmonth(int(y), int(m))
    print(output)



month = input("Month: ")
year = input("Year: ")

print_calendar(month, year)
