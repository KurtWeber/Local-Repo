import random
num = random.randrange(1,11)
print(num)
modnum = num % 2
if modnum == 0:
 print ("Heads")
else:
 print ("Tails")