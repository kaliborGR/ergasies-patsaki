import datetime
now=datetime.datetime.now()

nyear=now.year
nmonth=now.month
nday=now.day


new= str(raw_input("insert a date: "))

new_date = datetime.datetime.strptime(new,'%m/%d/%y')
year=new_date.year
month=new_date.month
day=new_date.day

eyear=year-nyear
emonth=month-nmonth
eday=day-nday

print(new)
print(year,month,day)
print(nyear,nmonth,nday)
print(eyear,emonth,eday)

print (eday,'days',emonth,'months',eyear,'years')