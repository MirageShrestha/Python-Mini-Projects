import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

t = int(time.strftime('%H'))

if(t<12):
    print("good moring")
elif(12<=t<=18):
    print("good afternoon")
elif(18<t<22):
    print("good eving")
else:
    print("good night")