import datetime

date = datetime.date(2021,2,4)
print(date)

current = datetime.date.today()
print(current)

time = datetime.time(12,32,56)
print(time)

now = datetime.datetime.now()

now = now.strftime("%d-%m-%Y, %H:%M:%S")
print(now)

taget_time = datetime.datetime(2025,12,5,1,5,56)
current_time = datetime.datetime.now()

print("has not passed" if taget_time > current_time  else print("has passed the date"))
    
