import datetime


count = 10000000000000

message = "trump 2024"

def delay(seconds):
    start = datetime.datetime.now()
    while (datetime.datetime.now() - start).total_seconds() < seconds:
        pass

for _ in range(count):
    print(message)
    delay(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)  
    
