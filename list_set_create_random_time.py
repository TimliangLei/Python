import random
import time

def RandomNumbers1(number,start,end):
    data=[]
    while True:
        element = random.randint(start,end)
        if element not in data:
            data.append(element)
        if len(data)==number:
            break
    return data

def RandomNumber2(number,start,end):
    data=set()
    while True:
        element = random.randint(start,end)
        data.add(element)
        if len(data) == number:
            return data
start = time.time()
for i in range(10000):
    d1=RandomNumbers1(500,1,10000)
print('Time used:',time.time()-start)

start = time.time()
for i in range(10000):
    d1=RandomNumbers2(500,1,10000)
print('Time used:',time.time()-start)
