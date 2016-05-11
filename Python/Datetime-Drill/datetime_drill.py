from datetime import datetime, time


now = datetime.now()
now_time = now.time()


if now_time >= time(6,00) and now_time <= time(18,00):
    print ('The New York office is Open')
else:
    print ('The New York office is Closed')

if now_time >= time(1,00) and now_time <= time(13,00):
    print ('The London office is Open')
else:
    print ('The London office is Closed')
