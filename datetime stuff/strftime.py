from datetime import date
d = date.fromordinal(730920) # 730920th day after 1. 1. 0001
d
datetime.date(2002, 3, 11)

# Methods related to formatting string output
d.isoformat()
'2002-03-11'
d.strftime("%d/%m/%y")
'11/03/02'
d.strftime("%A %d. %B %Y")
'Monday 11. March 2002'
d.ctime()
'Mon Mar 11 00:00:00 2002'
'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
'The day is 11, the month is March.'

# Methods for to extracting 'components' under different calendars
t = d.timetuple()
for i in t:     
    print(i)
2002                # year
3                   # month
11                  # day
0
0
0
0                   # weekday (0 = Monday)
70                  # 70th day in the year
-1
ic = d.isocalendar()
for i in ic:    
    print(i)
2002                # ISO year
11                  # ISO week number
1                   # ISO day number ( 1 = Monday )

# A date object is immutable; all operations produce a new object
d.replace(year=2005)
datetime.date(2005, 3, 11)
