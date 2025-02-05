import time
timestamp=time.strftime("%H:%M:%S")
#hour=int(time.strftime("%H"))
hour=int(input("Enter time to check :"))
print(hour)
if(hour>=0 and hour<12):
    print("Good morning sir !")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir !")
elif(hour>=17 and hour<20):
    print("Good evening sir !")
else:
    print("Good night Sir !")            
