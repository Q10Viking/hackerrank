import calendar

date_txt = calendar.TextCalendar(firstweekday=6).formatyear(2019)
#print(date_txt)
f = open('./calendar_2019.txt','w')
f.write(date_txt)
f.close()