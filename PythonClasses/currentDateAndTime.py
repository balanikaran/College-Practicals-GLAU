import time

# time in seconds since mid night, 1 Jan,1970
totalTimeSeconds = int(time.time())

# getting current second
currentSecond = totalTimeSeconds % 60
currentSecondIST = totalTimeSeconds % 60

# getting total minutes since mid night, 1 Jan, 1970
totalMinutes = totalTimeSeconds // 60
totalMinutesIST = totalTimeSeconds // 60 +5

# getting current minute
currentMinute = totalMinutes % 60
currentMinuteIST = totalMinutesIST % 60

# getting total hours since mid night, 1 Jan, 1970
totalHours = totalMinutes // 60
totalHoursIST = totalMinutes // 60 +30

# getting current hour
currentHour = totalHours % 24
currentHourIST = totalHoursIST % 24

print ("Time right now GMT: ", currentHour,":",currentMinute,":",currentSecond)
print ("Time right now IST: ", currentHourIST,":",currentMinuteIST,":",currentSecondIST)