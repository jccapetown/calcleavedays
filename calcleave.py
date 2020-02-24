#!/usr/bin/python

import datetime
from datetime import date
import os

def easter( year):
    "Returns Easter as a date object."
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    return date(year, month, day)


if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')

#print easter(2020)
#print easter(2020)- datetime.timedelta(days=2)
#get the input between the two days
sfirstday = raw_input('First Day (ddmmyyyy): ')
slastday =  raw_input('Last Day  (ddmmyyyy): ') 
#sfirstday = '16122015'
#slastday = '06012016' 

#calculate the date now
now= datetime.datetime.now()

#make the first input a date
dfirstday = datetime.datetime.strptime(sfirstday, "%d%m%Y").date()
dfirstyear = datetime.datetime.strptime(sfirstday, "%d%m%Y").date().year
#make the second input a date
dlastday = datetime.datetime.strptime(slastday, "%d%m%Y").date()
dlastyear = datetime.datetime.strptime(slastday, "%d%m%Y").date().year


origholdaylist = ['0101', '2103', '2704', '0105', '1606', '1008', '2410', '1612', '2512', '2612']
holidaynames={'0101' : "New Years", 
             '2103' : 'Human Rights Day',
             '2704' : 'Freedom Day',
             '0105' : 'International Workers Day',
             '1606' : 'Youth Day',
             '1008' : "National Woman's Day",
             '2410' : 'Heritage Day',
             '1612' : 'Day Of Reconciliation',
             '2512' : 'Christmas Day',
             '2612' : 'Boxing Day'}

calcholdaylist = []

for year in range(dfirstyear, dlastyear+1):
	for holday in origholdaylist:
		if datetime.datetime.strptime(holday + str(year), "%d%m%Y").date().weekday() == 6:
 			calcholdaylist.append(datetime.datetime.strptime(holday + str(year), "%d%m%Y").date() + datetime.timedelta(days=1))
			#print "Sunday %s moved to monday %s" % ( datetime.datetime.strptime(holday + str(year), "%d%m%Y").date(), datetime.datetime.strptime(holday + str(year), "%d%m%Y").date() + datetime.timedelta(days=1))
		else:
			calcholdaylist.append(datetime.datetime.strptime(holday + str(year), "%d%m%Y").date())
	EasterFriday = easter(year)- datetime.timedelta(days=2)
        holidaynames[EasterFriday.strftime("%d%m")] = 'Good Friday (Easter Friday)'
        calcholdaylist.append(easter(year)- datetime.timedelta(days=2))
	
        EasterMonday = easter(year)+ datetime.timedelta(days=1)
        holidaynames[EasterMonday.strftime("%d%m")] = 'Family Day (Easter Monday)'
	calcholdaylist.append(easter(year)+ datetime.timedelta(days=1))
        print holidaynames

#holday = '1611'
#print datetime.datetime.strptime(holday, "%d%m").date().day

tmpdate = dfirstday
print tmpdate.strftime('%A')
TotalHolidays = 0
FoundHolidays= []
TotalWorkDays= 0
WorkDays = []
weekenddays = 0
while True:
	if tmpdate.weekday() not in (5,6): #If it not is a sunday or a saturday
		found = False
		for holday in calcholdaylist:
			if tmpdate == holday:
				found = True
				TotalHolidays += 1
                                reworkhol = holday.strftime('%d%m')
				FoundHolidays.append("%s - %s" % (tmpdate, holidaynames[reworkhol]) )
				break;
		if not found:
			WorkDays.append(tmpdate)
			TotalWorkDays += 1
		
	else:
		weekenddays += 1

	if tmpdate == dlastday:
		break;
	tmpdate += datetime.timedelta(days=1)

print ""
print 'From %s to %s' % (dfirstday, dlastday)
print 'Days: ' + str( dlastday - dfirstday)
print 'Weekends: %s' % (weekenddays/2)
print 'Work Days: ' + str(TotalWorkDays)
for workday in WorkDays:
  print '-'*2, workday, "(",workday.strftime('%A'),")"
print 'Holidays: ' + str(TotalHolidays)
for holiday in FoundHolidays:
  print '-'*2, holiday
print ''

