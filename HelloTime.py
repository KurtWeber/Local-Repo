import time
fName = input("Please enter your first name: ")
print("Hello " + fName + "!")
t = time.localtime()
d = time.localtime()
current_date = time.strftime("%B %d, %Y", d)
current_time = time.strftime("%I:%M %p", t)
print("Today is:", current_date)
print("The current time is:", current_time)