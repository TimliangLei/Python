import random
import time

x=list(range(10000))
y=set(range(10000))
z=dict(zip(range(1000),range(10000)))
r=random.randint(0,9999)
start=time.time()
for i in range(99999):
    r in x
end = time.time()
print('list,time used:',end-start)
start=time.time()
for i in range(99999):
    r in y
end = time.time()
print('set,time used:',end-start)
start=time.time()
for i in range(99999):
    r in z
end = time.time()
print('dict,time used:',end-start)
