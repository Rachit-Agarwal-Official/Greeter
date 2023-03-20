# Importing time module
import time

# Putting the local time into the variables
hour = int(time.strftime("%H"))
min = int(time.strftime("%M"))
sec = int(time.strftime("%S"))

# Timestamps
# Morning = 4 to 12
# Afternoon = 12 to 17
# Evening = 17 to 19
# Night = 19 to 3

# Logic to get the timestamps in action
if hour >= 4 and hour <= 11 and min <= 59:
    print("Good Morning Sir")
elif hour >= 12 and hour <= 16 and min <= 59:
    print("Good Afternoon Sir")
elif hour >= 17 and hour <= 18 and min <= 59:
    print("Good Evening Sir")
else:
    print("Good Night Sir")

# Changing the time from 24 hours to 12 hours format and putting AM/PM
if hour == 12:
    section = "PM"
elif hour > 12:
    hour -= 12
    section = "PM"
else:
    section = "AM"


# Printing the current time
print("Current Time is: ", end = "")
print(hour, min, sec, sep = ":", end = " ")

if section == "AM":
    print("AM")
else:
    print("PM")