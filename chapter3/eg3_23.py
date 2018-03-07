import time
def demo(m,n):
    if m>n:
        m,n=n,m
    p=m*n
    while m!=0:
        r = n%m
        n=m
        m=r
    return(n,p/n)

def mydemo(m,n):
    import math
    r = math.gcd(m,n)
    return(r,int(m*n/r))

start=time.time()
print(demo(20,30))
print("demo time:",time.time()-start)

start=time.time()
print(mydemo(20,30))
print("mydemo time:",time.time()-start)
